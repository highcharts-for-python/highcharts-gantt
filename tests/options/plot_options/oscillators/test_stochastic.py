"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_gantt.options.plot_options.oscillators.stochastic import StochasticOptions as cls
from highcharts_gantt.options.plot_options.oscillators.stochastic import SlowStochasticOptions as cls2

from highcharts_gantt import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_StochasticOptions__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_StochasticOptions__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_StochasticOptions_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_StochasticOptions_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('plot_options/oscillators/stochastic/01.js', False, None),
    ('plot_options/oscillators/stochastic/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('plot_options/oscillators/stochastic/01.js', True, None),
    ('plot_options/oscillators/stochastic/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_StochasticOptions_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)


###### NEXT CLASS

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_SlowStochasticOptions__init__(kwargs, error):
    Class__init__(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_SlowStochasticOptions__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_SlowStochasticOptions_from_dict(kwargs, error):
    Class_from_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_SlowStochasticOptions_to_dict(kwargs, error):
    Class_to_dict(cls2, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('plot_options/oscillators/stochastic/02.js', False, None),
    ('plot_options/oscillators/stochastic/error-02.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('plot_options/oscillators/stochastic/02.js', True, None),
    ('plot_options/oscillators/stochastic/error-02.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_SlowStochasticOptions_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls2, input_files, filename, as_file, error)
