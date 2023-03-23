.. tabs::

  .. tab:: from Precise Location

    .. tip::

      **Best Practice!**

      This method of importing **Highcharts Gantt for Python** objects yields the fastest
      performance for the ``import`` statement. However, it is more verbose and requires
      you to navigate the extensive :doc:`Highcharts Gantt for Python API </api>`.

    .. code-block:: python

      # Import classes using precise module indications. For example:
      from highcharts_gantt.chart import Chart
      from highcharts_gantt.global_options.shared_options import SharedGanttOptions
      from highcharts_gantt.options import HighchartsGanttOptions
      from highcharts_gantt.options.plot_options.gantt import GanttOptions
      from highcharts_gantt.options.series.gantt import GanttSeries

  .. tab:: from ``.highcharts``

    .. caution::

      This method of importing **Highcharts Gantt for Python** classes has relatively slow
      performance because it imports hundreds of different classes from across the entire
      library. This performance impact may be acceptable to you in your use-case, but
      do use at your own risk.

    .. code-block:: python

      # Import objects from the catch-all ".highcharts" module.
      from highcharts_gantt import highcharts

      # You can now access specific classes without individual import statements.
      highcharts.Chart
      highcharts.SharedGanttOptions
      highcharts.HighchartsGanttOptions
      highcharts.GanttOptions
      highcharts.GanttSeries
