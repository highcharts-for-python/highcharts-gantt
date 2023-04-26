##############################################################
:mod:`.options <highcharts_gantt.options>`
##############################################################

.. contents:: Module Contents
  :local:
  :depth: 3
  :backlinks: entry

.. toctree::
  :titlesonly:

  accessibility/index
  annotations/index
  axes/index
  boost
  caption
  chart/index
  credits
  data
  defs
  drilldown
  exporting/index
  legend/index
  loading
  navigation/index
  navigator
  no_data
  pane
  plot_options/index
  responsive
  series/index
  sonification/index
  stock_tools/index
  subtitle
  time
  title
  tooltips

--------------

.. module:: highcharts_gantt.options

****************************************************************************************
class: :class:`HighchartsGanttOptions <highcharts_gantt.options.HighchartsGanttOptions>`
****************************************************************************************

.. autoclass:: HighchartsGanttOptions
  :members:
  :inherited-members:

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsGanttOptions
      :top-classes: highcharts_gantt.metaclasses.HighchartsMeta, highcharts_core.metaclasses.HighchartsMeta
      :parts: -1

-----------------------

****************************************************************************************
class: :class:`HighchartsStockOptions <highcharts_gantt.options.HighchartsStockOptions>`
****************************************************************************************

.. autoclass:: HighchartsStockOptions
  :members:
  :inherited-members:

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsStockOptions
      :top-classes: highcharts_gantt.metaclasses.HighchartsMeta, highcharts_core.metaclasses.HighchartsMeta
      :parts: -1

-----------------------

****************************************************************************************
class: :class:`HighchartsOptions <highcharts_gantt.options.HighchartsOptions>`
****************************************************************************************

.. autoclass:: HighchartsOptions
  :members:
  :inherited-members:

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsOptions
      :top-classes: highcharts_gantt.metaclasses.HighchartsMeta, highcharts_core.metaclasses.HighchartsMeta
      :parts: -1

-----------------------

***************************
Sub-components
***************************

.. list-table::
  :widths: 60 40
  :header-rows: 1

  * - Module
    - Classes / Functions
  * - :mod:`.options <highcharts_gantt.options>`
    - :class:`HighchartsGanttOptions <highcharts_gantt.options.HighchartsGanttOptions>`
      :class:`HighchartsStockOptions <highcharts_gantt.options.HighchartsStockOptions>`
      :class:`HighchartsOptions <highcharts_gantt.options.HighchartsOptions>`
      :class:`Options <highcharts_gantt.options.Options>`
  * - :mod:`.options.accessibility <highcharts_gantt.options.accessibility>`
    - :class:`Accessibility <highcharts_gantt.options.accessibility.Accessibility>`
      :class:`CustomAccessibilityComponents <highcharts_gantt.options.accessibility.CustomAccessibilityComponents>`
  * - :mod:`.options.accessibility.announce_new_data <highcharts_gantt.options.accessibility.announce_new_data>`
    - :class:`AnnounceNewData <highcharts_gantt.options.accessibility.announce_new_data.AnnounceNewData>`
  * - :mod:`.options.accessibility.keyboard_navigation <highcharts_gantt.options.accessibility.keyboard_navigation>`
    - :class:`KeyboardNavigation <highcharts_gantt.options.accessibility.keyboard_navigation.KeyboardNavigation>`
  * - :mod:`.options.accessibility.keyboard_navigation.focus_border <highcharts_gantt.options.accessibility.keyboard_navigation.focus_border>`
    - :class:`FocusBorder <highcharts_gantt.options.accessibility.keyboard_navigation.focus_border.FocusBorder>`
      :class:`FocusBorderStyle <highcharts_gantt.options.accessibility.keyboard_navigation.focus_border.FocusBorderStyle>`
  * - :mod:`.options.accessibility.keyboard_navigation.series_navigation <highcharts_gantt.options.accessibility.keyboard_navigation.series_navigation>`
    - :class:`SeriesNavigation <highcharts_gantt.options.accessibility.keyboard_navigation.series_navigation.SeriesNavigation>`
  * - :mod:`options.accessibility.point <highcharts_gantt.options.accessibility.point>`
    - :class:`AccessibilityPoint <highcharts_gantt.options.accessibility.point.AccessibilityPoint>`
  * - :mod:`options.accessibility.screen_reader_section <highcharts_gantt.options.accessibility.screen_reader_section>`
    - :class:`ScreenReaderSection <highcharts_gantt.options.accessibility.screen_reader_section.ScreenReaderSection>`
  * - :mod:`options.accessibility.series <highcharts_gantt.options.accessibility.series>`
    - :class:`SeriesAccessibility <highcharts_gantt.options.accessibility.series.SeriesAccessibility>`
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
  * - :mod:`.options.axes <highcharts_gantt.options.axes>`
    -
  * - :mod:`.options.axes.accessibility <highcharts_gantt.options.axes.accessibility>`
    - :class:`AxisAccessibility <highcharts_gantt.options.axes.accessibility.AxisAccessibility>`
  * - :mod:`.options.axes.breaks <highcharts_gantt.options.axes.breaks>`
    - :class:`AxisBreak <highcharts_gantt.options.axes.breaks.AxisBreak>`
  * - :mod:`.options.axes.color_axis <highcharts_gantt.options.axes.color_axis>`
    - :class:`ColorAxis <highcharts_gantt.options.axes.color_axis.ColorAxis>`
  * - :mod:`.options.axes.crosshair <highcharts_gantt.options.axes.crosshair>`
    - :class:`CrosshairOptions <highcharts_gantt.options.axes.crosshair.CrosshairOptions>`
  * - :mod:`.options.axes.data_classes <highcharts_gantt.options.axes.data_classes>`
    - :class:`DataClass <highcharts_gantt.options.axes.data_classes.DataClass>`
  * - :mod:`.options.axes.generic <highcharts_gantt.options.axes.generic>`
    - :class:`GenericAxis <highcharts_gantt.options.axes.generic.GenericAxis>`
  * - :mod:`.options.axes.labels <highcharts_gantt.options.axes.labels>`
    - :class:`AxisLabelOptions <highcharts_gantt.options.axes.labels.AxisLabelOptions>`
      :class:`PlotBandLabel <highcharts_gantt.options.axes.labels.PlotBandLabel>`
      :class:`PlotLineLabel <highcharts_gantt.options.axes.labels.PlotLineLabel>`
  * - :mod:`.options.axes.markers <highcharts_gantt.options.axes.markers>`
    - :class:`AxisMarker <highcharts_gantt.options.axes.markers.AxisMarker>`
  * - :mod:`.options.axes.numeric <highcharts_gantt.options.axes.numeric>`
    - :class:`NumericAxis <highcharts_gantt.options.axes.numeric.NumericAxis>`
  * - :mod:`.options.axes.parallel_axes <highcharts_gantt.options.axes.parallel_axes>`
    - :class:`ParallelAxesOptions <highcharts_gantt.options.axes.parallel_axes.ParallelAxesOptions>`
  * - :mod:`.options.axes.plot_bands <highcharts_gantt.options.axes.plot_bands>`
    - :class:`PlotBand <highcharts_gantt.options.axes.plot_bands.PlotBand>`
      :class:`PlotLine <highcharts_gantt.options.axes.plot_bands.PlotLine>`
  * - :mod:`.options.axes.resize <highcharts_gantt.options.axes.resize>`
    - :class:`ResizeOptions <highcharts_gantt.options.axes.resize.ResizeOptions>`
      :class:`ControlledAxis <highcharts_gantt.options.axes.resize.ControlledAxis>`
  * - :mod:`.options.axes.title <highcharts_gantt.options.axes.title>`
    - :class:`AxisTitle <highcharts_gantt.options.axes.title.AxisTitle>`
  * - :mod:`.options.axes.x_axis <highcharts_gantt.options.axes.x_axis>`
    - :class:`XAxis <highcharts_gantt.options.axes.x_axis.XAxis>`
  * - :mod:`.options.axes.y_axis <highcharts_gantt.options.axes.y_axis>`
    - :class:`YAxis <highcharts_gantt.options.axes.y_axis.YAxis>`
  * - :mod:`.options.axes.z_axis <highcharts_gantt.options.axes.z_axis>`
    - :class:`ZAxis <highcharts_gantt.options.axes.z_axis.ZAxis>`
  * - :mod:`.options.boost <highcharts_gantt.options.boost>`
    - :class:`Boost <highcharts_gantt.options.boost.Boost>`
      :class:`BoostDebug <highcharts_gantt.options.boost.BoostDebug>`
  * - :mod:`.options.caption <highcharts_gantt.options.caption>`
    - :class:`Caption <highcharts_gantt.options.caption.Caption>`
  * - :mod:`.options.chart <highcharts_gantt.options.chart>`
    - :class:`ChartOptions <highcharts_gantt.options.chart.ChartOptions>`
      :class:`PanningOptions <highcharts_gantt.options.chart.PanningOptions>`
  * - :mod:`.chart.options_3d <highcharts_gantt.options.chart.options_3d>`
    - :class:`Options3D <highcharts_gantt.options.chart.options_3d.Options3D>`
      :class:`Frame <highcharts_gantt.options.chart.options_3d.Frame>`
      :class:`PanelOptions <highcharts_gantt.options.chart.options_3d.PanelOptions>`
  * - :mod:`.options.chart.reset_zoom_button <highcharts_gantt.options.chart.reset_zoom_button>`
    - :class:`ResetZoomButtonOptions <highcharts_gantt.options.chart.reset_zoom_button.ResetZoomButtonOptions>`
  * - :mod:`.chart.scrollable_plot_area <highcharts_gantt.options.chart.scrollable_plot_area>`
    - :class:`ScrollablePlotArea <highcharts_gantt.options.chart.scrollable_plot_area.ScrollablePlotArea>`
  * - :mod:`.options.chart.zooming <highcharts_gantt.options.chart.zooming>`
    - :class:`ZoomingOptions <highcharts_gantt.options.chart.zooming.ZoomingOptions>`
  * - :mod:`.options.credits <highcharts_gantt.options.credits>`
    - :class:`Credits <highcharts_gantt.options.credits.Credits>`
      :class:`CreditStyleOptions <highcharts_gantt.options.credits.CreditStyleOptions>`
  * - :mod:`.options.data <highcharts_gantt.options.data>`
    - :class:`Data <highcharts_gantt.options.data.Data>`
  * - :mod:`.options.defs <highcharts_gantt.options.defs>`
    - :class:`MarkerDefinition <highcharts_gantt.options.defs.MarkerDefinition>`
      :class:`MarkerASTNode <highcharts_gantt.options.defs.MarkerASTNode>`
      :class:`MarkerAttributeObject <highcharts_gantt.options.defs.MarkerAttributeObject>`
  * - :mod:`.options.drilldown <highcharts_gantt.options.drilldown>`
    - :class:`Drilldown <highcharts_gantt.options.drilldown.Drilldown>`
  * - :mod:`.options.exporting <highcharts_gantt.options.exporting>`
    - :class:`Exporting <highcharts_gantt.options.exporting.Exporting>`
      :class:`ExportingAccessibilityOptions <highcharts_gantt.options.exporting.ExportingAccessibilityOptions>`
  * - :mod:`.options.exporting.csv <highcharts_gantt.options.exporting.csv>`
    - :class:`ExportingCSV <highcharts_gantt.options.exporting.csv.ExportingCSV>`
      :class:`CSVAnnotationOptions <highcharts_gantt.options.exporting.csv.CSVAnnotationOptions>`
  * - :mod:`.options.exporting.exporting.pdf_font <highcharts_gantt.options.exporting.pdf_font>`
    - :class:`PDFFontOptions <highcharts_gantt.options.exporting.pdf_font.PDFFontOptions>`
  * - :mod:`.options.legend <highcharts_gantt.options.legend>`
    - :class:`Legend <highcharts_gantt.options.legend.Legend>`
  * - :mod:`.options.legend.accessibility <highcharts_gantt.options.legend.accessibility>`
    - :class:`LegendAccessibilityOptions <highcharts_gantt.options.legend.accessibility.LegendAccessibilityOptions>`
      :class:`LegendKeyboardNavigation <highcharts_gantt.options.legend.accessibility.LegendKeyboardNavigation>`
  * - :mod:`.options.legend.bubble_legend <highcharts_gantt.options.legend.bubble_legend>`
    - :class:`BubbleLegend <highcharts_gantt.options.legend.bubble_legend.BubbleLegend>`
      :class:`BubbleLegendRange <highcharts_gantt.options.legend.bubble_legend.BubbleLegendRange>`
      :class:`BubbleLegendLabelOptions <highcharts_gantt.options.legend.bubble_legend.BubbleLegendLabelOptions>`
  * - :mod:`.options.legend.navigation <highcharts_gantt.options.legend.navigation>`
    - :class:`LegendNavigation <highcharts_gantt.options.legend.navigation.LegendNavigation>`
  * - :mod:`.options.legend.title <highcharts_gantt.options.legend.title>`
    - :class:`LegendTitle <highcharts_gantt.options.legend.title.LegendTitle>`
  * - :mod:`.options.loading <highcharts_gantt.options.loading>`
    - :class:`Loading <highcharts_gantt.options.loading.Loading>`
  * - :mod:`.options.navigation <highcharts_gantt.options.navigation>`
    - :class:`Navigation <highcharts_gantt.options.navigation.Navigation>`
  * - :mod:`.options.navigation.bindings <highcharts_gantt.options.navigation.bindings>`
    - :class:`Bindings <highcharts_gantt.options.navigation.bindings.Bindings>`
      :class:`RectangleAnnotationBinding <highcharts_gantt.options.navigation.bindings.RectangleAnnotationBinding>`
      :class:`LabelAnnotationBinding <highcharts_gantt.options.navigation.bindings.LabelAnnotationBinding>`
      :class:`EllipseAnnotationBinding <highcharts_gantt.options.navigation.bindings.EllipseAnnotationBinding>`
      :class:`CircleAnnotationBinding <highcharts_gantt.options.navigation.bindings.CircleAnnotationBinding>`
      :class:`Binding <highcharts_gantt.options.navigation.bindings.Binding>`
  * - :mod:`.options.navigator <highcharts_gantt.options.navigator>`
    - :class:`Navigator <highcharts_gantt.options.navigator.Navigator>`
      :class:`HandleOptions <highcharts_gantt.options.navigator.HandleOptions>`
  * - :mod:`.options.no_data <highcharts_gantt.options.no_data>`
    - :class:`NoData <highcharts_gantt.options.no_data.NoData>`
  * - :mod:`.options.pane <highcharts_gantt.options.pane>`
    - :class:`Pane <highcharts_gantt.options.pane.Pane>`
      :class:`PaneBackground <highcharts_gantt.options.pane.PaneBackground>`
  * - :mod:`.options.plot_options <highcharts_gantt.options.plot_options>`
    - :class:`PlotOptions <highcharts_gantt.options.plot_options.PlotOptions>`
  * - :mod:`.options.plot_options.abands <highcharts_gantt.options.plot_options.abands>`
    - :class:`AbandsOptions <highcharts_gantt.options.plot_options.abands.AbandsOptions>`
      :class:`BBOptions <highcharts_gantt.options.plot_options.abands.BBOptions>`
      :class:`KeltnerChannelsOptions <highcharts_gantt.options.plot_options.abands.KeltnerChannelsOptions>`
      :class:`PCOptions <highcharts_gantt.options.plot_options.abands.PCOptions>`
      :class:`AbandsStyleOptions <highcharts_gantt.options.plot_options.abands.AbandsStyleOptions>`
  * - :mod:`.options.plot_options.accessibility <highcharts_gantt.options.plot_options.accessibility>`
    - :class:`TypeOptionsAccessibility <highcharts_gantt.options.plot_options.accessibility.TypeOptionsAccessibility>`
      :class:`SeriesKeyboardNavigation <highcharts_gantt.options.plot_options.accessibility.SeriesKeyboardNavigation>`
  * - :mod:`.options.plot_options.ad <highcharts_gantt.options.plot_options.ad>`
    - :class:`ADOptions <highcharts_gantt.options.plot_options.ad.ADOptions>`
      :class:`ADParameters <highcharts_gantt.options.plot_options.ad.ADParameters>`
  * - :mod:`.options.plot_options.arcdiagram <highcharts_gantt.options.plot_options.arcdiagram>`
    - :class:`ArcDiagramOptions <highcharts_gantt.options.plot_options.arcdiagram.ArcDiagramOptions>`
  * - :mod:`.options.plot_options.area <highcharts_gantt.options.plot_options.area>`
    - :class:`AreaOptions <highcharts_gantt.options.plot_options.area.AreaOptions>`
      :class:`AreaRangeOptions <highcharts_gantt.options.plot_options.area.AreaRangeOptions>`
      :class:`AreaSplineOptions <highcharts_gantt.options.plot_options.area.AreaSplineOptions>`
      :class:`AreaSplineRangeOptions <highcharts_gantt.options.plot_options.area.AreaSplineRangeOptions>`
      :class:`LineOptions <highcharts_gantt.options.plot_options.area.LineOptions>`
      :class:`StreamGraphOptions <highcharts_gantt.options.plot_options.area.StreamGraphOptions>`
  * - :mod:`.options.plot_options.aroon <highcharts_gantt.options.plot_options.aroon>`
    - :class:`AroonOptions <highcharts_gantt.options.plot_options.aroon.AroonOptions>`
      :class:`AroonLineStyleOptions <highcharts_gantt.options.plot_options.aroon.AroonLineStyleOptions>`
  * - :mod:`.options.plot_options.atr <highcharts_gantt.options.plot_options.atr>`
    - :class:`ATROptions <highcharts_gantt.options.plot_options.atr.ATROptions>`
      :class:`NATROptions <highcharts_gantt.options.plot_options.atr.NATROptions>`
  * - :mod:`.options.plot_options.averages <highcharts_gantt.options.plot_options.averages>`
    - :class:`DEMAOptions <highcharts_gantt.options.plot_options.averages.DEMAOptions>`
      :class:`EMAOptions <highcharts_gantt.options.plot_options.averages.EMAOptions>`
      :class:`SMAOptions <highcharts_gantt.options.plot_options.averages.SMAOptions>`
      :class:`TEMAOptions <highcharts_gantt.options.plot_options.averages.TEMAOptions>`
      :class:`VWAPOptions <highcharts_gantt.options.plot_options.averages.VWAPOptions>`
      :class:`WMAOptions <highcharts_gantt.options.plot_options.averages.WMAOptions>`
      :class:`VWAPParameters <highcharts_gantt.options.plot_options.averages.VWAPParameters>`
  * - :mod:`.options.plot_options.bar <highcharts_gantt.options.plot_options.bar>`
    - :class:`BarOptions <highcharts_gantt.options.plot_options.bar.BarOptions>`
      :class:`ColumnOptions <highcharts_gantt.options.plot_options.bar.ColumnOptions>`
      :class:`ColumnPyramidOptions <highcharts_gantt.options.plot_options.bar.ColumnPyramidOptions>`
      :class:`ColumnRangeOptions <highcharts_gantt.options.plot_options.bar.ColumnRangeOptions>`
      :class:`CylinderOptions <highcharts_gantt.options.plot_options.bar.CylinderOptions>`
      :class:`VariwideOptions <highcharts_gantt.options.plot_options.bar.VariwideOptions>`
      :class:`WaterfallOptions <highcharts_gantt.options.plot_options.bar.WaterfallOptions>`
      :class:`WindBarbOptions <highcharts_gantt.options.plot_options.bar.WindBarbOptions>`
      :class:`XRangeOptions <highcharts_gantt.options.plot_options.bar.XRangeOptions>`
      :class:`BaseBarOptions <highcharts_gantt.options.plot_options.bar.BaseBarOptions>`
  * - :mod:`.options.plot_options.base <highcharts_gantt.options.plot_options.base>`
    - :class:`NonIndicatorOptions <highcharts_gantt.options.plot_options.base.NonIndicatorOptions>`
      :class:`NavigatorIndicatorOptions <highcharts_gantt.options.plot_options.base.NavigatorIndicatorOptions>`
      :class:`StockBaseOptions <highcharts_gantt.options.plot_options.base.StockBaseOptions>`
  * - :mod:`.options.plot_options.bellcurve <highcharts_gantt.options.plot_options.bellcurve>`
    - :class:`BellCurveOptions <highcharts_gantt.options.plot_options.bellcurve.BellCurveOptions>`
  * - :mod:`.options.plot_options.boxplot <highcharts_gantt.options.plot_options.boxplot>`
    - :class:`BoxPlotOptions <highcharts_gantt.options.plot_options.boxplot.BoxPlotOptions>`
      :class:`ErrorBarOptions <highcharts_gantt.options.plot_options.boxplot.ErrorBarOptions>`
  * - :mod:`.options.plot_options.bubble <highcharts_gantt.options.plot_options.bubble>`
    - :class:`BubbleOptions <highcharts_gantt.options.plot_options.bubble.BubbleOptions>`
  * - :mod:`.options.plot_options.bullet <highcharts_gantt.options.plot_options.bullet>`
    - :class:`BulletOptions <highcharts_gantt.options.plot_options.bullet.BulletOptions>`
      :class:`TargetOptions <highcharts_gantt.options.plot_options.bullet.TargetOptions>`
  * - :mod:`.options.plot_options.candlestick <highcharts_gantt.options.plot_options.candlestick>`
    - :class:`CandlestickOptions <highcharts_gantt.options.plot_options.candlestick.CandlestickOptions>`
      :class:`HollowCandlestickOptions <highcharts_gantt.options.plot_options.candlestick.HollowCandlestickOptions>`
      :class:`HeikinAshiOptions <highcharts_gantt.options.plot_options.candlestick.HeikinAshiOptions>`
  * - :mod:`.options.plot_options.data_sorting <highcharts_gantt.options.plot_options.data_sorting>`
    - :class:`DataSorting <highcharts_gantt.options.plot_options.data_sorting.DataSorting>`
  * - :mod:`.options.plot_options.dependencywheel <highcharts_gantt.options.plot_options.dependencywheel>`
    - :class:`DependencyWheelOptions <highcharts_gantt.options.plot_options.dependencywheel.DependencyWheelOptions>`
  * - :mod:`.options.plot_options.disparity_index <highcharts_gantt.options.plot_options.disparity_index>`
    - :class:`DisparityIndexOptions <highcharts_gantt.options.plot_options.disparity_index.DisparityIndexOptions>`
      :class:`DisparityIndexParameters <highcharts_gantt.options.plot_options.disparity_index.DisparityIndexParameters>`
  * - :mod:`.options.plot_options.dmi <highcharts_gantt.options.plot_options.dmi>`
    - :class:`DMIOptions <highcharts_gantt.options.plot_options.dmi.DMIOptions>`
      :class:`DMIStyleOptions <highcharts_gantt.options.plot_options.dmi.DMIStyleOptions>`
  * - :mod:`.options.plot_options.drag_drop <highcharts_gantt.options.plot_options.drag_drop>`
    - :class:`DragDropOptions <highcharts_gantt.options.plot_options.drag_drop.DragDropOptions>`
      :class:`HighLowDragDropOptions <highcharts_gantt.options.plot_options.drag_drop.HighLowDragDropOptions>`
      :class:`BoxPlotDragDropOptions <highcharts_gantt.options.plot_options.drag_drop.BoxPlotDragDropOptions>`
      :class:`BulletDragDropOptions <highcharts_gantt.options.plot_options.drag_drop.BulletDragDropOptions>`
      :class:`GuideBox <highcharts_gantt.options.plot_options.drag_drop.GuideBox>`
      :class:`GuideBoxOptions <highcharts_gantt.options.plot_options.drag_drop.GuideBoxOptions>`
      :class:`DragHandle <highcharts_gantt.options.plot_options.drag_drop.DragHandle>`
  * - :mod:`.options.plot_options.dumbbell <highcharts_gantt.options.plot_options.dumbbell>`
    - :class:`DumbbellOptions <highcharts_gantt.options.plot_options.dumbbell.DumbbellOptions>`
      :class:`LollipopOptions <highcharts_gantt.options.plot_options.dumbbell.LollipopOptions>`
  * - :mod:`.options.plot_options.flags <highcharts_gantt.options.plot_options.flags>`
    - :class:`FlagsOptions <highcharts_gantt.options.plot_options.flags.FlagsOptions>`
  * - :mod:`.options.plot_options.funnel <highcharts_gantt.options.plot_options.funnel>`
    - :class:`FunnelOptions <highcharts_gantt.options.plot_options.funnel.FunnelOptions>`
      :class:`Funnel3DOptions <highcharts_gantt.options.plot_options.funnel.Funnel3DOptions>`
  * - :mod:`.options.plot_options.gantt <highcharts_gantt.options.plot_options.gantt>`
    - :class:`GanttOptions <highcharts_gantt.options.plot_options.gantt.GanttOptions>`
  * - :mod:`.options.plot_options.gauge <highcharts_gantt.options.plot_options.gauge>`
    - :class:`GaugeOptions <highcharts_gantt.options.plot_options.gauge.GaugeOptions>`
      :class:`SolidGaugeOptions <highcharts_gantt.options.plot_options.gauge.SolidGaugeOptions>`
  * - :mod:`.options.plot_options.generic <highcharts_gantt.options.plot_options.generic>`
    - :class:`GenericTypeOptions <highcharts_gantt.options.plot_options.generic.GenericTypeOptions>`
  * - :mod:`.options.plot_options.heatmap <highcharts_gantt.options.plot_options.heatmap>`
    - :class:`HeatmapOptions <highcharts_gantt.options.plot_options.heatmap.HeatmapOptions>`
      :class:`TilemapOptions <highcharts_gantt.options.plot_options.Tilemap.TilemapOptions>`
  * - :mod:`.options.plot_options.histogram <highcharts_gantt.options.plot_options.histogram>`
    - :class:`HistogramOptions <highcharts_gantt.options.plot_options.histogram.HistogramOptions>`
  * - :mod:`.options.plot_options.hlc <highcharts_gantt.options.plot_options.hlc>`
    - :class:`HLCOptions <highcharts_gantt.options.plot_options.hlc.HLCOptions>`
      :class:`OHLCOptions <highcharts_gantt.options.plot_options.hlc.OHLCOptions>`
  * - :mod:`.options.plot_options.indicators <highcharts_gantt.options.plot_options.indicators>`
    - :class:`IndicatorOptions <highcharts_gantt.options.plot_options.indicators.IndicatorOptions>`
      :class:`ComparableIndicatorOptions <highcharts_gantt.options.plot_options.indicators.ComparableIndicatorOptions>`
      :class:`ParameterBase <highcharts_gantt.options.plot_options.indicators.ParameterBase>`
  * - :mod:`.options.plot_options.item <highcharts_gantt.options.plot_options.item>`
    - :class:`ItemOptions <highcharts_gantt.options.plot_options.item.ItemOptions>`
  * - :mod:`.options.plot_options.levels <highcharts_gantt.options.plot_options.levels>`
    - :class:`LevelOptions <highcharts_gantt.options.plot_options.levels.LevelOptions>`
      :class:`SunburstLevelOptions <highcharts_gantt.options.plot_options.levels.SunburstLevelOptions>`
      :class:`TreemapLevelOptions <highcharts_gantt.options.plot_options.levels.TreemapLevelOptions>`
      :class:`LevelSize <highcharts_gantt.options.plot_options.levels.LevelSize>`
      :class:`ColorVariation <highcharts_gantt.options.plot_options.levels.ColorVariation>`
      :class:`BaseLevelOptions <highcharts_gantt.options.plot_options.levels.BaseLevelOptions>`
  * - :mod:`.options.plot_options.linear_regressions <highcharts_gantt.options.plot_options.linear_regressions>`
    - :class:`LinearRegressionOptions <highcharts_gantt.options.plot_options.linear_regressions.LinearRegressionOptions>`
      :class:`LinearRegressionAngleOptions <highcharts_gantt.options.plot_options.linear_regressions.LinearRegressionAngleOptions>`
      :class:`LinearRegressionInterceptOptions <highcharts_gantt.options.plot_options.linear_regressions.LinearRegressionInterceptOptions>`
      :class:`LinearRegressionSlopeOptions <highcharts_gantt.options.plot_options.linear_regressions.LinearRegressionSlopeOptions>`
      :class:`TrendlineOptions <highcharts_gantt.options.plot_options.linear_regressions.TrendlineOptions>`
      :class:`LinearRegressionParameters <highcharts_gantt.options.plot_options.linear_regressions.LinearRegressionParameters>`
      :class:`TrendlineParameters <highcharts_gantt.options.plot_options.linear_regressions.TrendlineParameters>`
  * - :mod:`.options.plot_options.link <highcharts_gantt.options.plot_options.link>`
    - :class:`LinkOptions <highcharts_gantt.options.plot_options.link.LinkOptions>`
  * - :mod:`.options.plot_options.momentum <highcharts_gantt.options.plot_options.momentum>`
    - :class:`MomentumOptions <highcharts_gantt.options.plot_options.momentum.MomentumOptions>`
      :class:`OBVOptions <highcharts_gantt.options.plot_options.momentum.OBVOptions>`
      :class:`OBVParameters <highcharts_gantt.options.plot_options.momentum.OBVParameters>`
      :class:`ROCOptions <highcharts_gantt.options.plot_options.momentum.ROCOptions>`
      :class:`RSIOptions <highcharts_gantt.options.plot_options.momentum.RSIOptions>`
      :class:`RSIParameters <highcharts_gantt.options.plot_options.momentum.RSIParameters>`
  * - :mod:`.options.plot_options.momentum.ikh <highcharts_gantt.options.plot_options.momentum.ikh>`
    - :class:`IKHOptions <highcharts_gantt.options.plot_options.momentum.ikh.IKHOptions>`
      :class:`IKHParameters <highcharts_gantt.options.plot_options.momentum.ikh.IKHParameters>`
      :class:`SenkouSpanOptions <highcharts_gantt.options.plot_options.momentum.ikh.SenkouSpanOptions>`
      :class:`IKHLineOptions <highcharts_gantt.options.plot_options.momentum.ikh.IKHLineOptions>`
  * - :mod:`.options.plot_options.momentum.macd <highcharts_gantt.options.plot_options.momentum.macd>`
    - :class:`MACDOptions <highcharts_gantt.options.plot_options.momentum.macd.MACDOptions>`
      :class:`MACDParameters <highcharts_gantt.options.plot_options.momentum.macd.MACDParameters>`
      :class:`MACDLineOptions <highcharts_gantt.options.plot_options.momentum.macd.MACDLineOptions>`
  * - :mod:`.options.plot_options.momentum.supertrend <highcharts_gantt.options.plot_options.momentum.supertrend>`
    - :class:`SupertrendOptions <highcharts_gantt.options.plot_options.momentum.supertrend.SupertrendOptions>`
      :class:`SupertrendParameters <highcharts_gantt.options.plot_options.momentum.supertrend.SupertrendParameters>`
      :class:`SupertrendLineOptions <highcharts_gantt.options.plot_options.momentum.supertrend.SupertrendLineOptions>`
  * - :mod:`.options.plot_options.networkgraph <highcharts_gantt.options.plot_options.networkgraph>`
    - :class:`NetworkGraphOptions <highcharts_gantt.options.plot_options.networkgraph.NetworkGraphOptions>`
      :class:`LayoutAlgorithm <highcharts_gantt.options.plot_options.networkgraph.LayoutAlgorithm>`
  * - :mod:`.options.plot_options.organization <highcharts_gantt.options.plot_options.organization>`
    - :class:`OrganizationOptions <highcharts_gantt.options.plot_options.organization.OrganizationOptions>`
  * - :mod:`.options.plot_options.oscillators <highcharts_gantt.options.plot_options.oscillators>`
    - :class:`AroonOscillatorOptions <highcharts_gantt.options.plot_options.oscillators.AroonOscillatorOptions>`
      :class:`APOOptions <highcharts_gantt.options.plot_options.oscillators.APOOptions>`
      :class:`CCIOptions <highcharts_gantt.options.plot_options.oscillators.CCIOptions>`
      :class:`ChaikinOptions <highcharts_gantt.options.plot_options.oscillators.ChaikinOptions>`
      :class:`CMOOptions <highcharts_gantt.options.plot_options.oscillators.CMOOptions>`
      :class:`DPOOptions <highcharts_gantt.options.plot_options.oscillators.DPOOptions>`
      :class:`TRIXOptions <highcharts_gantt.options.plot_options.oscillators.TRIXOptions>`
      :class:`WilliamsROptions <highcharts_gantt.options.plot_options.oscillators.WilliamsROptions>`
      :class:`WilliamsRParameters <highcharts_gantt.options.plot_options.oscillators.WilliamsRParameters>`
  * - :mod:`.options.plot_options.oscillators.ao <highcharts_gantt.options.plot_options.oscillators.ao>`
    - :class:`AOOptions <highcharts_gantt.options.plot_options.oscillators.ao.AOOptions>`
  * - :mod:`.options.plot_options.oscillators.klinger <highcharts_gantt.options.plot_options.oscillators.klinger>`
    - :class:`KlingerOptions <highcharts_gantt.options.plot_options.oscillators.klinger.KlingerOptions>`
      :class:`KlingerParameters <highcharts_gantt.options.plot_options.oscillators.klinger.KlingerParameters>`
      :class:`KlingerLineOptions <highcharts_gantt.options.plot_options.oscillators.klinger.KlingerLineOptions>`
  * - :mod:`.options.plot_options.oscillators.money_flow <highcharts_gantt.options.plot_options.oscillators.money_flow>`
    - :class:`MFIOptions <highcharts_gantt.options.plot_options.oscillators.money_flow.MFIOptions>`
      :class:`MFIParameters <highcharts_gantt.options.plot_options.oscillators.money_flow.MFIParameters>`
      :class:`CMFOptions <highcharts_gantt.options.plot_options.oscillators.money_flow.CMFOptions>`
  * - :mod:`.options.plot_options.oscillators.ppo <highcharts_gantt.options.plot_options.oscillators.ppo>`
    - :class:`PPOOptions <highcharts_gantt.options.plot_options.oscillators.ppo.PPOOptions>`
      :class:`PPOParameters <highcharts_gantt.options.plot_options.oscillators.ppo.PPOParameters>`
  * - :mod:`.options.plot_options.oscillators.stochastic <highcharts_gantt.options.plot_options.oscillators.stochastic>`
    - :class:`StochasticOptions <highcharts_gantt.options.plot_options.oscillators.stochastic.StochasticOptions>`
      :class:`StochasticParameters <highcharts_gantt.options.plot_options.oscillators.stochastic.StochasticParameters>`
      :class:`SlowStochasticOptions <highcharts_gantt.options.plot_options.oscillators.stochastic.SlowStochasticOptions>`
      :class:`SlowStochasticParameters <highcharts_gantt.options.plot_options.oscillators.stochastic.SlowStochasticParameters>`
      :class:`StochasticStyleOptions <highcharts_gantt.options.plot_options.oscillators.stochastic.StochasticStyleOptions>`
  * - :mod:`.options.plot_options.packedbubble <highcharts_gantt.options.plot_options.packedbubble>`
    - :class:`PackedBubbleOptions <highcharts_gantt.options.plot_options.packedbubble.PackedBubbleOptions>`
      :class:`ParentNodeOptions <highcharts_gantt.options.plot_options.packedbubble.ParentNodeOptions>`
  * - :mod:`.options.plot_options.pareto <highcharts_gantt.options.plot_options.pareto>`
    - :class:`ParetoOptions <highcharts_gantt.options.plot_options.pareto.ParetoOptions>`
  * - :mod:`.options.plot_options.pie <highcharts_gantt.options.plot_options.pie>`
    - :class:`PieOptions <highcharts_gantt.options.plot_options.pie.PieOptions>`
      :class:`VariablePieOptions <highcharts_gantt.options.plot_options.pie.VariablePieOptions>`
  * - :mod:`.options.plot_options.pivot_points <highcharts_gantt.options.plot_options.pivot_points>`
    - :class:`PivotPointsOptions <highcharts_gantt.options.plot_options.pivot_points.PivotPointsOptions>`
      :class:`PivotPointsParameters <highcharts_gantt.options.plot_options.pivot_points.PivotPointsParameters>`
  * - :mod:`.options.plot_options.points <highcharts_gantt.options.plot_options.points>`
    - :class:`Point <highcharts_gantt.options.plot_options.points.Point>`
      :class:`OnPointOptions <highcharts_gantt.options.plot_options.points.OnPointOptions>`
      :class:`ConnectorOptions <highcharts_gantt.options.plot_options.points.ConnectorOptions>`
  * - :mod:`.options.plot_options.polygon <highcharts_gantt.options.plot_options.polygon>`
    - :class:`PolygonOptions <highcharts_gantt.options.plot_options.polygon.PolygonOptions>`
  * - :mod:`.options.plot_options.price_envelopes <highcharts_gantt.options.plot_options.price_envelopes>`
    - :class:`PriceEnvelopesOptions <highcharts_gantt.options.plot_options.price_envelopes.PriceEnvelopesOptions>`
      :class:`PriceEnvelopesParameters <highcharts_gantt.options.plot_options.price_envelopes.PriceEnvelopesParameters>`
      :class:`PriceEnvelopesStyleOptions <highcharts_gantt.options.plot_options.price_envelopes.PriceEnvelopesStyleOptions>`
  * - :mod:`.options.plot_options.psar <highcharts_gantt.options.plot_options.psar>`
    - :class:`PSAROptions <highcharts_gantt.options.plot_options.psar.PSAROptions>`
      :class:`PSARParameters <highcharts_gantt.options.plot_options.psar.PSARParameters>`
  * - :mod:`.options.plot_options.pyramid <highcharts_gantt.options.plot_options.pyramid>`
    - :class:`PyramidOptions <highcharts_gantt.options.plot_options.pyramid.PyramidOptions>`
      :class:`Pyramid3DOptions <highcharts_gantt.options.plot_options.pyramid.Pyramid3DOptions>`
  * - :mod:`.options.plot_options.sankey <highcharts_gantt.options.plot_options.sankey>`
    - :class:`SankeyOptions <highcharts_gantt.options.plot_options.sankey.SankeyOptions>`
  * - :mod:`.options.plot_options.scatter <highcharts_gantt.options.plot_options.scatter>`
    - :class:`ScatterOptions <highcharts_gantt.options.plot_options.scatter.ScatterOptions>`
      :class:`Scatter3DOptions <highcharts_gantt.options.plot_options.scatter.Scatter3DOptions>`
  * - :mod:`.options.plot_options.series <highcharts_gantt.options.plot_options.series>`
    - :class:`SeriesOptions <highcharts_gantt.options.plot_options.series.SeriesOptions>`
  * - :mod:`.options.plot_options.sonification <highcharts_gantt.options.plot_options.sonification>`
    - :class:`SeriesSonification <highcharts_gantt.options.plot_options.sonification.SeriesSonification>`
  * - :mod:`.options.plot_options.spline <highcharts_gantt.options.plot_options.spline>`
    - :class:`SplineOptions <highcharts_gantt.options.plot_options.spline.SplineOptions>`
  * - :mod:`.options.plot_options.sunburst <highcharts_gantt.options.plot_options.sunburst>`
    - :class:`SunburstOptions <highcharts_gantt.options.plot_options.sunburst.SunburstOptions>`
  * - :mod:`.options.plot_options.timeline <highcharts_gantt.options.plot_options.timeline>`
    - :class:`TimelineOptions <highcharts_gantt.options.plot_options.timeline.TimelineOptions>`
  * - :mod:`.options.plot_options.treegraph <highcharts_gantt.options.plot_options.treegraph>`
    - :class:`TreegraphOptions <highcharts_gantt.options.plot_options.treegraph.TreegraphOptions>`
      :class:`TreegraphEvents <highcharts_gantt.options.plot_options.treegraph.TreegraphEvents>`
  * - :mod:`.options.plot_options.treemap <highcharts_gantt.options.plot_options.treemap>`
    - :class:`TreemapOptions <highcharts_gantt.options.plot_options.treemap.TreemapOptions>`
  * - :mod:`.options.plot_options.vbp <highcharts_gantt.options.plot_options.vbp>`
    - :class:`VBPOptions <highcharts_gantt.options.plot_options.vbp.VBPOptions>`
      :class:`VBPParameters <highcharts_gantt.options.plot_options.vbp.VBPParameters>`
      :class:`ZoneLinesOptions <highcharts_gantt.options.plot_options.vbp.ZoneLinesOptions>`
      :class:`VolumeDivisionOptions <highcharts_gantt.options.plot_options.vbp.VolumeDivisionOptions>`
      :class:`VolumeDivisionStyles <highcharts_gantt.options.plot_options.vbp.VolumeDivisionStyles>`
  * - :mod:`.options.plot_options.vector <highcharts_gantt.options.plot_options.vector>`
    - :class:`VectorOptions <highcharts_gantt.options.plot_options.vector.VectorOptions>`
  * - :mod:`.options.plot_options.venn <highcharts_gantt.options.plot_options.venn>`
    - :class:`VennOptions <highcharts_gantt.options.plot_options.venn.VennOptions>`
  * - :mod:`.options.plot_options.wordcloud <highcharts_gantt.options.plot_options.wordcloud>`
    - :class:`WordcloudOptions <highcharts_gantt.options.plot_options.wordcloud.WordcloudOptions>`
      :class:`RotationOptions <highcharts_gantt.options.plot_options.wordcloud.RotationOptions>`
  * - :mod:`.options.plot_options.zigzag <highcharts_gantt.options.plot_options.zigzag>`
    - :class:`ZigZagOptions <highcharts_gantt.options.plot_options.zigzag.ZigZagOptions>`
      :class:`ZigZagParameters <highcharts_gantt.options.plot_options.zigzag.ZigZagParameters>`
  * - :mod:`.options.responsive <highcharts_gantt.options.responsive>`
    - :class:`Responsive <highcharts_gantt.options.responsive.Responsive>`
      :class:`ResponsiveRules <highcharts_gantt.options.responsive.ResponsiveRules>`
      :class:`Condition <highcharts_gantt.options.responsive.Condition>`
  * - :mod:`.options.series <highcharts_gantt.options.series>`
    -
  * - :mod:`.options.series.abands <highcharts_gantt.options.series.abands>`
    - :class:`AbandsSeries <highcharts_gantt.options.series.abands.AbandsSeries>`
      :class:`BBSeries <highcharts_gantt.options.series.abands.BBSeries>`
      :class:`KeltnerChannelsSeries <highcharts_gantt.options.series.abands.KeltnerChannelsSeries>`
      :class:`PCSeries <highcharts_gantt.options.series.abands.PCSeries>`
  * - :mod:`.options.series.ad <highcharts_gantt.options.series.ad>`
    - :class:`ADSeries <highcharts_gantt.options.series.ad.ADSeries>`
  * - :mod:`.options.series.arcdiagram <highcharts_gantt.options.series.arcdiagram>`
    - :class:`ArcDiagramSeries <highcharts_gantt.options.series.arcdiagram.ArcDiagramSeries>`
  * - :mod:`.options.series.area <highcharts_gantt.options.series.area>`
    - :class:`AreaSeries <highcharts_gantt.options.series.area.AreaSeries>`
      :class:`AreaRangeSeries <highcharts_gantt.options.series.area.AreaRangeSeries>`
      :class:`AreaSplineSeries <highcharts_gantt.options.series.area.AreaSplineSeries>`
      :class:`AreaSplineRangeSeries <highcharts_gantt.options.series.area.AreaSplineRangeSeries>`
      :class:`LineSeries <highcharts_gantt.options.series.area.LineSeries>`
      :class:`StreamGraphSeries <highcharts_gantt.options.series.area.StreamGraphSeries>`
  * - :mod:`.options.series.aroon <highcharts_gantt.options.series.aroon>`
    - :class:`AroonSeries <highcharts_gantt.options.series.aroon.AroonSeries>`
  * - :mod:`.options.series.atr <highcharts_gantt.options.series.atr>`
    - :class:`ATRSeries <highcharts_gantt.options.series.atr.ATRSeries>`
      :class:`NATRSeries <highcharts_gantt.options.series.atr.NATRSeries>`
  * - :mod:`.options.series.averages <highcharts_gantt.options.series.averages>`
    - :class:`DEMASeries <highcharts_gantt.options.series.averages.DEMASeries>`
      :class:`EMASeries <highcharts_gantt.options.series.averages.EMASeries>`
      :class:`SMASeries <highcharts_gantt.options.series.averages.SMASeries>`
      :class:`TEMASeries <highcharts_gantt.options.series.averages.TEMASeries>`
      :class:`VWAPSeries <highcharts_gantt.options.series.averages.VWAPSeries>`
      :class:`WMASeries <highcharts_gantt.options.series.averages.WMASeries>`
  * - :mod:`.options.series.bar <highcharts_gantt.options.series.bar>`
    - :class:`BarSeries <highcharts_gantt.options.series.bar.BarSeries>`
      :class:`ColumnSeries <highcharts_gantt.options.series.bar.ColumnSeries>`
      :class:`ColumnPyramidSeries <highcharts_gantt.options.series.bar.ColumnPyramidSeries>`
      :class:`ColumnRangeSeries <highcharts_gantt.options.series.bar.ColumnRangeSeries>`
      :class:`CylinderSeries <highcharts_gantt.options.series.bar.CylinderSeries>`
      :class:`VariwideSeries <highcharts_gantt.options.series.bar.VariwideSeries>`
      :class:`WaterfallSeries <highcharts_gantt.options.series.bar.WaterfallSeries>`
      :class:`WindBarbSeries <highcharts_gantt.options.series.bar.WindBarbSeries>`
      :class:`XRangeSeries <highcharts_gantt.options.series.bar.XRangeSeries>`
      :class:`BaseBarSeries <highcharts_gantt.options.series.bar.BaseBarSeries>`
  * - :mod:`.options.series.base <highcharts_gantt.options.series.base>`
    - :class:`SeriesBase <highcharts_gantt.options.series.base.SeriesBase>`
      :class:`IndicatorSeriesBase <highcharts_gantt.options.series.base.IndicatorSeriesBase>`
      :class:`NavigatorIndicatorSeries <highcharts_gantt.options.series.base.NavigatorIndicatorSeries>`
      :class:`IndicatorFactoryMixin <highcharts_gantt.options.series.base.IndicatorFactoryMixin>`
  * - :mod:`.options.series.bellcurve <highcharts_gantt.options.series.bellcurve>`
    - :class:`BellCurveSeries <highcharts_gantt.options.series.bellcurve.BellCurveSeries>`
  * - :mod:`.options.series.boxplot <highcharts_gantt.options.series.boxplot>`
    - :class:`BoxPlotSeries <highcharts_gantt.options.series.boxplot.BoxPlotSeries>`
      :class:`ErrorBarSeries <highcharts_gantt.options.series.boxplot.ErrorBarSeries>`
  * - :mod:`.options.series.bubble <highcharts_gantt.options.series.bubble>`
    - :class:`BubbleSeries <highcharts_gantt.options.series.bubble.BubbleSeries>`
  * - :mod:`.options.series.bullet <highcharts_gantt.options.series.bullet>`
    - :class:`BulletSeries <highcharts_gantt.options.series.bullet.BulletSeries>`
  * - :mod:`.options.series.candlestick <highcharts_gantt.options.series.candlestick>`
    - :class:`CandlestickSeries <highcharts_gantt.options.series.candlestick.CandlestickSeries>`
      :class:`HollowCandlestickSeries <highcharts_gantt.options.series.candlestick.HollowCandlestickSeries>`
      :class:`HeikinAshiSeries <highcharts_gantt.options.series.candlestick.HeikinAshiSeries>`
  * - :mod:`.options.series.data <highcharts_gantt.options.series.data>`
    -
  * - :mod:`.options.series.data.accessibility <highcharts_gantt.options.series.data.accessibility>`
    - :class:`DataPointAccessibility <highcharts_gantt.options.series.data.accessibility.DataPointAccessibility>`
  * - :mod:`.options.series.data.arcdiagram <highcharts_gantt.options.series.data.arcdiagram>`
    - :class:`ArcDiagramData <highcharts_gantt.options.series.data.arcdiagram.ArcDiagramData>`
  * - :mod:`.options.series.data.bar <highcharts_gantt.options.series.data.bar>`
    - :class:`BarData <highcharts_gantt.options.series.data.bar.BarData>`
      :class:`WaterfallData <highcharts_gantt.options.series.data.bar.WaterfallData>`
      :class:`WindBarbData <highcharts_gantt.options.series.data.bar.WindBarbData>`
      :class:`XRangeData <highcharts_gantt.options.series.data.bar.XRangeData>`
  * - :mod:`.options.series.data.base <highcharts_gantt.options.series.data.base>`
    - :class:`DataBase <highcharts_gantt.options.series.data.base.DataBase>`
  * - :mod:`.options.series.data.boxplot <highcharts_gantt.options.series.data.boxplot>`
    - :class:`BoxPlotData <highcharts_gantt.options.series.data.boxplot.BoxPlotData>`
  * - :mod:`.options.series.data.bullet <highcharts_gantt.options.series.data.bullet>`
    - :class:`BulletData <highcharts_gantt.options.series.data.bullet.BulletData>`
  * - :mod:`.options.series.data.candlestick <highcharts_gantt.options.series.data.candlestick>`
    - :class:`CandlestickData <highcharts_gantt.options.series.data.candlestick.CandlestickData>`
  * - :mod:`.options.series.data.cartesian <highcharts_gantt.options.series.data.cartesian>`
    - :class:`CartesianData <highcharts_gantt.options.series.data.cartesian.CartesianData>`
      :class:`Cartesian3DData <highcharts_gantt.options.series.data.cartesian.Cartesian3DData>`
      :class:`CartesianValueData <highcharts_gantt.options.series.data.cartesian.CartesianValueData>`
  * - :mod:`.options.series.data.connect <highcharts_gantt.options.series.data.connect>`
    - :class:`DataConnection <highcharts_gantt.options.series.data.connect.DataConnection>`
  * - :mod:`.options.series.data.connections <highcharts_gantt.options.series.data.connections>`
    - :class:`ConnectionData <highcharts_gantt.options.series.data.connections.ConnectionData>`
      :class:`WeightedConnectionData <highcharts_gantt.options.series.data.connections.WeightedConnectionData>`
      :class:`OutgoingWeightedConnectionData <highcharts_gantt.options.series.data.connections.OutgoingWeightedConnectionData>`
      :class:`ConnectionBase <highcharts_gantt.options.series.data.connections.ConnectionBase>`
  * - :mod:`.options.series.data.gantt <highcharts_gantt.options.series.data.gantt>`
    - :class:`GanttData <highcharts_gantt.options.series.data.gantt.GanttData>`
      :class:`ProgressIndicator <highcharts_gantt.options.series.data.gantt.ProgressIndicator>`
  * - :mod:`.options.series.data.hlc <highcharts_gantt.options.series.data.hlc>`
    - :class:`HLCData <highcharts_gantt.options.series.data.hlc.HLCData>`
      :class:`OHLCData <highcharts_gantt.options.series.data.hlc.OHLCData>`
  * - :mod:`.options.series.data.pie <highcharts_gantt.options.series.data.pie>`
    - :class:`PieData <highcharts_gantt.options.series.data.pie.PieData>`
      :class:`VariablePieData <highcharts_gantt.options.series.data.pie.VariablePieData>`
  * - :mod:`.options.series.data.range <highcharts_gantt.options.series.data.range>`
    - :class:`RangeData <highcharts_gantt.options.series.data.range.RangeData>`
      :class:`ConnectedRangeData <highcharts_gantt.options.series.data.range.ConnectedRangeData>`
  * - :mod:`.options.series.data.single_point <highcharts_gantt.options.series.data.single_point>`
    - :class:`SinglePointData <highcharts_gantt.options.series.data.single_point.SinglePointData>`
      :class:`SingleValueData <highcharts_gantt.options.series.data.single_point.SingleValueData>`
      :class:`SingleXData <highcharts_gantt.options.series.data.single_point.SingleXData>`
      :class:`LabeledSingleXData <highcharts_gantt.options.series.data.single_point.LabeledSingleXData>`
      :class:`ConnectedSingleXData <highcharts_gantt.options.series.data.single_point.ConnectedSingleXData>`
      :class:`SinglePointBase <highcharts_gantt.options.series.data.single_point.SinglePointBase>`
  * - :mod:`.options.series.data.sunburst <highcharts_gantt.options.series.data.sunburst>`
    - :class:`SunburstData <highcharts_gantt.options.series.data.sunburst.SunburstData>`
  * - :mod:`.options.series.data.treegraph <highcharts_gantt.options.series.data.treegraph>`
    - :class:`TreegraphData <highcharts_gantt.options.series.data.treegraph.TreegraphData>`
  * - :mod:`.options.series.data.treemap <highcharts_gantt.options.series.data.treemap>`
    - :class:`TreemapData <highcharts_gantt.options.series.data.treemap.TreemapData>`
  * - :mod:`.options.series.data.vector <highcharts_gantt.options.series.data.vector>`
    - :class:`VectorData <highcharts_gantt.options.series.data.vector.VectorData>`
  * - :mod:`.options.series.data.venn <highcharts_gantt.options.series.data.venn>`
    - :class:`VennData <highcharts_gantt.options.series.data.venn.VennData>`
  * - :mod:`.options.series.data.wordcloud <highcharts_gantt.options.series.data.wordcloud>`
    - :class:`WordcloudData <highcharts_gantt.options.series.data.wordcloud.WordcloudData>`
  * - :mod:`.options.series.dependencywheel <highcharts_gantt.options.series.dependencywheel>`
    - :class:`DependencyWheelSeries <highcharts_gantt.options.series.dependencywheel.DependencyWheelSeries>`
  * - :mod:`.options.series.disparity_index <highcharts_gantt.options.series.disparity_index>`
    - :class:`DisparityIndexSeries <highcharts_gantt.options.series.disparity_index.DisparityIndexSeries>`
  * - :mod:`.options.series.dmi <highcharts_gantt.options.series.dmi>`
    - :class:`DMISeries <highcharts_gantt.options.series.dmi.DMISeries>`
  * - :mod:`.options.series.dumbbell <highcharts_gantt.options.series.dumbbell>`
    - :class:`DumbbellSeries <highcharts_gantt.options.series.dumbbell.DumbbellSeries>`
      :class:`LollipopSeries <highcharts_gantt.options.series.dumbbell.LollipopSeries>`
  * - :mod:`.options.series.flags <highcharts_gantt.options.series.flags>`
    - :class:`FlagsSeries <highcharts_gantt.options.series.flags.FlagsSeries>`
  * - :mod:`.options.series.funnel <highcharts_gantt.options.series.funnel>`
    - :class:`FunnelSeries <highcharts_gantt.options.series.funnel.FunnelSeries>`
      :class:`Funnel3DSeries <highcharts_gantt.options.series.funnel.Funnel3DSeries>`
  * - :mod:`.options.series.gantt <highcharts_gantt.options.series.gantt>`
    - :class:`GanttSeries <highcharts_gantt.options.series.gantt.GanttSeries>`
  * - :mod:`.options.series.gauge <highcharts_gantt.options.series.gauge>`
    - :class:`GaugeSeries <highcharts_gantt.options.series.gauge.GaugeSeries>`
      :class:`SolidGaugeSeries <highcharts_gantt.options.series.gauge.SolidGaugeSeries>`
  * - :mod:`.options.series.heatmap <highcharts_gantt.options.series.heatmap>`
    - :class:`HeatmapSeries <highcharts_gantt.options.series.heatmap.HeatmapSeries>`
      :class:`TilemapSeries <highcharts_gantt.options.series.heatmap.TilemapSeries>`
  * - :mod:`.options.series.histogram <highcharts_gantt.options.series.histogram>`
    - :class:`HistogramSeries <highcharts_gantt.options.series.histogram.HistogramSeries>`
  * - :mod:`.options.series.hlc <highcharts_gantt.options.series.hlc>`
    - :class:`HLCSeries <highcharts_gantt.options.series.hlc.HLCSeries>`
      :class:`OHLCSeries <highcharts_gantt.options.series.hlc.OHLCSeries>`
  * - :mod:`.options.series.item <highcharts_gantt.options.series.item>`
    - :class:`ItemSeries <highcharts_gantt.options.series.item.ItemSeries>`
  * - :mod:`.options.series.labels <highcharts_gantt.options.series.labels>`
    - :class:`SeriesLabel <highcharts_gantt.options.series.labels.SeriesLabel>`
      :class:`Box <highcharts_gantt.options.series.labels.Box>`
  * - :mod:`.options.series.linear_regressions <highcharts_gantt.options.series.linear_regressions>`
    - :class:`LinearRegressionSeries <highcharts_gantt.options.series.linear_regressions.LinearRegressionSeries>`
      :class:`LinearRegressionAngleSeries <highcharts_gantt.options.series.linear_regressions.LinearRegressionAngleSeries>`
      :class:`LinearRegressionInterceptSeries <highcharts_gantt.options.series.linear_regressions.LinearRegressionInterceptSeries>`
      :class:`LinearRegressionSlopeSeries <highcharts_gantt.options.series.linear_regressions.LinearRegressionSlopeSeries>`
      :class:`TrendlineSeries <highcharts_gantt.options.series.linear_regressions.TrendlineSeries>`
  * - :mod:`.options.series.momentum <highcharts_gantt.options.series.momentum>`
    - :class:`MomentumSeries <highcharts_gantt.options.series.momentum.MomentumSeries>`
      :class:`OBVSeries <highcharts_gantt.options.series.momentum.OBVSeries>`
      :class:`ROCSeries <highcharts_gantt.options.series.momentum.ROCSeries>`
      :class:`RSISeries <highcharts_gantt.options.series.momentum.RSISeries>`
  * - :mod:`.options.series.momentum.ikh <highcharts_gantt.options.series.momentum.ikh>`
    - :class:`IKHSeries <highcharts_gantt.options.series.momentum.ikh.IKHSeries>`
  * - :mod:`.options.series.momentum.macd <highcharts_gantt.options.series.momentum.macd>`
    - :class:`MACDSeries <highcharts_gantt.options.series.momentum.macd.MACDSeries>`
  * - :mod:`.options.series.momentum.supertrend <highcharts_gantt.options.series.momentum.supertrend>`
    - :class:`SupertrendSeries <highcharts_gantt.options.series.momentum.supertrend.SupertrendSeries>`
  * - :mod:`.options.series.networkgraph <highcharts_gantt.options.series.networkgraph>`
    - :class:`NetworkGraphSeries <highcharts_gantt.options.series.networkgraph.NetworkGraphSeries>`
  * - :mod:`.options.series.organization <highcharts_gantt.options.series.organization>`
    - :class:`OrganizationSeries <highcharts_gantt.options.series.organization.OrganizationSeries>`
  * - :mod:`.options.series.oscillators <highcharts_gantt.options.series.oscillators>`
    - :class:`AroonOscillatorSeries <highcharts_gantt.options.series.oscillators.AroonOscillatorSeries>`
      :class:`APOSeries <highcharts_gantt.options.series.oscillators.APOSeries>`
      :class:`CCISeries <highcharts_gantt.options.series.oscillators.CCISeries>`
      :class:`ChaikinSeries <highcharts_gantt.options.series.oscillators.ChaikinSeries>`
      :class:`CMOSeries <highcharts_gantt.options.series.oscillators.CMOSeries>`
      :class:`DPOSeries <highcharts_gantt.options.series.oscillators.DPOSeries>`
      :class:`TRIXSeries <highcharts_gantt.options.series.oscillators.TRIXSeries>`
      :class:`WilliamsRSeries <highcharts_gantt.options.series.oscillators.WilliamsRSeries>`
  * - :mod:`.options.series.oscillators.ao <highcharts_gantt.options.series.oscillators.ao>`
    - :class:`AOSeries <highcharts_gantt.options.series.oscillators.ao.AOSeries>`
  * - :mod:`.options.series.oscillators.klinger <highcharts_gantt.options.series.oscillators.klinger>`
    - :class:`KlingerSeries <highcharts_gantt.options.series.oscillators.klinger.KlingerSeries>`
  * - :mod:`.options.series.oscillators.money_flow <highcharts_gantt.options.series.oscillators.money_flow>`
    - :class:`MFISeries <highcharts_gantt.options.series.oscillators.money_flow.MFISeries>`
      :class:`CMFSeries <highcharts_gantt.options.series.oscillators.money_flow.CMFSeries>`
  * - :mod:`.options.series.oscillators.ppo <highcharts_gantt.options.series.oscillators.ppo>`
    - :class:`PPOSeries <highcharts_gantt.options.series.oscillators.ppo.PPOSeries>`
  * - :mod:`.options.series.oscillators.stochastic <highcharts_gantt.options.series.oscillators.stochastic>`
    - :class:`StochasticSeries <highcharts_gantt.options.series.oscillators.stochastic.StochasticSeries>`
      :class:`SlowStochasticSeries <highcharts_gantt.options.series.oscillators.stochastic.SlowStochasticSeries>`
  * - :mod:`.options.series.packedbubble <highcharts_gantt.options.series.packedbubble>`
    - :class:`PackedBubbleSeries <highcharts_gantt.options.series.packedbubble.PackedBubbleSeries>`
  * - :mod:`.options.series.pareto <highcharts_gantt.options.series.pareto>`
    - :class:`ParetoSeries <highcharts_gantt.options.series.pareto.ParetoSeries>`
  * - :mod:`.options.series.pie <highcharts_gantt.options.series.pie>`
    - :class:`PieSeries <highcharts_gantt.options.series.pie.PieSeries>`
      :class:`VariablePieSeries <highcharts_gantt.options.series.pie.VariablePieSeries>`
  * - :mod:`.options.series.pivot_points <highcharts_gantt.options.series.pivot_points>`
    - :class:`PivotPointsSeries <highcharts_gantt.options.series.pivot_points.PivotPointsSeries>`
  * - :mod:`.options.series.polygon <highcharts_gantt.options.series.polygon>`
    - :class:`PolygonSeries <highcharts_gantt.options.series.polygon.PolygonSeries>`
  * - :mod:`.options.series.price_envelopes <highcharts_gantt.options.series.price_envelopes>`
    - :class:`PriceEnvelopesSeries <highcharts_gantt.options.series.price_envelopes.PriceEnvelopesSeries>`
  * - :mod:`.options.series.psar <highcharts_gantt.options.series.psar>`
    - :class:`PSARSeries <highcharts_gantt.options.series.psar.PSARSeries>`
  * - :mod:`.options.series.pyramid <highcharts_gantt.options.series.pyramid>`
    - :class:`PyramidSeries <highcharts_gantt.options.series.pyramid.PyramidSeries>`
      :class:`Pyramid3DSeries <highcharts_gantt.options.series.pyramid.Pyramid3DSeries>`
  * - :mod:`.options.series.sankey <highcharts_gantt.options.series.sankey>`
    - :class:`SankeySeries <highcharts_gantt.options.series.sankey.SankeySeries>`
  * - :mod:`.options.series.scatter <highcharts_gantt.options.series.scatter>`
    - :class:`ScatterSeries <highcharts_gantt.options.series.scatter.ScatterSeries>`
      :class:`Scatter3DSeries <highcharts_gantt.options.series.scatter.Scatter3DSeries>`
  * - :mod:`.options.series.series_generator <highcharts_gantt.options.series.series_generator>`
    - :func:`create_series_obj() <highcharts_gantt.options.series.series_generator.create_series_obj>`
  * - :mod:`.options.series.spline <highcharts_gantt.options.series.spline>`
    - :class:`SplineSeries <highcharts_gantt.options.series.spline.SplineSeries>`
  * - :mod:`.options.series.sunburst <highcharts_gantt.options.series.sunburst>`
    - :class:`SunburstSeries <highcharts_gantt.options.series.sunburst.SunburstSeries>`
  * - :mod:`.options.series.timeline <highcharts_gantt.options.series.timeline>`
    - :class:`TimelineSeries <highcharts_gantt.options.series.timeline.TimelineSeries>`
  * - :mod:`.options.series.treegraph <highcharts_gantt.options.series.treegraph>`
    - :class:`TreegraphSeries <highcharts_gantt.options.series.treegraph.TreegraphSeries>`
  * - :mod:`.options.series.treemap <highcharts_gantt.options.series.treemap>`
    - :class:`TreemapSeries <highcharts_gantt.options.series.treemap.TreemapSeries>`
  * - :mod:`.options.series.vbp <highcharts_gantt.options.series.vbp>`
    - :class:`VBPSeries <highcharts_gantt.options.series.vbp.VBPSeries>`
  * - :mod:`.options.series.vector <highcharts_gantt.options.series.vector>`
    - :class:`VectorSeries <highcharts_gantt.options.series.vector.VectorSeries>`
  * - :mod:`.options.series.venn <highcharts_gantt.options.series.venn>`
    - :class:`VennSeries <highcharts_gantt.options.series.venn.VennSeries>`
  * - :mod:`.options.series.wordcloud <highcharts_gantt.options.series.wordcloud>`
    - :class:`WordcloudSeries <highcharts_gantt.options.series.wordcloud.WordcloudSeries>`
  * - :mod:`.options.series.zigzag <highcharts_gantt.options.series.zigzag>`
    - :class:`ZigZagSeries <highcharts_gantt.options.series.zigzag.ZigZagSeries>`
  * - :mod:`.options.sonification <highcharts_gantt.options.sonification>`
    - :class:`SonificationOptions <highcharts_gantt.options.sonification.SonificationOptions>`
  * - :mod:`.options.sonification.grouping <highcharts_gantt.options.sonification.grouping>`
    - :class:`PointGrouping <highcharts_gantt.options.sonification.grouping.SonificationGrouping>`
  * - :mod:`.options.sonification.mapping <highcharts_gantt.options.sonification.mapping>`
    - :class:`SonificationMapping <highcharts_gantt.options.sonification.mapping.SonificationMapping>`
      :class:`AudioParameter <highcahrts_core.options.sonification.mapping.AudioParameter>`
      :class:`AudioFilter <highcharts_gantt.options.sonification.mapping.AudioFilter>`
      :class:`PitchParameter <highcharts_gantt.options.sonification.mapping.PitchParameter>`
      :class:`TremoloEffect <highcahrts_core.options.sonification.mapping.TremoloEffect>`
  * - :mod:`.options.sonification.track_configurations <highcharts_gantt.options.sonification.track_configurations>`
    - :class:`InstrumentTrackConfiguration <highcharts_gantt.options.sonification.track_configurations.InstrumentTrackConfiguration>`
      :class:`SpeechTrackConfiguration <highcharts_gantt.options.sonification.track_configurations.SpeechTrackConfiguration>`
      :class:`ContextTrackConfiguration <highcharts_gantt.options.sonification.track_configurations.ContextTrackConfiguration>`
      :class:`TrackConfigurationBase <highcharts_gantt.options.sonification.track_configurations.TrackConfigurationBase>`
      :class:`ActiveWhen <highcharts_gantt.options.sonification.track_configurations.ActiveWhen>`
  * - :mod:`.options.stock_tools <highcharts_gantt.options.stock_tools>`
    - :class:`StockTools <highcharts_gantt.options.stock_tools.StockTools>`
      :class:`StockToolsGUI <highcharts_gantt.options.stock_tools.StockToolsGUI>`
  * - :mod:`.options.stock_tools.definitions <highcharts_gantt.options.stock_tools.definitions>`
    - :class:`StockToolsDefinitions <highcharts_gantt.options.stock_tools.definitions.StockToolsDefinitions>`
      :class:`AdvancedDefinitions <highcharts_gantt.options.stock_tools.definitions.AdvancedDefinitions>`
      :class:`CrookedLinesDefinitions <highcharts_gantt.options.stock_tools.definitions.CrookedLinesDefinitions>`
      :class:`FlagsDefinitions <highcharts_gantt.options.stock_tools.definitions.FlagsDefinitions>`
      :class:`LinesDefinitions <highcharts_gantt.options.stock_tools.definitions.LinesDefinitions>`
      :class:`MeasureDefinitions <highcharts_gantt.options.stock_tools.definitions.MeasureDefinitions>`
      :class:`SimpleShapesDefinitions <highcharts_gantt.options.stock_tools.definitions.SimpleShapesDefinitions>`
      :class:`TypeChangeDefinitions <highcharts_gantt.options.stock_tools.definitions.TypeChangeDefinitions>`
      :class:`VerticalLabelsDefinitions <highcharts_gantt.options.stock_tools.definitions.VerticalLabelsDefinitions>`
      :class:`ZoomChangeDefinitions <highcharts_gantt.options.stock_tools.definitions.ZoomChangeDefinitions>`
      :class:`Definition <highcharts_gantt.options.stock_tools.definitions.Definition>`
  * - :mod:`.options.subtitle <highcharts_gantt.options.subtitle>`
    - :class:`Subtitle <highcharts_gantt.options.subtitle.Subtitle>`
  * - :mod:`.options.time <highcharts_gantt.options.time>`
    - :class:`Time <highcharts_gantt.options.time.Time>`
  * - :mod:`.options.title <highcharts_gantt.options.title>`
    - :class:`Title <highcharts_gantt.options.title.Title>`
  * - :mod:`.options.tooltips <highcharts_gantt.options.tooltips>`
    - :class:`Tooltip <highcharts_gantt.options.tooltips.Tooltip>`
