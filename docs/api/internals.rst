#################################
Library Internals
#################################

.. contents:: Section Contents
  :local:
  :depth: 3
  :backlinks: entry

--------------

.. module:: highcharts_gantt.metaclasses

******************************************************************************
module: :mod:`.metaclasses <highcharts_gantt.metaclasses>`
******************************************************************************

The :mod:`.metaclasses <highcharts_gantt.metaclasses>` module contains - as one might
expect - :term:`metaclasses <metaclass>` that are used to ensure a consistent interface
throughout the **Highcharts Gantt for Python** library.


class: :class:`HighchartsMeta <highcharts_gantt.metaclasses.HighchartsMeta>`
===================================================================================

.. autoclass:: HighchartsMeta
  :members:
  :inherited-members:
  :private-members:

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsMeta
      :parts: -1

  |

class: :class:`JavaScriptDict <highcharts_gantt.metaclasses.JavaScriptDict>`
====================================================================================

.. autoclass:: JavaScriptDict
  :members:
  :inherited-members:
  :private-members:

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: JavaScriptDict
      :parts: -1

  |

----------------------

.. module:: highcharts_gantt.decorators

******************************************************************************
module: :mod:`.decorators <highcharts_gantt.decorators>`
******************************************************************************

The :mod:`.decorators <highcharts_gantt.decorators>` module contains decorators and
decorator-assisting functions used throughout the **Highcharts Gantt for Python** library.

decorator: :deco:`@class_sensitive <highcharts_gantt.decorators.class_sensitive>`
=======================================================================================

.. autodecorator:: class_sensitive

function: :func:`validate_types() <highcharts_gantt.decorators.validate_types>`
===================================================================================

.. autofunction:: validate_types

----------------------------------

.. module:: highcharts_gantt.js_literal_functions

******************************************************************************************
module:: :mod:`.js_literal_functions <highcharts_gantt.js_literal_functions>`
******************************************************************************************

The :mod:`.js_literal_functions <highcharts_gantt.js_literal_functions>` module contains
functions that are used to parse, process, de-serialize, and serialize JavaScript literal
notation.

function: :func:`serialize_to_js_literal() <highcharts_gantt.js_literal_functions.serialize_to_js_literal>`
===================================================================================================================================

.. autofunction:: serialize_to_js_literal

function: :func:`attempt_variable_declaration() <highcharts_gantt.js_literal_functions.attempt_variable_declaration>`
===================================================================================================================================

.. autofunction:: attempt_variable_declaration

function: :func:`is_js_function_or_class() <highcharts_gantt.js_literal_functions.is_js_function_or_class>`
===================================================================================================================================

.. autofunction:: is_js_function_or_class

function: :func:`get_js_literal() <highcharts_gantt.js_literal_functions.get_js_literal>`
===================================================================================================================================

.. autofunction:: get_js_literal

function: :func:`assemble_js_literal() <highcharts_gantt.js_literal_functions.assemble_js_literal>`
===================================================================================================================================

.. autofunction:: assemble_js_literal

function: :func:`convert_js_literal_to_python() <highcharts_gantt.js_literal_functions.convert_js_literal_to_python>`
===================================================================================================================================

.. autofunction:: convert_js_literal_to_python

function: :func:`convert_js_property_to_python() <highcharts_gantt.js_literal_functions.convert_js_property_to_python>`
===================================================================================================================================

.. autofunction:: convert_js_property_to_python

function: :func:`convert_js_to_python() <highcharts_gantt.js_literal_functions.convert_js_to_python>`
===================================================================================================================================

.. autofunction:: convert_js_to_python

function: :func:`get_key_value_pairs() <highcharts_gantt.js_literal_functions.get_key_value_pairs>`
===================================================================================================================================

.. autofunction:: get_key_value_pairs

-------------------------

.. module:: highcharts_gantt.utility_functions

********************************************************************
:mod:`.utility_functions <highcharts_gantt.utility_functions>`
********************************************************************

The :mod:`.utility_functions <highcharts_gantt.utility_functions>` module contains a
small number of functions which serve as utilities across the
**Highcharts Gantt for Python** library. Think of it as a function "catch all" module.

function:: :func:`mro_to_dict() <highcharts_gantt.utility_functions.mro_to_dict>`
=====================================================================================================

.. autofunction:: mro_to_dict

function:: :func:`get_remaining_mro() <highcharts_gantt.utility_functions.get_remaining_mro>`
=====================================================================================================

.. autofunction:: get_remaining_mro

function:: :func:`mro__to_untrimmed_dict() <highcharts_gantt.utility_functions.mro__to_untrimmed_dict>`
==============================================================================================================

.. autofunction:: mro__to_untrimmed_dict

function:: :func:`validate_color() <highcharts_gantt.utility_functions.validate_color>`
=====================================================================================================

.. autofunction:: validate_color

function:: :func:`to_camelCase() <highcharts_gantt.utility_functions.to_camelCase>`
=====================================================================================================

.. autofunction:: to_camelCase

function:: :func:`parse_csv() <highcharts_gantt.utility_functions.parse_csv>`
=====================================================================================================

.. autofunction:: parse_csv

function:: :func:`parse_jira_issue() <highcharts_gantt.utility_functions.parse_jira_issue>`
=====================================================================================================

.. autofunction:: parse_jira_issue

----------------------------------

.. module:: highcharts_gantt.monday

******************************************************************************************
module:: :mod:`.monday <highcharts_gantt.monday>`
******************************************************************************************

The :mod:`.monday <highcharts_gantt.monday>` module contains
functions that are used to retrieve, parse, process, and de-serialize task items from the Monday.com API.

function: :func:`get_tasks() <highcharts_gantt.monday.get_tasks>`
========================================================================================================================

.. autofunction:: get_tasks

function: :func:`get_column_definitions() <highcharts_gantt.monday.get_column_definitions>`
========================================================================================================================

.. autofunction:: get_column_definitions

function: :func:`convert_item_to_task() <highcharts_gantt.monday.convert_item_to_task>`
========================================================================================================================

.. autofunction:: convert_item_to_task

function: :func:`format_column() <highcharts_gantt.monday.format_column>`
========================================================================================================================

.. autofunction:: format_column

function: :func:`get_column_title() <highcharts_gantt.monday.get_column_title>`
========================================================================================================================

.. autofunction:: get_column_title

function: :func:`get_column_type() <highcharts_gantt.monday.get_column_type>`
========================================================================================================================

.. autofunction:: get_column_type

function: :func:`elevate_subtasks() <highcharts_gantt.monday.elevate_subtasks>`
========================================================================================================================

.. autofunction:: elevate_subtasks

function: :func:`flatten_columns() <highcharts_gantt.monday.flatten_columns>`
========================================================================================================================

.. autofunction:: flatten_columns
