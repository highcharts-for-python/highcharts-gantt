
The structure of the **Highcharts Gantt for Python** library closely matches the structure
of the `Highcharts Gantt <https://www.highcharts.com/products/gantt/>`__ options object (see the relevant
`reference documentation <https://api.highcharts.com/gantt/>`_).

At the root of the library - importable from ``highcharts_gantt`` - you will find the
:mod:`highcharts_gantt.highcharts` module. This module is a catch-all importable module,
which allows you to easily access the most-commonly-used Highcharts Gantt for Python
classes and modules.

.. note::

  Whlie you can access all of the **Highcharts Gantt for Python** classes from
  ``highcharts_gantt.highcharts``, if you want to more precisely navigate to specific
  class definitions you can do fairly easily using the module organization and naming
  conventions used in the library.

  *This is the recommended best practice to maximize performance*.

  In the root of the ``highcharts_gantt`` library you can find universally-shared
  class definitions, like :mod:`.metaclasses <highcharts_gantt.metaclasses>` which
  contains the :class:`HighchartsMeta <highcharts_gantt.metaclasses.HighchartsMeta>`
  and :class:`JavaScriptDict <highcharts_gantt.metaclasses.JavaScriptDict>`
  definitions, or :mod:`.decorators <highcharts_gantt.decorators>` which define
  method/property decorators that are used throughout the library.

  The :mod:`.utility_classes <highcharts_gantt.utility_classes>` module contains class
  definitions for classes that are referenced or used throughout the other class
  definitions.

  And you can find the Highcharts Gantt ``options`` object and all of its
  properties defined in the :mod:`.options <highcharts_gantt.options>` module, with
  specific (complicated or extensive) sub-modules providing property-specific classes
  (e.g. the :mod:`.options.plot_options <highcharts_gantt.options.plot_options>`
  module defines all of the different configuration options for different series types,
  while the :mod:`.options.series <highcharts_gantt.options.series>` module defines all
  of the classes that represent :term:`series` of data in a given chart).