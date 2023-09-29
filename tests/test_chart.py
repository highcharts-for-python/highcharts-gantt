"""Tests for ``highcharts.no_data``."""

import os
import pytest

from json.decoder import JSONDecodeError

from highcharts_gantt.chart import Chart as cls
from highcharts_gantt import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal, Class_from_js_literal_with_expected, run_pandas_tests

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
            



@pytest.mark.parametrize('kwargs, expected_series, expected_data_points, error', [
    ({}, 0, [], None),

    ({
        'series': [
            {
                'data': [[1, 2], [3, 4]],
                'type': 'line'
            }
        ]
    }, 1, [(0, 2)], None),
    ({
        'series': {
            'data': [[1, 2], [3, 4]],
            'type': 'line'
        }
    }, 1, [(0, 2)], None),
    
    ({
        'data': [[1, 2], [3, 4]],
        'series_type': 'line'
    }, 1, [(0, 2)], None),

    ({
        'data': [[1, 2], [3, 4]],
    }, 1, [(0, 2)], errors.HighchartsValueError),

])
def test_issue90_one_shot_creation(kwargs, expected_series, expected_data_points, error):
    if not error:
        result = cls(**kwargs)
        assert result is not None
        if kwargs:
            assert getattr(result, 'options') is not None
            assert getattr(result.options, 'series') is not None
            assert len(result.options.series) == expected_series
            for item in expected_data_points:
                assert len(result.options.series[item[0]].data) == item[1]
    else:
        with pytest.raises(error):
            result = cls(**kwargs)
            

@pytest.mark.parametrize('filename, error', [
    ('test-data-files/nst-est2019-01.csv', None),
])
def test_from_pandas_in_rows(run_pandas_tests, input_files, filename, error):
    if not run_pandas_tests:
        return

    import pandas
    
    input_file = check_input_file(input_files, filename)
    df = pandas.read_csv(input_file, header = 0, thousands = ',')
    df.index = df['Geographic Area']
    df = df.drop(columns = ['Geographic Area'])
    print(df)
    
    if not error:
        result = cls.from_pandas_in_rows(df)
        assert result is not None
        assert isinstance(result, cls)
        assert len(result.options.series) == len(df)
        for series in result.options.series:
            assert series.data is not None
            assert len(series.data) == len(df.columns)
    else:
        with pytest.raises(error):
            result = cls.from_pandas_in_rows(df)


def prep_df(df):
    df.index = df['Geographic Area']
    df = df.drop(columns = ['Geographic Area'])
    
    return df


def reduce_to_two_columns(df):
    df = df[['Geographic Area', '2010']]
    
    return df


@pytest.mark.parametrize('filename, kwargs, pre_test_df_func, expected_series, expected_data_points, error', [
    # SCENARIO 0: Series in Rows
    ('test-data-files/nst-est2019-01.csv',
     {
         'series_in_rows': True
     },
     prep_df,
     57,
     10,
     None),
    
    # SCENARIO 1a: Has Property Map, Single Series
    ('test-data-files/nst-est2019-01.csv',
     {
         'property_map': {
             'name': 'Geographic Area',
         },
         'series_in_rows': False
     },
     None,
     1,
     57,
     None),

    # SCENARIO 1b: Has Property Map, Multiple Series
    ('test-data-files/nst-est2019-01.csv',
     {
         'property_map': {
             'x': ['Geographic Area', '2010']
         },
         'series_in_rows': False
     },
     None,
     2,
     57,
     None),
    
    # SCENARIO 2a: Single Property in KWARGS
    ('test-data-files/nst-est2019-01.csv',
     {
         'x': 'Geographic Area',
         'y': '2010'
     },
     None,
     1,
     57,
     None),
    
    # SCENARIO 3a: Exact Match on Column Count
    ('test-data-files/nst-est2019-01.csv',
     {},
     reduce_to_two_columns,
     1,
     57,
     None),
    
    # SCENARIO 3b: Multiple Series, Multipled Columns
    ('test-data-files/nst-est2019-01.csv',
     {},
     prep_df,
     5,
     57,
     None),

    # SCENARIO 4: Mismatched Columns
    # NOTE: On SeriesBase, this will actually return one series per column.
    # This is because SeriesBase supports 1D arrays.
    ('test-data-files/nst-est2019-01.csv',
     {},
     None,
     11,
     57,
     None),
    
])
def test_from_pandas(run_pandas_tests,
                     input_files,
                     filename,
                     kwargs,
                     pre_test_df_func,
                     expected_series,
                     expected_data_points,
                     error):
    if not run_pandas_tests:
        return

    import pandas

    input_file = check_input_file(input_files, filename)
    df = pandas.read_csv(input_file, header = 0, thousands = ',')
    if pre_test_df_func:
        df = pre_test_df_func(df)
    print(df)

    if not error:
        result = cls.from_pandas(df, **kwargs)
        assert result is not None
        assert isinstance(result, cls)
        assert len(result.options.series) == expected_series
        for series in result.options.series:
            assert series.data is not None
            assert len(series.data) == expected_data_points
    else:
        with pytest.raises(error):
            result = cls.from_pandas(df, **kwargs)
