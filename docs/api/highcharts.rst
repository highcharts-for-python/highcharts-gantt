##################################################
:mod:`.highcharts <highcharts_gantt.highcharts>`
##################################################

.. contents:: Module Contents
  :local:
  :depth: 3
  :backlinks: entry

.. module:: highcharts_gantt.highcharts

The :mod:`highcharts_gantt.highcharts` module is designed to be a catch-all module for
ease of importing. It does not actually define any functionality itself, but instead
imports classes from across the **Highcharts Gantt for Python** library to expose them
under a single import statement. This enables you to choose between whatever import-style
you prefer to apply:

  .. include:: /using/_importing.rst

.. caution::

  You should be aware that importing the :mod:`highcharts_gantt.highcharts` module takes
  a relatively long time. This is because it needs to import hundreds of other classes
  from across the entire library. Assuming you are just doing it once, this may be
  acceptable to you. However you should be aware that is much less performant than
  importing precise classes when and as-needed.
