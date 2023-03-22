import os
from validator_collection import validators, checkers

import logging

logger = logging.getLogger('highcharts_gantt')
logger.setLevel(logging.INFO)

try:
    import orjson as json
except ImportError:
    try:
        import rapidjson as json
    except ImportError:
        try:
            import simplejson as json
        except ImportError:
            import json

try:
    import monday
    HAS_MONDAY = True
except ImportError:
    HAS_MONDAY = False

import requests

from highcharts_gantt import errors


def get_column_definitions(client, board_id):
    """Return a collection of Monday column definitions from the Monday.com API.
    
    :param client: The `monday <https://monday.readthedocs.io/en/latest/>`__ API client
      to use to retrieve the column definitions.
    :type client: :class:`monday.MondayClient <monday:MondayClient>`
    
    :param board_id: The unique identifier of the board whose column definitions should be retrieved.
    :type board_id: :class:`int <python:int>` or :class:`str <python:str>`
    
    :returns: Collection of column definitions from the Monday.com API, with ``id`` as the key and definition as the 
      value.
    :rtype: :class:`dict <python:dict>`
    """
    column_definitions = {}
    try:
        response = client.boards.fetch_columns_by_board_id(board_id)
    except requests.exceptions.HTTPError:
        raise errors.MondayAuthenticationError('The Monday.com API Token returned as unauthorized.')

    data = response['data']
    boards = data['boards']
    columns = []
    for board in boards:
        if board['id'] == str(board_id):
            columns = board['columns']
            break

    for column in columns:
        field_name = column['id']
        column_definitions[field_name] = column

    if not columns:
        raise errors.MondayBoardNotFoundError(f'No column definitions for board ID {board_id} found.')

    return column_definitions


def get_tasks(board_id, api_token = None, log_tasks = False):
    """Return a list of the Monday.com items (tasks) that are present in ``board_id``.

    :param api_token: The Monday.com API token to use when authenticating your
        request against the Monday.com API. Defaults to :obj:`None <python:None>`,
        which will then try to determine the token from the ``MONDAY_API_TOKEN``
        environment variable.
        
        .. warning::
        
        If no token is either passed to the method *or* found in the 
        ``MONDAY_API_TOKEN`` environment variable, calling this method will raise
        an error.
        
    :type api_token: :class:`str <python:str>` or :obj:`None <python:None>`

    :param board_id: The unique identifier of the board whose items should be retrieved.
    :type board_id: :class:`int <python:int>` or :class:`str <python:str>`
    
    :returns: Collection of items. The object is a :class:`dict <python:dict>` representing the
      overall item, with keys:
      * ``'name'`` containing the item's human-readable label
      * ``'columns'`` containing a :class:`dict <python:dict>` with the column values
      * ``'id'`` containing the Monday.com ID of the item
      
    :param log_tasks: if ``True``, then will output the task :class:`dict <python:dict>` object
      at the ``logging.INFO`` level. Defaults to ``False``.
      
      .. tip::
      
        **BEST PRACTICE!**
        
        Setting this value to ``True`` can be useful during initial debugging/development to help you define the 
        ``property_column_map`` to use when creating a Gantt chart from a Monday.com board.
        
    :type log_tasks: :class:`bool <python:bool>`
    
    :rtype: :class:`dict <python:dict>`
    
    :raises MondayBoardNotFoundError: if the ``board_id`` is not found
    """
    if not HAS_MONDAY:
        raise errors.HighchartsDependencyError('the .from_monday() method depends '
                                                'on the monday Python library. That '
                                                'library was not found in your '
                                                'runtime environment.')
    if not api_token:
        api_token = os.getenv('MONDAY_API_TOKEN', None)
    
    if not api_token:
        raise errors.MondayAuthenticationError('.from_monday() requires a '
                                                'Monday.com API token. None was '
                                                'supplied.')

    api_token = validators.string(api_token)
    board_id = validators.integer(board_id)

    client = monday.MondayClient(api_token)

    try:
        column_definitions = get_column_definitions(client, board_id)
    except requests.exceptions.HTTPError:
        raise errors.MondayAuthenticationError('The Monday.com API token returned as unauthorized.')

    response = client.boards.fetch_items_by_board_id([board_id], limit = 100, page = 1)
    data = response['data']
    boards = data['boards']
    if len(boards) == 0:
        raise errors.MondayBoardNotFoundError(f'board_id ({board_id}) was not found')

    items = boards[0]['items']
    
    collection = {}
    for item in items:
        task = convert_item_to_task(item,
                                    column_definitions,
                                    client,
                                    log_tasks = log_tasks)
        task_id = task['id']
        collection[task_id] = task
    
    collection = elevate_subtasks(collection)
    collection = flatten_columns(collection)

    return collection


def convert_item_to_task(item, column_definitions, client, log_tasks = False):
    """Convert the Monday.com ``item`` representation into a more logical data structure.

    :param item: The Monday.com item representation.
    :type item: :class:`dict <python:dict>`
    
    :param column_definitions: The column definition object returned by the Monday.com 
      API.
    :type column_definitions: :class:`dict <python:dict>`
    
    :param client: The `monday <https://monday.readthedocs.io/en/latest/>`__ API client
      to use to retrieve the column definitions. Defaults to :obj:`None <python:None>`
    :type client: :class:`monday.MondayClient <monday:MondayClient>`

    :param log_tasks: if ``True``, then will output the task :class:`dict <python:dict>` object
      at the ``logging.INFO`` level. Defaults to ``False``.

      .. tip::

        **BEST PRACTICE!**

        Setting this value to ``True`` can be useful during initial debugging/development to help you define the 
        ``property_column_map`` to use when creating a Gantt chart from a Monday.com board.

    :type log_tasks: :class:`bool <python:bool>`
    
    :returns: The formatted value.
    """
    task = {}

    task_id = item.get('id', None)

    task['id'] = task_id
    task['name'] = item.get('name', None)
    column_values = item.get('column_values', [])

    columns = {}
    for column in column_values:
        field_name = get_column_title(column, column_definitions)
        columns[field_name] = format_column(column,
                                            column_definitions = column_definitions,
                                            client = client,
                                            parent_id = task_id)
    task['columns'] = columns

    if log_tasks:
        logger.log(logging.INFO, f'Monday.com Item converted to Highcharts Gantt Task dict:\n{task}')

    return task


def format_column(column,
                  column_definitions,
                  client,
                  parent_id = None,
                  log_tasks = False):
    """Format the Monday.com ``column`` representation to be navigable.

    :param column: The Moday.com ``column_value`` representation of the column.
    :type column: :class:`dict <python:dict>`
    
    :param column_definitions: The column definition object returned by the Monday.com 
      API.
    :type column_definition: :class:`dict <python:dict>`
    
    :param client: The `monday <https://monday.readthedocs.io/en/latest/>`__ API client
      to use to retrieve the column definitions. Defaults to :obj:`None <python:None>`
    :type client: :class:`monday.MondayClient <monday:MondayClient>`
    
    :param parent_id: The Monday.com ID of the parent item (task). Defaults to :obj:`None <python:None>`
    :type parent_id: :class:`int <python:int>` or :class:`str <python:str>` or :obj:`None <python:None>`
    
    :param log_tasks: if ``True``, then will output the task :class:`dict <python:dict>` object
      at the ``logging.INFO`` level. Defaults to ``False``.

      .. tip::

        **BEST PRACTICE!**

        Setting this value to ``True`` can be useful during initial debugging/development to help you define the 
        ``property_column_map`` to use when creating a Gantt chart from a Monday.com board.

    :type log_tasks: :class:`bool <python:bool>`

    :returns: The formatted value.
    
    """
    def default(column_definition, field_name, value, text = None, client = None, parent_id = None, log_tasks = False):
        return value
    
    def text_field(column_definition, 
                   field_name, 
                   value, 
                   text = None, 
                   client = None, 
                   parent_id = None, 
                   log_tasks = False):
        if value is None and text is None:
            return None
        
        if text:
            return text
        
        return json.loads(value)
    
    def date_field(column_definition,
                   field_name,
                   value,
                   text = None,
                   client = None,
                   parent_id = None,
                   log_tasks = False):
        if value is None:
            return None
        value = json.loads(value)['date']
        
        return validators.date(value, allow_empty = True, text = None, parent_id = None)
        
    def numeric_field(column_definition,
                      field_name,
                      value,
                      text = None,
                      client = None,
                      parent_id = None,
                      log_tasks = False):
        if value is None:
            return None
        return json.loads(value)
    
    def longtext_field(column_definition,
                       field_name,
                       value,
                       text = None,
                       client = None,
                       parent_id = None,
                       log_tasks = False):
        if value is None:
            return None
        value = json.loads(value)['text']
        value = value.strip()
        if not value:
            return None
        
        return value
    
    def color_field(column_definition,
                    field_name,
                    value,
                    text = None,
                    client = None,
                    parent_id = None,
                    log_tasks = False):
        if value is None:
            return None
        labels = json.loads(column_definition[field_name]['settings_str'])['labels']
        value = labels.get(str(json.loads(value)['index']))
    
        return value
    
    def dropdown_field(column_definition,
                       field_name,
                       value,
                       text = None,
                       client = None,
                       parent_id = None,
                       log_tasks = False):
        if value is None:
            return None

        labels = json.loads(column_definition[field_name]['settings_str'])['labels']
        label_map = { row['id'] : row['name'] for row in labels }

        values = [label_map.get(id, None) for id in json.loads(value)['ids']]

        return values
    
    def timeline_field(column_definition,
                       field_name,
                       value,
                       text = None,
                       client = None,
                       parent_id = None,
                       log_tasks = False):
        if value is None:
            return None
        
        value = json.loads(value)
        
        start = value.get('from', None)
        start = validators.date(start, allow_empty = True)
        
        end = value.get('to', None)
        end = validators.date(end, allow_empty = True)
        
        visualization_type = value.get('visualization_type', None)
        
        values = {
            'start': start,
            'end': end,
            'is_milestone': visualization_type == 'milestone'
        }
        
        return values
    
    def multiple_person_field(column_definition,
                              field_name,
                              value,
                              text = None,
                              client = None,
                              parent_id = None,
                              log_tasks = False):
        if value is None and text is None:
            return None

        if text:
            return text

        if value is None:
            return None
        
        return json.loads(value)
    
    def subtask_field(column_definition,
                      field_name,
                      value,
                      text = None,
                      client = None,
                      parent_id = None,
                      log_tasks = False):
        if not value:
            return None

        value = json.loads(value)

        link_pulse_ids = value.get('linkedPulseIds', [])
        subtasks = {}
        for entry in link_pulse_ids:
            item_id = entry.get('linkedPulseId', None)
            response = client.items.fetch_items_by_id(item_id)
            data = response['data']
            if len(data['items']) > 0:
                item = data['items'][0]
            else:
                raise errors.MondayItemNotFoundError(f'Item ID ({item_id}) was not found')

            task = convert_item_to_task(item,
                                        column_definitions,
                                        client,
                                        log_tasks = log_tasks)
            task['parent_id'] = parent_id
            task_id = task['id']
            subtasks[task_id] = task

        return subtasks

    def dependency_field(column_definition,
                         field_name,
                         value,
                         text = None,
                         client = None,
                         parent_id = None,
                         log_tasks = False):
        if not value:
            return None

        value = json.loads(value)

        link_pulse_ids = value.get('linkedPulseIds', [])
        dependency_ids = [str(x.get('linkedPulseId', None)) for x in link_pulse_ids]
        
        return dependency_ids

    type_to_formatter_map = {
        'color': color_field,
        'dropdown': dropdown_field,
        'long-text': longtext_field,
        'date': date_field,
        'numeric': numeric_field,
        'text': text_field,
        'subtasks': subtask_field,
        'timerange': timeline_field,
        'multiple-person': multiple_person_field,
        'dependency': dependency_field,
    }

    field_name = column['id']
    value = column['value']
    text = column.get('text', None)

    type_ = get_column_type(field_name, column_definitions)
    formatter = type_to_formatter_map.get(type_, default)

    return formatter(column_definitions, field_name, value, text, client, parent_id, log_tasks)


def get_column_title(column, column_definitions):
    """Retrieve the human-readable title given to the column in Monday.com.
    
    :param column: The Monday.com representation of the column whose title is to be retrieved.
    :type column: :class:`dict <python:dict>`
    
    :param column_definitions: The Monday.com representation of the column definition.
    :type column_definitions: :class:`dict <python:dict>`
    
    :returns: The human-readable title given to the column.
    :rtype: :class:`str <python:str>`
    """
    column_id = column['id']
    if column_id.startswith('dependency'):
        return 'dependencies'

    try:
        title = column_definitions[column_id]['title']
    except KeyError as error:
        if column_id.startswith('date'):
            alt_column_id = None
            for key in column_definitions:
                if key.startswith('date'):
                    alt_column_id = key
                    break
            if not alt_column_id:
                raise error
            title = column_definitions[alt_column_id]['title']
        elif 'type' in column and column['type'] == 'dependency':
            title = 'dependencies'
        else:
            raise error

    return title


def get_column_type(column_id, column_definitions):
    """Retrieve the column type given to the column with ``column_id``.
    
    :param column_id: The identifier of the column to retrieve.
    :type column_id: :class:`str <python:str>`
    
    :param column_definitions: The Monday.com representation of the board's column definitions.
    :type column_definitions: :class:`dict <python:dict>`
    
    :returns: The type assigned to the column.
    :rtype: :class:`str <python:str>`
    """
    try:
        type_ = column_definitions[column_id]['type']
    except KeyError as error:
        if column_id.startswith('date'):
            alt_column_id = None
            for key in column_definitions:
                if key.startswith('date'):
                    alt_column_id = key
                    break
            if not alt_column_id:
                raise error
            type_ = column_definitions[alt_column_id]['type']
        else:
            raise error

    return type_


def elevate_subtasks(tasks):
    """Raise sub-tasks to the highest level of the collection.
    
    :param tasks: Collection of Highcharts Gantt for Python task :class:`dict <python:dict>` structures.
    :type tasks: :class:`dict <python:dict>`
    
    :returns: The collection of tasks with no subtask items.
    :rtype: :class:`dict <python:dict>`
    """
    updated_collection = {}
    for task_id in tasks:
        task = tasks[task_id]
        
        new_task = {}
        new_task['id'] = task_id
        
        name = task['name']
        new_task['name'] = name
        new_task['columns'] = {}
        
        columns = task['columns']
        for title in columns:
            column = columns[title]
            if column is None:
                continue
            is_subitems = False
            if title == 'Subitems':
                is_subitems = True
            elif isinstance(column, dict):
                for key in column:
                    if isinstance(column[key], dict) and 'parent_id' in column[key]:
                        is_subitems = True
                        break

            if is_subitems:
                sub_item_tasks = elevate_subtasks(column)
                for key in sub_item_tasks:
                    updated_collection[key] = sub_item_tasks[key]
                    updated_collection[key]['parent_id'] = task_id
            else:
                new_task['columns'][title] = column
                
        updated_collection[task_id] = new_task
    
    return updated_collection


def flatten_columns(tasks):
    """Flatten the ``'columns'`` key, elevating its key/value pairs to the upper level.
    
    :param tasks: Collection of Monday.com tasks.
    :type tasks: :class:`dict <python:dict>`
    """
    collection = {}
    for key in tasks:
        task = tasks[key]
        if not isinstance(task, dict) or 'columns' not in task:
            collection[key] = task
            continue
        new_task = {
            'id': task['id'],
            'name': task['name']
        }
        columns = task['columns']
        for title in columns:
            column = columns[title]
            if isinstance(column, dict) and 'start' in column and 'end' in column:
                new_task['start'] = columns[title]['start']
                new_task['end'] = columns[title]['end']
                new_task['is_milestone'] = columns[title]['is_milestone']
            else:
                new_task[title] = columns[title]
                new_task['is_milestone'] = False

        if 'start' not in new_task and 'Date' in new_task:
            new_task['start'] = new_task['Date']
        if 'end' not in new_task and 'Date' in new_task:
            new_task['end'] = new_task['Date']

        new_task['completed'] = 0
        if 'Status' in new_task:
            task_status = new_task['Status']
            if task_status in ['Done', 'Finished', 'Complete']:
                new_task['completed'] = 1
            elif task_status in ['Working on it', 'In Progress', 'Doing']:
                new_task['completed'] = 0.5

        collection[key] = new_task

    return collection
