  .. note::

    ``.add_series()`` is supported by the
    :class:`Chart <highcharts_gantt.chart.Chart>`,
    :class:`HighchartsGanttOptions <highcharts_gantt.options.HighchartsGanttOptions>`, and
    :class:`HighchartsStockOptions <highcharts_gantt.options.HighchartsStockOptions>`
    classes

.. code-block:: python

  my_chart = Chart()

  my_series = LineSeries()
  my_chart.add_series(my_series)

.. collapse:: Method Signature

  .. method:: .add_series(self, *series)
    :noindex:

    Adds ``series`` to the
    :meth:`Chart.options.series <highcharts_gantt.options.HighchartsGanttOptions.series>`
    property.

    :param series: One or more :term:`series` instances (descended from
      :class:`SeriesBase <highcharts_gantt.options.series.base.SeriesBase>`) or an
      instance (e.g. :class:`dict <python:dict>`, :class:`str <python:str>`, etc.)
      coercable to one
    :type series: :class:`SeriesBase <highcharts_gantt.options.series.base.SeriesBase>`
      or coercable
