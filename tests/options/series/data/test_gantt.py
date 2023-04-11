"""Tests for ``highcharts.no_data``."""

import pytest
import datetime

from json.decoder import JSONDecodeError
from validator_collection import validators

from highcharts_gantt.options.series.data.gantt import ProgressIndicator as cls, GanttData as cls2
from highcharts_gantt import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
        'amount': 0.5,
        'fill': '#ccc'
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_ProgressIndicator__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_ProgressIndicator__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_ProgressIndicator_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_ProgressIndicator_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/data/gantt/01.js', False, None),

    ('series/data/gantt/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/data/gantt/01.js', True, None),

    ('series/data/gantt/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_ProgressIndicator_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)


######## NEXT CLASS

STANDARD_PARAMS_2 = [
    ({}, None),
    ({
        'collapsed': False,
        'completed': 0.5,
        'dependency': None,
        'milestone': False,
        'parent': 'some-id-goes-here',
        'y': 123
    }, None),
    ({
        'collapsed': False,
        'completed': {
            'amount': 0.5,
            'fill': '#ccc'
        },
        'dependency': None,
        'milestone': False,
        'parent': 'some-id-goes-here',
        'y': 123
    }, None),
    
    # + DataBase
    ({
        'collapsed': False,
        'completed': 0.5,
        'dependency': None,
        'milestone': False,
        'parent': 'some-id-goes-here',
        'y': 123,
        'accessibility': {
            'description': 'Some description goes here',
            'enabled': True
        },
        'class_name': 'some-class-name',
        'color': '#ccc',
        'color_index': 2,
        'custom': {
            'some_key': 123,
            'other_key': 456
        },
        'description': 'Some description goes here',
        'events': {
            'click': """function(event) { return true; }""",
            'drag': """function(event) { return true; }""",
            'drop': """function(event) { return true; }""",
            'mouseOut': """function(event) { return true; }"""
        },
        'id': 'some-id-goes-here',
        'label_rank': 3,
        'name': 'Some Name Goes here',
        'selected': False
    }, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_GanttData__init__(kwargs, error):
    Class__init__(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS_2)
def test_GanttData__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_GanttData_from_dict(kwargs, error):
    Class_from_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS_2)
def test_GanttData_to_dict(kwargs, error):
    Class_to_dict(cls2, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/data/gantt/02.js', False, None),

    ('series/data/gantt/error-02.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/data/gantt/02.js', True, None),

    ('series/data/gantt/error-02.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_GanttData_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls2, input_files, filename, as_file, error)


@pytest.mark.parametrize('kwargs, error', [
    ({
        'task': {
            'id': '4181772228',
            'name': 'Release Highcharts Core for Python',
            'Person': 'Chris Modzelewski',
            'is_milestone': False,
            'Status': 'Done',
            'Date': datetime.date(2023, 3, 21),
            'start': datetime.date(2023, 3, 21),
            'end': datetime.date(2023, 3, 21),
            'completed': 1
        },
        'template': 'task-management'
    }, None),
    ({
        'task': {
            'id': '4181781003',
            'name': 'Release Highcharts Gantt for Python',
            'Person': 'Chris Modzelewski',
            'is_milestone': False,
            'Status': 'Working on it',
            'Date': datetime.date(2023, 3, 31),
            'start': datetime.date(2023, 3, 21),
            'end': datetime.date(2023, 3, 31),
            'dependencies': [4181772232],
            'completed': 0.5
        }
    }, None),
    
    ({
        'task': {
            'id': '4181781003',
            'name': 'Release Highcharts Gantt for Python',
            'Person': 'Chris Modzelewski',
            'is_milestone': False,
            'Status': 'Working on it',
            'Date': datetime.date(2023, 3, 31),
            'start': datetime.date(2023, 3, 21),
            'end': datetime.date(2023, 3, 31),
            'dependencies': [4181772232],
            'completed': 0.5
        },
        'template': 'invalid-template-name'
    }, errors.MondayTemplateError),

])
def test_GanttData_from_monday(kwargs, error):
    if not error:
        result = cls2.from_monday(**kwargs)
        assert result is not None
        assert isinstance(result, cls2) is True
        if 'task' in kwargs:
            task = kwargs['task']
            if 'id' in task:
                assert result.id == task['id']
            if 'name' in task:
                assert result.name == task['name']
            if 'is_milestone' in task:
                assert result.milestone == task['is_milestone']
            if 'start' in task:
                assert (result.start == validators.datetime(task['start']) or
                        result.start == validators.date(task['start']))
            if 'end' in task:
                assert (result.end == validators.datetime(task['end']) or
                        result.end == validators.date(task['end']))
            if 'dependencies' in task:
                assert len(result.dependency) == len(task['dependencies'])
    else:
        with pytest.raises(error):
            result = cls2.from_monday(**kwargs)