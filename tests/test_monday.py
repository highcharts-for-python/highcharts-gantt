"""Tests for ``highcharts.monday``."""

import os
import pytest

from json.decoder import JSONDecodeError

from highcharts_gantt import errors, monday
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal, Class_from_js_literal_with_expected

from dotenv import load_dotenv
from validator_collection import validators

load_dotenv()

api_token = os.getenv('MONDAY_API_TOKEN', None)

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
    import monday as monday_api
    HAS_MONDAY = True
except ImportError:
    HAS_MONDAY = False


@pytest.mark.parametrize('board_id, expected_length, error', [
    (None, 7, None),
    (None, 1, errors.MondayBoardNotFoundError),
    (None, 1, errors.MondayAuthenticationError),
])
def test_get_column_definitions(board_id, expected_length, error):
    client = monday_api.MondayClient(api_token)
    if not board_id:
        board_id = validators.integer(os.getenv('MONDAY_BOARD_ID', None))

    if not error:
        result = monday.get_column_definitions(client, board_id)
        assert result is not None
        assert isinstance(result, dict)
        assert len(result) == expected_length
    elif error == errors.MondayBoardNotFoundError:
        board_id = 12345
        with pytest.raises(error):
            result = monday.get_column_definitions(client, board_id)
    elif error == errors.MondayAuthenticationError:
        client = monday_api.MondayClient('invalid-api-token')
        with pytest.raises(error):
            result = monday.get_column_definitions(client, board_id)
    else:
        with pytest.raises(error):
            result = monday.get_column_definitions(client, board_id)
            

@pytest.mark.parametrize('board_id, expected_tasks, expected_columns, log_tasks, error', [
    (None, 7, 8, False, None),

    (None, 1, 1, False, errors.MondayAuthenticationError),
    (None, 1, 1, False, errors.MondayBoardNotFoundError),
])
def test_get_tasks(board_id, expected_tasks, expected_columns, log_tasks, error):
    if not board_id:
        board_id = validators.integer(os.getenv('MONDAY_BOARD_ID', None))
    
    if not error:
        result = monday.get_tasks(board_id, 
                                  api_token = api_token,
                                  log_tasks = log_tasks)
        assert result is not None
        assert isinstance(result, dict) is True
        print(result)
        assert len(result) == expected_tasks
        max_columns = 0
        for key in result:
            task = result[key]
            assert task.get('name', None) is not None
            assert task.get('id', None) is not None
            assert task.get('id', None) == key
            
            if max_columns < len(task) - 2:
                max_columns = len(task) - 2
            
        assert max_columns == expected_columns
    elif error == errors.MondayAuthenticationError:
        with pytest.raises(errors.MondayAuthenticationError):
            result = monday.get_tasks(board_id,
                                      api_token = 'invalid-api-token',
                                      log_tasks = log_tasks)
    elif error == errors.MondayBoardNotFoundError:
        with pytest.raises(errors.MondayBoardNotFoundError):
            result = monday.get_tasks(board_id = 12345,
                                      api_token = api_token,
                                      log_tasks = log_tasks)
    else:
        with pytest.raises(error):
            result = monday.get_tasks(board_id, api_token, log_tasks)