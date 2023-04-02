"""Defines a set of constants that are used throughout the library."""
from highcharts_stock.constants import *

GANTT_INCLUDE_LIBS = [x for x in STOCK_INCLUDE_LIBS]
GANTT_INCLUDE_LIBS.extend([
    "https://code.highcharts.com/gantt/modules/gantt.js",
])

GANTT_INCLUDE_STR = STOCK_INCLUDE_STR + """
    <script src="https://code.highcharts.com/gantt/modules/gantt.js"/>
"""


MONDAY_TEMPLATES = {
    'task-management': {
        'id': 'id',
        'name': 'name',
        'start': 'start',
        'end': 'end',
        'parent': 'parent_id',
        'milestone': 'is_milestone',
        'completed': 'completed'
    },
}
