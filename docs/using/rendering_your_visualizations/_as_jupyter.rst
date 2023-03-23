.. code-block:: python

  from highcharts_gantt.chart import Chart
  from highcharts_gantt.options.series.gantt import GanttSeries
  from highcharts_gantt.global_options.shared_options import SharedGanttOptions

  my_chart = Chart(container = 'target_div',
                   options = {
                       'series': [
                           GanttSeries(data = [ ... ])
                       ]
                   },
                   variable_name = 'myChart',
                   is_gantt_chart = True)

  # Now this will render the contents of "my_chart" in your Jupyter Notebook
  my_chart.display()

  # You can also supply shared options to display to make sure that they are applied:
  my_shared_options = SharedGanttOptions()

  # Now this will render the contents of "my_chart" in your Jupyter Notebook, but applying
  # your shared options
  my_chart.display(global_options = my_shared_options)

.. collapse:: Method Signature

  .. method:: display(self, global_options = None)
    :noindex:

    Display the chart in `Jupyter Labs <https://jupyter.org/>`__ or
    `Jupyter Notebooks <https://jupyter.org/>`__.

    :param global_options: The :term:`shared options` to use when rendering the chart.
      Defaults to :obj:`None <python:None>`
    :type global_options: :class:`SharedOptions <highcharts_gantt.global_options.shared_options.SharedOptions>`
      or :obj:`None <python:None>`

    :raises HighchartsDependencyError: if
      `ipython <https://ipython.readthedocs.io/en/stable/>`__ is not available in the
      runtime environment
