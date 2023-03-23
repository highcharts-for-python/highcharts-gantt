################################################################
:mod:`.annotations <highcharts_gantt.options.annotations>`
################################################################

.. contents:: Module Contents
  :local:
  :depth: 3
  :backlinks: entry

.. toctree::
  :titlesonly:

  animation
  control_point_options
  events
  label_options
  points
  shape_options
  stock_tools/index

--------------

.. module:: highcharts_gantt.options.annotations

****************************************************************************************
class: :class:`Annotation <highcharts_gantt.options.annotations.Annotation>`
****************************************************************************************

.. autoclass:: Annotation
  :members:
  :inherited-members:

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: Annotation
      :top-classes: highcharts_gantt.metaclasses.HighchartsMeta, highcharts_core.metaclasses.HighchartsMeta
      :parts: -1

  |

-----------------------

***************************
Sub-components
***************************

.. list-table::
  :widths: 60 40
  :header-rows: 1

  * - Module
    - Classes / Functions
  * - :mod:`.options.annotations <highcharts_gantt.options.annotations>`
    - :class:`Annotation <highcharts_gantt.options.annotations.Annotation>`
  * - :mod:`.options.annotations.animation <highcharts_gantt.options.annotations.animation>`
    - :class:`AnnotationAnimation <highcharts_gantt.options.annotations.animation.AnnotationAnimation>`
  * - :mod:`.options.annotations.control_point_options <highcharts_gantt.options.annotations.control_point_options>`
    - :class:`AnnotationControlPointOption <highcharts_gantt.options.annotations.control_point_options.AnnotationControlPointOption>`
  * - :mod:`.options.annotations.events <highcharts_gantt.options.annotations.events>`
    - :class:`AnnotationEvent <highcharts_gantt.options.annotations.events.AnnotationEvent>`
  * - :mod:`.options.annotations.label_options <highcharts_gantt.options.annotations.label_options>`
    - :class:`AnnotationLabel <highcharts_gantt.options.annotations.label_options.AnnotationLabel>`
      :class:`AnnotationLabelOptionAccessibility <highcharts_gantt.options.annotations.label_options.AnnotationLabelOptionAccessibility>`
      :class:`LabelOptions <highcharts_gantt.options.annotations.label_options.LabelOptions>`
  * - :mod:`.options.annotations.options.annotations.points <highcharts_gantt.options.annotations.points>`
    - :class:`AnnotationPoint <highcharts_gantt.options.annotations.points.AnnotationPoint>`
  * - :mod:`.options.annotations.shape_options <highcharts_gantt.options.annotations.shape_options>`
    - :class:`AnnotationShape <highcharts_gantt.options.annotations.shape_options.AnnotationShape>`
      :class:`ShapeOptions <highcharts_gantt.options.annotations.shape_options.ShapeOptions>`
  * - :mod:`.options.annotations.stock_tools <highcharts_gantt.options.annotations.stock_tools>`
    - :class:`CrookedLineAnnotation <highcharts_gantt.options.annotations.stock_tools.CrookedLineAnnotation>`
      :class:`ElliottWaveAnnotation <highcharts_gantt.options.annotations.stock_tools.ElliottWaveAnnotation>`
      :class:`FibonacciAnnotation <highcharts_gantt.options.annotations.stock_tools.FibonacciAnnotation>`
      :class:`FibonacciTimeZonesAnnotation <highcharts_gantt.options.annotations.stock_tools.FibonacciTimeZonesAnnotation>`
      :class:`InfinityLineAnnotation <highcharts_gantt.options.annotations.stock_tools.InfinityLineAnnotation>`
      :class:`MeasureAnnotation <highcharts_gantt.options.annotations.stock_tools.MeasureAnnotation>`
      :class:`PitchforkAnnotation <highcharts_gantt.options.annotations.stock_tools.PitchforkAnnotation>`
      :class:`TimeCyclesAnnotation <highcharts_gantt.options.annotations.stock_tools.TimeCyclesAnnotation>`
      :class:`TunnelAnnotation <highcharts_gantt.options.annotations.stock_tools.TunnelAnnotation>`
      :class:`VerticalLineAnnotation <highcharts_gantt.options.annotations.stock_tools.VerticalLineAnnotation>`
  * - :mod:`.options.annotations.stock_tools.type_options <highcharts_gantt.options.annotations.stock_tools.type_options>`
    -
  * - :mod:`.options.annotations.stock_tools.type_options.crooked_line <highcharts_gantt.options.annotations.stock_tools.type_options.crooked_line>`
    - :class:`CrookedLineTypeOptions <highcharts_gantt.options.annotations.stock_tools.type_options.crooked_line.CrookedLineTypeOptions>`
      :class:`InfinityLineTypeOptions <highcharts_gantt.options.annotations.stock_tools.type_options.crooked_line.InfinityLineTypeOptions>`
  * - :mod:`.options.annotations.stock_tools.type_options.elliot_wave <highcharts_gantt.options.annotations.stock_tools.type_options.elliott_wave>`
    - :class:`ElliottWaveTypeOptions <highcharts_gantt.options.annotations.stock_tools.type_options.elliott_wave.ElliottWaveTypeOptions>`
  * - :mod:`.options.annotations.stock_tools.type_options.fibonacci <highcharts_gantt.options.annotations.stock_tools.type_options.fibonacci>`
    - :class:`FibonacciTypeOptions <highcharts_gantt.options.annotations.stock_tools.type_options.fibonacci.FibonacciTypeOptions>`
      :class:`FibonacciTimeZonesTypeOptions <highcharts_gantt.options.annotations.stock_tools.type_options.fibonacci.FibonacciTimeZonesTypeOptions>`
  * - :mod:`.options.annotations.stock_tools.type_options.line <highcharts_gantt.options.annotations.stock_tools.type_options.line>`
    - :class:`LineFillOnly <highcharts_gantt.options.annotations.stock_tools.type_options.line.LineFillOnly>`
      :class:`LineStrokeWidth <highcharts_gantt.options.annotations.stock_tools.type_options.line.LineStrokeWidth>`
      :class:`LineStrokeWidthStroke <highcharts_gantt.options.annotations.stock_tools.type_options.line.LineStrokeWidthStroke>`
  * - :mod:`.options.annotations.stock_tools.type_options.measure <highcharts_gantt.options.annotations.stock_tools.type_options.measure>`
    - :class:`MeasureTypeOptions <highcharts_gantt.options.annotations.stock_tools.type_options.measure.MeasureTypeOptions>`
      :class:`MeasureLabelOptions <highcharts_gantt.options.annotations.stock_tools.type_options.measure.MeasureLabelOptions>`
      :class:`MeasureLabelStyle <highcharts_gantt.options.annotations.stock_tools.type_options.measure.MeasureLabelStyle>`
  * - :mod:`.options.annotations.stock_tools.type_options.pitchfork <highcharts_gantt.options.annotations.stock_tools.type_options.pitchfork>`
    - :class:`PitchforkTypeOptions <highcharts_gantt.options.annotations.stock_tools.type_options.pitchfork.PitchforkTypeOptions>`
  * - :mod:`.options.annotations.stock_tools.type_options.points <highcharts_gantt.options.annotations.stock_tools.type_options.points>`
    - :class:`StockToolsPoint <highcharts_gantt.options.annotations.stock_tools.type_options.points.StockToolsPoint>`
      :class:`LabeledStockToolsPoint <highcharts_gantt.options.annotations.stock_tools.type_options.points.LabeledStockToolsPoint>`
      :class:`StockToolsXPoint <highcharts_gantt.options.annotations.stock_tools.type_options.points.StockToolsXPoint>`
  * - :mod:`.options.annotations.stock_tools.type_options.time_cycles <highcharts_gantt.options.annotations.stock_tools.type_options.time_cycles>`
    - :class:`TimeCyclesTypeOptions <highcharts_gantt.options.annotations.stock_tools.type_options.time_cycles.TimeCyclesTypeOptions>`
  * - :mod:`.options.annotations.stock_tools.type_options.tunnel <highcharts_gantt.options.annotations.stock_tools.type_options.tunnel>`
    - :class:`TunnelTypeOptions <highcharts_gantt.options.annotations.stock_tools.type_options.tunnel.TunnelTypeOptions>`
  * - :mod:`.options.annotations.stock_tools.type_options.vertical_line <highcharts_gantt.options.annotations.stock_tools.type_options.vertical_line>`
    - :class:`VerticalLineTypeOptions <highcharts_gantt.options.annotations.stock_tools.type_options.vertical_line.VerticalLineTypeOptions>`
      :class:`VerticalLineConnector <highcharts_gantt.options.annotations.stock_tools.type_options.vertical_line.VerticalLineConnector>`
