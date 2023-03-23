"""Tests for ``highcharts.no_data``."""
import os
import pytest

from json.decoder import JSONDecodeError

from highcharts_gantt.options.series.gantt import GanttSeries as cls
from highcharts_gantt.options.series.data.connect import DataConnection
from highcharts_gantt import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

from dotenv import load_dotenv

load_dotenv()

STANDARD_PARAMS = [
    ({}, None),
    ({
      'group_z_padding': 4,
      'partial_fill': {
        'fill': '#cccccc'
      }
    }, None),
    # + Gantt Connector Options
    ({
        'connectors': {
            'dash_style': 'Solid',
            'end_marker': {
                'enabled': True,
                'fill_color': '#cccccc',
                'height': 24,
                'line_width': 2,
                'radius': 2,
                'states': {
                    'hover': {
                        'enabled': True
                    }
                },
                'symbol': 'circle',
                'width': 48
            },
            'line_color': '#ccc',
            'line_width': 2,
            'marker': {
                'enabled': True,
                'fill_color': '#cccccc',
                'height': 24,
                'line_width': 2,
                'radius': 2,
                'states': {
                    'hover': {
                        'enabled': True
                    }
                },
                'symbol': 'circle',
                'width': 48
            },
            'start_marker': {
                'enabled': True,
                'fill_color': '#cccccc',
                'height': 24,
                'line_width': 2,
                'radius': 2,
                'states': {
                    'hover': {
                        'enabled': True
                    }
                },
                'symbol': 'circle',
                'width': 48
            },
        }
    }, None),
    # + Base Bar Options
    ({
      'group_z_padding': 4,
      'partial_fill': {
        'fill': '#cccccc'
      },

      'border_color': '#ccc',
      'border_radius': 4,
      'border_width': 2,
      'center_in_category': True,
      'color_by_point': True,
      'colors': [
          '#fff',
          'ccc',
          {
            'linearGradient': {
                'x1': 0.123,
                'x2': 0.567,
                'y1': 0.891,
                'y2': 0.987
            },
            'stops': [
                [0.123, '#cccccc'],
                [0.456, '#ff0000'],
                [1, '#00ff00']
            ]
          },
          {
            'animation': {
                'defer': 5
            },
            'patternOptions': {
                'aspectRatio': 0.5,
                'backgroundColor': '#999999',
                'id': 'some_id_goes_here',
                'opacity': 0.5,
                'width': 120,
                'x': 5,
                'y': 10
            },
            'patternIndex': 2
          }
      ],
      'grouping': False,
      'group_padding': 6,
      'max_point_width': 12,
      'min_point_length': 12,
      'point_padding': 6,
      'point_range': 24,
      'point_width': 12
    }, None),
    # + Base Bar + Series + Generic
    ({
      'group_z_padding': 4,
      'partial_fill': {
        'fill': '#cccccc'
      },

      'border_color': '#ccc',
      'border_radius': 4,
      'border_width': 2,
      'center_in_category': True,
      'color_by_point': True,
      'colors': [
          '#fff',
          'ccc',
          {
            'linearGradient': {
                'x1': 0.123,
                'x2': 0.567,
                'y1': 0.891,
                'y2': 0.987
            },
            'stops': [
                [0.123, '#cccccc'],
                [0.456, '#ff0000'],
                [1, '#00ff00']
            ]
          },
          {
            'animation': {
                'defer': 5
            },
            'patternOptions': {
                'aspectRatio': 0.5,
                'backgroundColor': '#999999',
                'id': 'some_id_goes_here',
                'opacity': 0.5,
                'width': 120,
                'x': 5,
                'y': 10
            },
            'patternIndex': 2
          }
      ],
      'grouping': False,
      'group_padding': 6,
      'max_point_width': 12,
      'min_point_length': 12,
      'point_padding': 6,
      'point_range': 24,
      'point_width': 12,

      'animation_limit': 10,
      'boost_blending': '#ccc',
      'boost_threshold': 1234,
      'color_axis': 1,
      'color_index': 5,
      'color_key': 'some-key-value',
      'connect_ends': True,
      'connect_nulls': True,
      'crisp': True,
      'crop_threshold': 123,
      'data_sorting': {
          'enabled': True,
          'matchByName': True,
          'sortKey': 'some-key-value'
      },
      'drag_drop': {
          'draggableX': True,
          'draggableY': True,
          'dragHandle': {
              'className': 'draghandle-classname-goes-here',
              'color': '#ccc',
              'cursor': 'alias',
              'lineColor': '#ddd',
              'lineWidth': 2,
              'pathFormatter': """function() { return true; }""",
              'zIndex': 10
          },
          'dragMaxX': 3456,
          'dragMaxY': 6532,
          'dragMinX': 123,
          'dragMinY': 321,
          'dragPrecisionX': 5,
          'dragPrecisionY': 5,
          'dragSensitivity': 2,
          'groupBy': 'some-property-name',
          'guideBox': {
              'default': {
                  'className': 'some-classname-goes-here',
                  'color': '#999',
                  'cursor': 'pointer',
                  'lineColor': '#ccc',
                  'lineWidth': 2,
                  'zIndex': 100
              }
          },
          'liveRedraw': True
      },
      'find_nearest_point_by': 'x',
      'get_extremes_from_all': True,
      'linecap': 'round',
      'line_width': 2,
      'negative_color': '#fff',
      'point_interval': 5,
      'point_interval_unit': 'weeks',
      'point_placement': 'on',
      'point_start': 12,
      'relative_x_value': True,
      'shadow': False,
      'soft_threshold': True,
      'stacking': 'normal',
      'step': 'left',
      'zone_axis': 'y',
      'zones': [
          {
            'className': 'some-class-name1',
            'color': '#999999',
            'dashStyle': 'Solid',
            'fillColor': '#cccccc',
            'value': 123
          },
          {
            'className': 'some-class-name1',
            'color': '#999999',
            'dashStyle': 'Solid',
            'fillColor': '#cccccc',
            'value': 123
          },
          {
            'className': 'some-class-name1',
            'color': '#999999',
            'dashStyle': 'Solid',
            'fillColor': '#cccccc',
            'value': 123
          }
      ],

      'accessibility': {
          'description': 'Description goes here',
          'enabled': True,
          'exposeAsGroupOnly': True,
          'keyboardNavigation': {
              'enabled': True
          },
          'point': {
              'dateFormat': 'format string',
              'dateFormatter': """function() { return true; }""",
              'describeNull': False,
              'descriptionFormatter': """function() { return true; }""",
              'valueDecimals': 2,
              'valueDescriptionFormat': 'format string',
              'valuePrefix': '$',
              'valueSuffix': 'USD'
          },
      },
      'allow_point_select': True,
      'animation': {
          'defer': 5
      },
      'class_name': 'some-class-name',
      'clip': False,
      'color': '#fff',
      'cursor': 'alias',
      'custom': {
          'item1': 'some value',
          'item2': 'some value'
      },
      'dash_style': 'Dash',
      'data_labels': {
        'align': 'center',
        'allowOverlap': True,
        'animation': {
            'defer': 5
        },
        'backgroundColor': {
            'linearGradient': {
                'x1': 0.123,
                'x2': 0.234,
                'y1': 0.345,
                'y2': 0.456
            },
            'stops': [
                [0.12, '#999'],
                [0.34, '#fff']
            ]
        },
        'borderColor': '#999999',
        'borderRadius': 24,
        'borderWidth': 1,
        'className': 'some-class-name',
        'color': '#000000',
        'crop': True,
        'defer': False,
        'enabled': True,
        'filter': {
            'operator': '>=',
            'property': 'some_property',
            'value': 123
        },
        'format': 'some format',
        'formatter': """function() { return true; }""",
        'inside': True,
        'nullFormat': 'some format',
        'nullFormatter': """function() { return true; }""",
        'overflow': 'none',
        'padding': 12,
        'position': 'center',
        'rotation': 0,
        'shadow': False,
        'shape': 'rect',
        'style': 'style goes here',
        'useHTML': False,
        'verticalAlign': 'top',
        'x': 10,
        'y': 20,
        'z': 0
      },
      'description': 'Description goes here',
      'enable_mouse_tracking': True,
      'events': {
        'afterAnimate': """function(event) { return true; }""",
        'click': """function(event) { return true; }""",
        'hide': """function(event) { return true; }""",
        'mouseOut': """function(event) { return true; }""",
        'show': """function(event) { return true; }"""
      },
      'include_in_data_export': True,
      'keys': [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      'label': {
          'boxesToAvoid': [
              {
               'bottom': 12,
               'left': -46,
               'right': 84,
               'top': 24
              },
              {
               'bottom': 48,
               'left': -46,
               'right': 84,
               'top': 86
              }
          ],
          'connectorAllowed': True,
          'connectorNeighbourDistance': 12,
          'enabled': True,
          'format': 'format string',
          'formatter': """function() { return true; }""",
          'maxFontSize': 18,
          'minFontSize': 6,
          'onArea': False,
          'style': 'some style string'
      },
      'linked_to': 'some_id',
      'marker': {
        'enabled': True,
        'fillColor': '#cccccc',
        'height': 24,
        'lineWidth': 2,
        'radius': 2,
        'states': {
            'hover': {
                'enabled': True
            }
        },
        'symbol': 'circle',
        'width': 48
      },
      'on_point': {
          'connectorOptions': {
              'dashstyle': 'Dash',
              'stroke': '#ccc',
              'width': 2
          },
          'id': 'some-id',
          'position': {
              'align': 'left',
              'verticalAlign': 'top',
              'x': 15,
              'y': -46
          }
      },
      'opacity': 0.2,
      'point': {
          'events': {
            'click': """function(event) { return true; }""",
            'drag': """function(event) { return true; }""",
            'drop': """function(event) { return true; }""",
            'mouseOut': """function(event) { return true; }"""
          }
      },
      'point_description_formatter': """function (point) { return true; }""",
      'selected': False,
      'show_checkbox': True,
      'show_in_legend': True,
      'skip_keyboard_navigation': False,
      'states': {
        'hover': {
            'animation': {
                'duration': 123
            },
            'borderColor': '#cccccc',
            'brightness': 0.3,
            'enabled': True
        },
        'inactive': {
            'enabled': True,
            'opacity': 0.5
        },
        'normal': {
            'animation': {
                'defer': 24
            }
        },
        'select': {
            'color': '#ff0000',
            'enabled': True,
        }
      },
      'sticky_tracking': True,
      'threshold': 123,
      'tooltip': {
        'animation': True,
        'backgroundColor': '#ccc',
        'borderColor': '#999',
        'borderRadius': 4,
        'borderWidth': 1,
        'className': 'some-class-name',
        'clusterFormat': 'format string',
        'dateTimeLabelFormats': {
          'day': 'test',
          'hour': 'test',
          'millisecond': 'test',
          'minute': 'test',
          'month': 'test',
          'second': 'test',
          'week': 'test',
          'year': 'test'
        },
        'distance': 12,
        'enabled': True,
        'followPointer': True,
        'followTouch_move': True,
        'footerFormat': 'format string',
        'formatter': """function() { return true; }""",
        'headerFormat': 'format string',
        'headerShape': 'circle',
        'hideDelay': 3,
        'nullFormat': 'format string',
        'nullFormatter': """function() { return true; }""",
        'outside': False,
        'padding': 6,
        'pointFormat': 'format string',
        'pointFormatter': """function() { return true; }""",
        'positioner': """function() { return true; }""",
        'shadow': False,
        'shape': 'rect',
        'shared': False,
        'snap': 4,
        'split': False,
        'stickOnContact': True,
        'style': 'style string goes here',
        'useHTML': False,
        'valueDecimals': 2,
        'valuePrefix': '$',
        'valueSuffix': ' USD',
        'xDateFormat': 'format string'
       },
      'turbo_threshold': 456,
      'visible': True
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_GanttSeries__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_GanttSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_GanttSeries_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_GanttSeries_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('plot_options/gantt/01.js', False, None),
    ('plot_options/gantt/02.js', False, None),

    ('plot_options/gantt/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
    ('plot_options/gantt/error-02.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('plot_options/gantt/01.js', True, None),
    ('plot_options/gantt/02.js', True, None),

    ('plot_options/gantt/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
    ('plot_options/gantt/error-02.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_GanttSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)


def callback_function(connection_target, task):
    return DataConnection(to = connection_target['gid'],
                          type = 'straight')


@pytest.mark.parametrize('kwargs, expected_data_points, error', [
    ({}, 5, None),
    ({'completed_since': '2023-03-22'}, 2, None),

    # Connection Callback
    ({ 'connection_callback': callback_function }, 5, None),

    # Errors
    ({}, 0, errors.AsanaAuthenticationError),
])
def test_GanttSeries_from_asana(kwargs, expected_data_points, error):
    project_gid = os.getenv('ASANA_PROJECT_GID', None)
    section_gid = os.getenv('ASANA_SECTION_GID', None)
    
    kwargs['project_gid'] = project_gid
    kwargs['section_gid'] = section_gid
    
    if not error:
        personal_access_token = os.getenv('ASANA_PERSONAL_ACCESS_TOKEN', None)
        
        kwargs['personal_access_token'] = personal_access_token
        
        result = cls.from_asana(**kwargs)
        assert result is not None
        assert isinstance(result, cls) is True
        assert len(result.data) == expected_data_points
    elif error == errors.AsanaAuthenticationError:
        kwargs['personal_access_token'] = 'invalid-token-goes-here'

        with pytest.raises(error):
            result = cls.from_asana(**kwargs)
    elif error:
        with pytest.raises(error):
            result = cls.from_asana(**kwargs)
            
@pytest.mark.parametrize('kwargs, expected_data_points, error', [
    ({ 'template': 'task-management' }, 7, None),

    # Errors
    ({}, 0, errors.MondayAuthenticationError),
])
def test_GanttSeries_from_monday(kwargs, expected_data_points, error):
    board_id = os.getenv('MONDAY_BOARD_ID', None)
    
    kwargs['board_id'] = board_id
    
    if not error:
        personal_access_token = os.getenv('MONDAY_API_TOKEN', None)
        
        kwargs['api_token'] = personal_access_token
        
        result = cls.from_monday(**kwargs)
        assert result is not None
        assert isinstance(result, cls) is True
        assert len(result.data) == expected_data_points
    elif error == errors.MondayAuthenticationError:
        kwargs['api_token'] = 'invalid-token-goes-here'

        with pytest.raises(error):
            result = cls.from_monday(**kwargs)
    elif error:
        with pytest.raises(error):
            result = cls.from_monday(**kwargs)
            

@pytest.mark.parametrize('kwargs, expected_data_points, error', [
    ({}, 6, None),

    # Errors
    ({}, 0, (errors.JIRAAuthenticationError, errors.JIRAProjectNotFoundError)),
])
def test_GanttSeries_from_jira(kwargs, expected_data_points, error):
    kwargs['project_key'] = os.getenv('JIRA_PROJECT_ID')
    
    if not error:
        result = cls.from_jira(**kwargs)
        assert result is not None
        assert isinstance(result, cls) is True
        assert len(result.data) == expected_data_points
    elif error == (errors.JIRAAuthenticationError, errors.JIRAProjectNotFoundError):
        kwargs['username'] = 'invalid-username'
        kwargs['password_or_token'] = 'invalid-token'

        with pytest.raises(error):
            result = cls.from_jira(**kwargs)
    else:
        with pytest.raises(error):
            result = cls.from_jira(**kwargs)