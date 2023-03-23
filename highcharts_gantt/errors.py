from highcharts_core.errors import *


class AsanaAuthenticationError(HighchartsValueError):
    """:exc:`ValueError <python:ValueError>` encountered when trying to call 
    :meth:`GanttSeries.from_asana() <highcharts_gantt.options.series.gantt.GanttSeries.from_asana>` 
    with improperly configured authentication."""
    pass


class MondayAuthenticationError(HighchartsValueError):
    """:exc:`ValueError <python:ValueError>` encountered when trying to call 
    :meth:`GanttSeries.from_monday() <highcharts_gantt.options.series.gantt.GanttSeries.from_monday>` 
    with improperly configured authentication."""
    pass


class MondayBoardNotFoundError(HighchartsValueError):
    """:exc:`ValueError <python:ValueError>` encountered when an indicated Monday.com board was not found."""
    pass


class MondayItemNotFoundError(HighchartsValueError):
    """:exc:`ValueError <python:ValueError>` encountered when an indicated Monday.com item (task) was not found."""
    pass


class MondayTemplateError(HighchartsValueError):
    """:exc:`ValueError <python:ValueError>` encountered when attempting to apply a 
    Monday.com template that is not supported by **Highcharts Gantt for Python**.
    """
    pass


class JIRAAuthenticationError(HighchartsValueError):
    """:exc:`ValueError <python:ValueError>` encountered when trying to call 
    :meth:`GanttSeries.from_jira() <highcharts_gantt.options.series.gantt.GanttSeries.from_jira>` 
    with improperly configured authentication."""
    pass


class JIRAProjectNotFoundError(HighchartsValueError):
    """:exc:`ValueError <python:ValueError>` encountered when the JIRA project key specified in
    :meth:`GanttSeries.load_from_jira() <highcharts_gantt.options.series.gantt.GanttSeries.load_from_jira>` 
    is not found. 
    
    .. tip::
    
      This often occurs when the JIRA API client silently fails authentication, which can happen when using JIRA
      Cloud.

    """
    pass

class JIRADuplicateIssueError(HighchartsValueError):
    """:exc:`ValueError <python:ValueError>` encountered when encountering a JIRA issue 
    that is a duplicate of another issue."""
    pass
