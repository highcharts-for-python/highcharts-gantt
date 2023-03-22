"""Defines a set of constants that are used throughout the library."""
from highcharts_core.constants import *


GANTT_INCLUDE_LIBS = [
    "https://code.highcharts.com/gantt/modules/gantt.js",
    "https://code.highcharts.com/stock/highcharts-more.js",
    "https://code.highcharts.com/stock/highcharts-more.src.js",
    "https://code.highcharts.com/stock/modules/exporting.js",
    "https://code.highcharts.com/stock/modules/exporting.src.js",
    "https://code.highcharts.com/stock/modules/drilldown.js",
    "https://code.highcharts.com/stock/modules/drilldown.src.js",
    "https://code.highcharts.com/stock/modules/solid-gauge.js",
    "https://code.highcharts.com/stock/modules/solid-gauge.src.js"
]

GANTT_INCLUDE_STR = """<script src="https://code.highcharts.com/gantt/modules/gantt.js"></script>"""


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
