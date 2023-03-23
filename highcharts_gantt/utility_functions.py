from typing import Any

from highcharts_core.utility_functions import *

from highcharts_gantt import errors

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

from validator_collection import checkers, validators


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
    if connection_callback and not checkers.is_callable(connection_callback):
        raise errors.HighchartsValueError('connection_callback - if supplied - '
                                            'must be callable.')

    connection_kwargs = validators.dict(connection_kwargs,
                                        allow_empty = True) or {}
    
    from highcharts_gantt.options.series.data.connect import DataConnection

    if not checkers.is_type(issue, 'Issue'):
        raise errors.HighchartsValueError(f'parse_jira_issue() expects a jira Issue '
                                          f'instance. Received: '
                                          f'{issue.__class__.__name__}.')

    worklogs_sorted_by_start = sorted(issue.fields.worklog.worklogs, 
                                      key = lambda x: validators.datetime(x.started))
    if issue.fields.status.name == 'Duplicate':
        raise errors.DuplicateJIRAIssueError()

    if not issue.fields.status and not issue.fields.resolution:
        is_status_finished = None
        is_resolution_finished = None
    elif issue.fields.status:
        is_status_finished = issue.fields.status.name in ['Fixed',
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
        is_resolution_finished = None
    else:
        is_status_finished = None
        is_resolution_finished = issue.fields.resolution.name in ['Fixed',
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
    
    is_finished = is_status_finished or is_resolution_finished
        
    data_point_kwargs = {}
    if not is_finished:
        data_point_kwargs['end'] = issue.fields.duedate
        try:
            data_point_kwargs['completed'] = issue.fields.progress.percent / 100
        except AttributeError:
            data_point_kwargs['completed'] = None
    elif is_resolution_finished:
        data_point_kwargs['end'] = validators.datetime(issue.fields.resolutiondate)
        data_point_kwargs['completed'] = 1
    else:
        data_point_kwargs['end'] = validators.datetime(issue.fields.statuscategorychangedate)
        data_point_kwargs['completed'] = 1

    if len(worklogs_sorted_by_start) > 0:
        data_point_kwargs['start'] = validators.datetime(worklogs_sorted_by_start[0].started)

    data_point_kwargs['id'] = issue.key
    data_point_kwargs['name'] = issue.fields.summary
    data_point_kwargs['description'] = issue.fields.description
    
    parent_issue = getattr(issue.fields, 'parent', None)
    if parent_issue:
        data_point_kwargs['parent'] = parent_issue.key

    dependencies = []
    for item in issue.fields.issuelinks:
        if item.type.name == 'Duplicate':
            if hasattr(item, 'inwardIssue'):
                continue
            else:
                raise errors.JIRADuplicateIssueError

        inward_issue = getattr(item, 'inwardIssue', None)
        if not inward_issue:
            continue

        if connection_callback:
            connection = connection_callback(connection_target = inward_issue.key,
                                             issue = issue)
        elif connection_kwargs:
            connection_kwargs['to'] = inward_issue.key
            connection = DataConnection(**connection_kwargs)
        else:
            connection = DataConnection(to = inward_issue.key)

        dependencies.append(connection)

    if dependencies:
        data_point_kwargs['dependency'] = dependencies

    data_point_kwargs['custom'] = issue.raw

    return data_point_kwargs