from typing import Any
from highcharts_core.utility_functions import *

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

from validator_collection import checkers

def format_monday_columns(column_definition, field_name, value):
    """Format the ``value`` found in ``field_name`` to be human-readable.
    
    :param column_definition: The column definition object returned by the Monday.com 
      API.
    :type column_definition: :class:`dict <python:dict>`
    
    :param field_name: The name of the field to format.
    :type field_name: :class:`str <python:str>`
    
    :param value: The value to format.
    :type value: any
    
    :returns: The formatted value.
    
    """
    def default(column_definition, field_name, value):
        return value
    
    def text_field(column_definition, field_name, value):
        return json.loads(value)
    
    def date_field(column_definition, field_name, value):
        if value is None:
            return None
        value = json.loads(value)['date']
        
        return validators.date(value, allow_empty = True)
        
    def numeric_field(column_definition, field_name, value):
        if value is None:
            return None
        return json.loads(value)
    
    def longtext_field(column_definition, field_name, value):
        if value is None:
            return None
        value = json.loads(value)['text']
        value = value.strip()
        if not value:
            return None
        
        return value
    
    def color_field(column_definition, field_name, value):
        if value is None:
            return None
        labels = json.loads(column_definition[field_name]['settings_str'])['labels']
        value = labels.get(str(json.loads(value)['index']))
    
        return value
    
    def dropdown_field(column_definition, field_name, value):
        if value is None:
            return None
        
        labels = json.loads(column_definition[field_name]['settings_str'])['labels']
        label_map = { row['id']:row['name'] for row in labels }
        
        values = [label_map.get(id, None) for id in json.loads(value)['ids']]
        
        return values
    
    type_to_formatter_map = {
        'color': color_field,
        'dropdown': dropdown_field,
        'long-text': longtext_field,
        'date': date_field,
        'numeric': numeric_field,
        'text': text_field
    }
    
    type_ = column_definition[field_name]['type']
    formatter = type_to_formatter_map.get(type_, default)
    
    return formatter(column_definition, field_name, value)


def parse_jira_issue(issue,
                     connection_kwargs = None,
                     connection_callback = None):
    """Return a :class:`dict <python:dict>` whose keys are 
    :class:`GanttData <highcharts_gantt.options.series.data.gantt.GanttData>` 
    properties and values are corresponding field values parsed from ``issue``.
    
    :param issue: The JIRA :class:`Issue <jira:jira.resources.Issue>` to parse.
    :type issue: :class:`Issue <jira:jira.resources.Issue>`
    
    :returns: A :class:`dict <python:dict>` whose keys are 
      :class:`GanttData <highcharts_gantt.options.series.data.gantt.GanttData>` 
      properties and values are corresponding field values parsed from ``issue``.
    :rtype: :class:`dict <python:dict>`
    """
    if not checkers.is_type(issue, 'Issue'):
        raise errors.HighchartsValueError(f'parse_jira_isuse() expects a jira Issue '
                                          f'instance. Received: '
                                          f'{issue.__class__.__name__}.')

    worklogs_sorted_by_start = sorted(issue.worklog.worklogs, 
                                      key = lambda x: validators.datetime(x.started))
    if issue.status.name == 'Duplicate':
        raise errors.DuplicateJIRAIssueError()

    is_finished = issue.status.name in ['Fixed',
                                        'Done',
                                        'Resolved',
                                        'Closed',
                                        'Declined',
                                        'Completed',
                                        "Won't fix",
                                        "Won't do",
                                        'Cannot reproduce',
                                        'Known error',
                                        'Hardware failure',
                                        'Software failure',
                                        'Approved',
                                        'Cancelled',
                                        'Rejected',
                                        'Published',
                                        'Accepted',
                                        'Lost',
                                        'Won',
                                        'Purchased'] or \
                  issue.resolution.name in ['Fixed',
                                            'Done',
                                            'Resolved',
                                            'Closed',
                                            'Declined',
                                            'Completed',
                                            "Won't fix",
                                            "Won't do",
                                            'Cannot reproduce',
                                            'Known error',
                                            'Hardware failure',
                                            'Software failure',
                                            'Approved',
                                            'Cancelled',
                                            'Rejected',
                                            'Published',
                                            'Accepted',
                                            'Lost',
                                            'Won',
                                            'Purchased']
    
    data_point_kwargs = {}
    if not is_finished:
        data_point_kwargs['end'] = issue.duedate
        data_point_kwargs['completed'] = None
    else:
        data_point_kwargs['end'] = validators.datetime(issue.statuscategorychangedate)
        data_point_kwargs['completed'] = 1

    data_point_kwargs['start'] = validators.datetime(
        worklogs_sorted_by_start[0].started)
    data_point_kwargs['id'] = issue.id
    data_point_kwargs['name'] = issue.summary
    data_point_kwargs['description'] = issue.description
    
    data_point_kwargs['parent'] = getattr(issue, 'parent', None)

    dependencies = []
    for item in issue.issuelinks:
        if item.type.name == 'Duplicate':
            continue
        inward_issue = item.inwardIssue
        if connection_callback:
            connection = connection_callback(connection_target = inward_issue,
                                             issue = issue)
        elif connection_kwargs:
            connection = connection_kwargs
            connection['to'] = inward_issue.id
        else:
            connection = inward_issue.id
        dependencies.append(connection)

    if dependencies:
        data_point_kwargs['dependency'] = dependencies
    data_point_kwargs['custom'] = issue.raw
    
    return data_point_kwargs