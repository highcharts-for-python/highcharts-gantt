"""Tests for ``highcharts.no_data``."""

import os
import pytest

from json.decoder import JSONDecodeError

from highcharts_gantt.chart import Chart as cls
from highcharts_gantt import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal, Class_from_js_literal_with_expected

from dotenv import load_dotenv

load_dotenv()


STANDARD_PARAMS = [
    ({}, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('input_filename, expected_filename, as_file, error', [
    ('chart_obj/01-input.js',
     'chart_obj/01-expected.js',
     False,
     None),
    ('chart_obj/01-input.js',
     'chart_obj/01-expected.js',
     False,
     None),
])
def test_from_js_literal(input_files, input_filename, expected_filename, as_file, error):
    Class_from_js_literal_with_expected(cls,
                                        input_files,
                                        input_filename,
                                        expected_filename,
                                        as_file,
                                        error)


def callback_function(connection_target, task):
    from highcharts_gantt.options.series.data.connect import DataConnection

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
def test_from_asana(kwargs, expected_data_points, error):
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
        assert result.is_gantt_chart is True
        assert result.options is not None
        assert result.options.series is not None
        assert len(result.options.series) == 1
        assert len(result.options.series[0].data) == expected_data_points
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
def test_from_monday(kwargs, expected_data_points, error):
    board_id = os.getenv('MONDAY_BOARD_ID', None)

    kwargs['board_id'] = board_id

    if not error:
        personal_access_token = os.getenv('MONDAY_API_TOKEN', None)

        kwargs['api_token'] = personal_access_token

        result = cls.from_monday(**kwargs)
        assert result is not None
        assert isinstance(result, cls) is True
        assert result.is_gantt_chart is True
        assert result.options is not None
        assert result.options.series is not None
        assert len(result.options.series) == 1
        assert len(result.options.series[0].data) == expected_data_points
    elif error == errors.MondayAuthenticationError:
        kwargs['api_token'] = 'invalid-token-goes-here'

        with pytest.raises(error):
            result = cls.from_monday(**kwargs)
    else:
        with pytest.raises(error):
            result = cls.from_monday(**kwargs)
            

@pytest.mark.parametrize('kwargs, expected_data_points, error', [
    ({}, 6, None),

    # Errors
    ({}, 0, (errors.JIRAAuthenticationError, errors.JIRAProjectNotFoundError)),
])
def test_from_jira(kwargs, expected_data_points, error):
    kwargs['project_key'] = os.getenv('JIRA_PROJECT_ID')

    if not error:
        result = cls.from_jira(**kwargs)
        assert result is not None
        assert isinstance(result, cls) is True
        assert result.is_gantt_chart is True
        assert result.options is not None
        assert result.options.series is not None
        assert len(result.options.series) == 1
        assert len(result.options.series[0].data) == expected_data_points
    elif error == (errors.JIRAAuthenticationError, errors.JIRAProjectNotFoundError):
        kwargs['username'] = 'invalid-username'
        kwargs['password_or_token'] = 'invalid-token'
        
        with pytest.raises(error):
            result = cls.from_jira(**kwargs)
    else:
        with pytest.raises(error):
            result = cls.from_jira(**kwargs)