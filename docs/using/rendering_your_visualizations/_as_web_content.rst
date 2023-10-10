.. tabs::

  .. tab:: as a Highcharts Gantt Chart

    .. code-block:: python

      from highcharts_gantt.chart import Chart
      from highcharts_gantt.options.series.gantt import GanttSeries

      my_chart = Chart(container = 'target_div',
                       options = {
                           'series': [
                               GanttSeries(data = [
                                   ...
                               ])
                           ]
                       },
                       variable_name = 'myChart',
                       is_gantt_chart = True)

      as_js_literal = my_chart.to_js_literal()

      # This will produce a string equivalent to:
      #
      # document.addEventListener('DOMContentLoaded', function() {
      #   const myChart = Highcharts.ganttChart('target_div', {
      #      series: {
      #          type: 'gantt',
      #          data: [
      #            ...
      #          ]
      #      }
      #   });
      # });

  .. tab:: as a Highcharts JS Chart

    .. code-block:: python

      from highcharts_gantt.chart import Chart
      from highcharts_gantt.options.series.area import LineSeries

      my_chart = Chart(data = [0, 5, 3, 5], series_type = 'line')

      as_js_literal = my_chart.to_js_literal()

      # This will produce a string equivalent to:
      #
      # document.addEventListener('DOMContentLoaded', function() {
      #   const myChart = Highcharts.chart('target_div', {
      #      series: {
      #          type: 'line',
      #          data: [0, 5, 3, 5]
      #      }
      #   });
      # });
