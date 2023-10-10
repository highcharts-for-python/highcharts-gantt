###########################################
Highcharts Gantt for Python API Reference
###########################################

.. contents::
  :local:
  :depth: 3
  :backlinks: entry

------------------------

*****************************
API Design Patterns
*****************************

Code Style: Python vs JavaScript Naming Conventions
=======================================================

.. include:: using/_code_style_naming_conventions.rst

Standard Methods
=======================================

Every single object supported by the
`Highcharts Gantt API <https://api.highcharts.com/gantt/>`__ corresponds to a Python
class in **Highcharts Gantt for Python**. These classes generally inherit from the
:class:`HighchartsMeta <highcharts_gantt.metaclasses.HighchartsMeta>` metaclass, which
provides each class with a number of standard methods.

These methods are the "workhorses" of **Highcharts Gantt for Python** and you will be
relying heavily on them when using the library. Thankfully, their signatures and behavior
is generally consistent - even if what happens "under the hood" is class-specific at
times.

Deserialization Methods
---------------------------

.. include:: api/_deserialization_methods.rst

Serialization Methods
--------------------------

.. include:: api/_serialization_methods.rst

Other Convenience Methods
------------------------------

.. include:: api/_other_convenience_methods.rst

Handling Default Values
===============================

.. include:: api/_handling_defaults.rst


Module Structure
=====================

.. include:: api/_module_structure.rst

Class Structures and Inheritance
====================================

.. include:: api/_class_structures.rst

.. warning::

  Certain sections of the **Highcharts Gantt for Python** library - in particular the
  ``options.series`` classes - rely heavily on multiple inheritance. This is a known
  anti-pattern in Python development as it runs the risk of encountering the
  :term:`diamond of death` inheritance problem. This complicates the process of inheriting
  methods or properties from parent classes when properties or methods share names
  across multiple parents.

  We know this the diamond of death is an anti-pattern, but it was a necessary one to 
  minimize code duplication and maximize consistency. For that reason, we implemented it 
  properly *despite* the anti-pattern, using some advanced Python concepts to navigate the 
  Python MRO (Method Resolution Order) system cleanly. However, an awareness of the pattern 
  used may prove helpful if your code inherits from the Highcharts for Python classes.

  .. seealso::

    For a more in-depth discussion of how the anti-pattern was implemented safely and
    reliably, please review the :doc:`Contributor Guidelines <contributing>`.

--------------------------

.. _core_components:

********************************
Core Components
********************************

.. list-table::
  :widths: 60 40
  :header-rows: 1

  * - Module
    - Classes / Functions
  * - :mod:`.chart <highcharts_gantt.chart>`
    - :class:`Chart <highcharts_gantt.chart.Chart>`
  * - :mod:`.global_options <highcharts_gantt.global_options>`
    -
  * - :mod:`.global_options.language <highcharts_gantt.global_options.language>`
    - :class:`Language <highcharts_gantt.global_options.language.Language>`
  * - :mod:`.global_options.language.accessibility <highcharts_gantt.global_options.language.accessibility>`
    - :class:`AccessibilityLanguageOptions <highcharts_gantt.global_options.language.accessibility.AccessibilityLanguageOptions>`
  * - :mod:`.global_options.language.accessibility.announce_new_data <highcharts_gantt.global_options.language.accessibility.announce_new_data>`
    - :class:`AnnounceNewDataLanguageOptions <highcharts_gantt.global_options.language.accessibility.announce_new_data.AnnounceNewDataLanguageOptions>`
  * - :mod:`.global_options.language.accessibility.axis <highcharts_gantt.global_options.language.accessibility.axis>`
    - :class:`AxisLanguageOptions <highcharts_gantt.global_options.language.accessibility.axis.AxisLanguageOptions>`
  * - :mod:`.global_options.language.accessibility.chart_types <highcharts_gantt.global_options.language.accessibility.chart_types>`
    - :class:`ChartTypesLanguageOptions <highcharts_gantt.global_options.language.accessibility.chart_types.ChartTypesLanguageOptions>`
  * - :mod:`.global_options.language.accessibility.exporting <highcharts_gantt.global_options.language.accessibility.exporting>`
    - :class:`ExportingLanguageOptions <highcharts_gantt.global_options.language.accessibility.exporting.ExportingLanguageOptions>`
  * - :mod:`.global_options.language.accessibility.legend <highcharts_gantt.global_options.language.accessibility.legend>`
    - :class:`LegendLanguageOptions <highcharts_gantt.global_options.language.accessibility.legend.LegendLanguageOptions>`
  * - :mod:`.global_options.language.accessibility.range_selector <highcharts_gantt.global_options.language.accessibility.range_selector>`
    - :class:`RangeSelectorLanguageOptions <highcharts_gantt.global_options.language.accessibility.range_selector.RangeSelectorLanguageOptions>`
  * - :mod:`.global_options.language.accessibility.screen_reader_section <highcharts_gantt.global_options.language.accessibility.screen_reader_section>`
    - :class:`ScreenReaderSectionLanguageOptions <highcharts_gantt.global_options.language.accessibility.screen_reader_section.ScreenReaderSectionLanguageOptions>`
      :class:`ScreenReaderSectionAnnotationLanguage <highcharts_gantt.global_options.language.accessibility.screen_reader_section.ScreenReaderSectionAnnotationLanguage>`
  * - :mod:`.global_options.language.accessibility.series <highcharts_gantt.global_options.language.accessibility.series>`
    - :class:`SeriesLanguageOptions <highcharts_gantt.global_options.language.accessibility.series.SeriesLanguageOptions>`
      :class:`SeriesSummaryLanguageOptions <highcharts_gantt.global_options.language.accessibility.series.SeriesSummaryLanguageOptions>`
      :class:`SeriesTypeDescriptions <highcharts_gantt.global_options.language.accessibility.series.SeriesTypeDescriptions>`
  * - :mod:`.global_options.language.accessibility.sonification <highcharts_gantt.global_options.language.accessibility.sonification>`
    - :class:`SonificationLanguageOptions <highcharts_gantt.global_options.language.accessibility.sonification.SonificationLanguageOptions>`
  * - :mod:`.global_options.language.accessibility.table <highcharts_gantt.global_options.language.accessibility.table>`
    - :class:`TableLanguageOptions <highcharts_gantt.global_options.language.accessibility.table.TableLanguageOptions>`
  * - :mod:`.global_options.language.accessibility.zoom <highcharts_gantt.global_options.language.accessibility.zoom>`
    - :class:`ZoomLanguageOptions <highcharts_gantt.global_options.language.accessibility.zoom.ZoomLanguageOptions>`
  * - :mod:`.global_options.language.export_data <highcharts_gantt.global_options.language.export_data>`
    - :class:`ExportDataLanguageOptions <highcharts_gantt.global_options.language.export_data.ExportDataLanguageOptions>`
  * - :mod:`.global_options.language.navigation <highcharts_gantt.global_options.language.navigation>`
    - :class:`NavigationLanguageOptions <highcharts_gantt.global_options.language.navigation.NavigationLanguageOptions>`
      :class:`PopupLanguageOptions <highcharts_gantt.global_options.language.navigation.PopupLanguageOptions>`
  * - :mod:`.global_options.language.stock_tools <highcharts_gantt.global_options.language.stock_tools>`
    - :class:`StockToolsLanguageOptions <highcharts_gantt.global_options.language.stock_tools.StockToolsLanguageOptions>`
      :class:`StockToolsGUI <highcharts_gantt.global_options.language.stock_tools.StockToolsGUI>`
  * - :mod:`.global_options.shared_options <highcharts_gantt.global_options.shared_options>`
    - :class:`SharedGanttOptions <highcharts_gantt.global_options.shared_options.SharedGanttOptions>`
      :class:`SharedStockOptions <highcharts_gantt.global_options.shared_options.SharedStockOptions>`
      :class:`SharedOptions <highcharts_gantt.global_options.shared_options.SharedOptions>`
  * - :mod:`.headless_export <highcharts_gantt.headless_export>`
    - :class:`ExportServer <highcharts_gantt.headless_export.ExportServer>`
  * - :mod:`.highcharts <highcharts_gantt.highcharts>`
    - (most classes from across the library)
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
  * - :mod:`.options.chart.options_3d <highcharts_gantt.options.chart.options_3d>`
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
  * - :mod:`.options.plot_options.pictorial <highcharts_gantt.options.plot_options.pictorial>`
    - :class:`PictorialOptions <highcharts_gantt.options.plot_options.pictorial.PictorialOptions>`
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
  * - :mod:`.options.series.data.arcdiagram <highcharts_stock.options.series.data.arcdiagram>`
    - :class:`ArcDiagramData <highcharts_stock.options.series.data.arcdiagram.ArcDiagramData>`
      :class:`ArcDiagramDataCollection <highcharts_stock.options.series.data.arcidagram.ArcDiagramDataCollection>`
  * - :mod:`.options.series.data.bar <highcharts_stock.options.series.data.bar>`
    - :class:`BarData <highcharts_stock.options.series.data.bar.BarData>`
      :class:`BarDataCollection <highcharts_stock.options.series.data.bar.BarDataCollection>`
      :class:`WaterfallData <highcharts_stock.options.series.data.bar.WaterfallData>`
      :class:`WaterfallDataCollection <highcharts_stock.options.series.data.bar.WaterfallDataCollection>`
      :class:`WindBarbData <highcharts_stock.options.series.data.bar.WindBarbData>`
      :class:`WindBarbDataCollection <highcharts_stock.options.series.data.bar.WindBarbDataCollection>`
      :class:`XRangeData <highcharts_stock.options.series.data.bar.XRangeData>`
      :class:`XRangeDataCollection <highcharts_stock.options.series.data.bar.XRangeDataCollection>`
  * - :mod:`.options.series.data.base <highcharts_stock.options.series.data.base>`
    - :class:`DataBase <highcharts_stock.options.series.data.base.DataBase>`
  * - :mod:`.options.series.data.boxplot <highcharts_stock.options.series.data.boxplot>`
    - :class:`BoxPlotData <highcharts_stock.options.series.data.boxplot.BoxPlotData>`
      :class:`BoxPlotDataCollection <highcharts_stock.options.series.data.boxplot.BoxPlotDataCollection>`
  * - :mod:`.options.series.data.bullet <highcharts_stock.options.series.data.bullet>`
    - :class:`BulletData <highcharts_stock.options.series.data.bullet.BulletData>`
      :class:`BulletDataCollection <highcharts_stock.options.series.data.bullet.BulletDataCollection>`
  * - :mod:`.options.series.data.candlestick <highcharts_stock.options.series.data.candlestick>`
    - :class:`CandlestickData <highcharts_stock.options.series.data.candlestick.CandlestickData>`
  * - :mod:`.options.series.data.cartesian <highcharts_stock.options.series.data.cartesian>`
    - :class:`CartesianData <highcharts_stock.options.series.data.cartesian.CartesianData>`
      :class:`CartesianDataCollection <highcharts_stock.options.series.data.cartesian.CartesianDataCollection>`
      :class:`Cartesian3DData <highcharts_stock.options.series.data.cartesian.Cartesian3DData>`
      :class:`Cartesian3DDataCollection <highcharts_stock.options.series.data.cartesian.Cartesian3DDataCollection>`
      :class:`CartesianValueData <highcharts_stock.options.series.data.cartesian.CartesianValueData>`
      :class:`CartesianValueDataCollection <highcharts_stock.options.series.data.cartesian.CartesianValueDataCollection>`
  * - :mod:`.options.series.data.collections <highcharts_stock.options.series.data.collections>`
    - :class:`DataPointCollection <highcharts_stock.options.series.data.collections.DataPointCollection>`
  * - :mod:`.options.series.data.connections <highcharts_stock.options.series.data.connections>`
    - :class:`ConnectionData <highcharts_stock.options.series.data.connections.ConnectionData>`
      :class:`ConnectionDataCollection <highcharts_stock.options.series.data.connections.ConnectionDataCollection>`
      :class:`WeightedConnectionData <highcharts_stock.options.series.data.connections.WeightedConnectionData>`
      :class:`WeightedConnectionDataCollection <highcharts_stock.options.series.data.connections.WeightedConnectionDataCollection>`
      :class:`OutgoingWeightedConnectionData <highcharts_stock.options.series.data.connections.OutgoingWeightedConnectionData>`
      :class:`OutgoingWeightedConnectionDataCollection <highcharts_stock.options.series.data.connections.OutgoingWeightedConnectionDataCollection>`
      :class:`ConnectionBase <highcharts_stock.options.series.data.connections.ConnectionBase>`
  * - :mod:`.options.series.data.gantt <highcharts_gantt.options.series.data.gantt>`
    - :class:`GanttData <highcharts_gantt.options.series.data.gantt.GanttData>`
      :class:`GanttDataCollection <highcharts_gantt.options.series.data.gantt.GanttDataCollection>`
      :class:`ProgressIndicator <highcharts_gantt.options.series.data.gantt.ProgressIndicator>`
  * - :mod:`.options.series.data.hlc <highcharts_stock.options.series.data.hlc>`
    - :class:`HLCData <highcharts_stock.options.series.data.hlc.HLCData>`
      :class:`HLCDataCollection <highcharts_stock.options.series.data.hlc.HLCDataCollection>`
      :class:`OHLCData <highcharts_stock.options.series.data.hlc.OHLCData>`
      :class:`OHLCDataCollection <highcharts_stock.options.series.data.hlc.OHLCDataCollection>`
  * - :mod:`.options.series.data.pie <highcharts_stock.options.series.data.pie>`
    - :class:`PieData <highcharts_stock.options.series.data.pie.PieData>`
      :class:`PieDataCollection <highcharts_stock.options.series.data.pie.PieDataCollection>`
      :class:`VariablePieData <highcharts_stock.options.series.data.pie.VariablePieData>`
      :class:`VariablePieDataCollection <highcharts_stock.options.series.data.pie.VariablePieDataCollection>`
  * - :mod:`.options.series.data.range <highcharts_stock.options.series.data.range>`
    - :class:`RangeData <highcharts_stock.options.series.data.range.RangeData>`
      :class:`RangeDataCollection <highcharts_stock.options.series.data.range.RangeDataCollection>`
      :class:`ConnectedRangeData <highcharts_stock.options.series.data.range.ConnectedRangeData>`
      :class:`ConnectedRangeDataCollection <highcharts_stock.options.series.data.range.ConnectedRangeDataCollection>`
  * - :mod:`.options.series.data.single_point <highcharts_stock.options.series.data.single_point>`
    - :class:`SinglePointData <highcharts_stock.options.series.data.single_point.SinglePointData>`
      :class:`SinglePointDataCollection <highcharts_stock.options.series.data.single_point.SinglePointDataCollection>`
      :class:`SingleValueData <highcharts_stock.options.series.data.single_point.SingleValueData>`
      :class:`SingleValueDataCollection <highcharts_stock.options.series.data.single_point.SingleValueDataCollection>`
      :class:`SingleXData <highcharts_stock.options.series.data.single_point.SingleXData>`
      :class:`SingleXDataCollection <highcharts_stock.options.series.data.single_point.SingleXDataCollection>`
      :class:`LabeledSingleXData <highcharts_stock.options.series.data.single_point.LabeledSingleXData>`
      :class:`LabeledSingleXDataCollection <highcharts_stock.options.series.data.single_point.LabeledSingleXDataCollection>`
      :class:`ConnectedSingleXData <highcharts_stock.options.series.data.single_point.ConnectedSingleXData>`
      :class:`ConnectedSingleXDataCollection <highcharts_stock.options.series.data.single_point.ConnectedSingleXDataCollection>`
      :class:`SinglePointBase <highcharts_stock.options.series.data.single_point.SinglePointBase>`
  * - :mod:`.options.series.data.sunburst <highcharts_stock.options.series.data.sunburst>`
    - :class:`SunburstData <highcharts_stock.options.series.data.sunburst.SunburstData>`
      :class:`SunburstDataCollection <highcharts_stock.options.series.data.sunburst.SunburstDataCollection>`
  * - :mod:`.options.series.data.treegraph <highcharts_stock.options.series.data.treegraph>`
    - :class:`TreegraphData <highcharts_stock.options.series.data.treegraph.TreegraphData>`
      :class:`TreegraphDataCollection <highcharts_stock.options.series.data.treegraph.TreegraphDataCollection>`
  * - :mod:`.options.series.data.treemap <highcharts_stock.options.series.data.treemap>`
    - :class:`TreemapData <highcharts_stock.options.series.data.treemap.TreemapData>`
      :class:`TreemapDataCollection <highcharts_stock.options.series.data.treemap.TreemapDataCollection>`
  * - :mod:`.options.series.data.vector <highcharts_stock.options.series.data.vector>`
    - :class:`VectorData <highcharts_stock.options.series.data.vector.VectorData>`
      :class:`VectorDataCollection <highcharts_stock.options.series.data.vector.VectorDataCollection>`
  * - :mod:`.options.series.data.venn <highcharts_stock.options.series.data.venn>`
    - :class:`VennData <highcharts_stock.options.series.data.venn.VennData>`
      :class:`VennDataCollection <highcharts_stock.options.series.data.venn.VennDataCollection>`
  * - :mod:`.options.series.data.wordcloud <highcharts_stock.options.series.data.wordcloud>`
    - :class:`WordcloudData <highcharts_stock.options.series.data.wordcloud.WordcloudData>`
      :class:`WordcloudDataCollection <highcharts_stock.options.series.data.wordcloud.WordcloudDataCollection>`
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
  * - :mod:`.options.series.pictorial <highcharts_gantt.options.series.pictorial>`
    - :class:`PictorialSeries <highcharts_gantt.options.series.pictorial.PictorialSeries>`
      :class:`PictorialPaths <highcharts_gantt.options.series.pictorial.PictorialPaths>`
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
  * - :mod:`.utility_classes <highcharts_gantt.utility_classes>`
    -
  * - :mod:`.utility_classes.animation <highcharts_gantt.utility_classes.animation>`
    - :class:`AnimationOptions <highcharts_gantt.utility_classes.animation.AnimationOptions>`
  * - :mod:`.utility_classes.ast <highcharts_gantt.utility_classes.ast>`
    - :class:`ASTMap <highcharts_gantt.utility_classes.ast.ASTMap>`
      :class:`ASTNode <highcharts_gantt.utility_classes.ast.ASTNode>`
      :class:`TextPath <highcharts_gantt.utility_classes.ast.TextPath>`
      :class:`AttributeObject <highcharts_gantt.utility_classes.ast.AttributeObject>`
  * - :mod:`.utility_classes.breadcrumbs <highcharts_gantt.utility_classes.breadcrumbs>`
    - :class:`BreadcrumbOptions <highcharts_gantt.utility_classes.breadcrumbs.BreadcrumbOptions>`
      :class:`Separator <highcharts_gantt.utility_classes.breadcrumbs.Separator>`
  * - :mod:`.utility_classes.buttons <highcharts_gantt.utility_classes.buttons>`
    - :class:`ExportingButtons <highcharts_gantt.utility_classes.buttons.ExportingButtons>`
      :class:`ContextButtonConfiguration <highcharts_gantt.utility_classes.buttons.ContextButtonConfiguration>`
      :class:`ButtonConfiguration <highcharts_gantt.utility_classes.buttons.ButtonConfiguration>`
      :class:`ButtonTheme <highcharts_gantt.utility_classes.buttons.ButtonTheme>`
  * - :mod:`.utility_classes.clusters <highcharts_gantt.utility_classes.clusters>`
    - :class:`ClusterOptions <highcharts_gantt.utility_classes.clusters.ClusterOptions>`
      :class:`VectorLayoutAlgorithm <highcharts_gantt.utility_classes.clusters.VectorLayoutAlgorithm>`
  * - :mod:`.utility_classes.data_grouping <highcharts_gantt.utility_classes.data_grouping>`
    - :class:`DataGroupingOptions <highcharts_gantt.utility_classes.data_grouping.DataGroupingOptions>`
  * - :mod:`.utility_classes.data_labels <highcharts_gantt.utility_classes.data_labels>`
    - :class:`DataLabel <highcharts_gantt.utility_classes.data_labels.DataLabel>`
      :class:`NodeDataLabel <highcharts_gantt.utility_classes.data_labels.NodeDataLabel>`
      :class:`Filter <highcharts_gantt.utility_classes.data_labels.Filter>`
  * - :mod:`.utility_classes.date_time_label_formats <highcharts_gantt.utility_classes.date_time_label_formats>`
    - :class:`DateTimeLabelFormats <highcharts_gantt.utility_classes.date_time_label_formats.DateTimeLabelFormats>`
  * - :mod:`.utility_classes.events <highcharts_gantt.utility_classes.events>`
    - :class:`ChartEvents <highcharts_gantt.utility_classes.events.ChartEvents>`
      :class:`BreadcrumbEvents <highcharts_gantt.utility_classes.events.BreadcrumbEvents>`
      :class:`NavigationEvents <highcharts_gantt.utility_classes.events.NavigationEvents>`
      :class:`PointEvents <highcharts_gantt.utility_classes.events.PointEvents>`
      :class:`SeriesEvents <highcharts_gantt.utility_classes.events.SeriesEvents>`
      :class:`ClusterEvents <highcharts_gantt.utility_classes.events.ClusterEvents>`
      :class:`AxisEvents <highcharts_gantt.utility_classes.events.AxisEvents>`
      :class:`MouseEvents <highcharts_gantt.utility_classes.events.MouseEvents>`
      :class:`RangeSelectorEvents <highcharts_gantt.utility_classes.events.RangeSelectorEvents>`
  * - :mod:`.utility_classes.gradients <highcharts_gantt.utility_classes.gradients>`
    - :class:`Gradient <highcharts_gantt.utility_classes.gradients.Gradient>`
      :class:`LinearGradient <highcharts_gantt.utility_classes.gradients.LinearGradient>`
      :class:`RadialGradient <highcharts_gantt.utility_classes.gradients.RadialGradient>`
  * - :mod:`.utility_classes.javascript_functions <highcharts_gantt.utility_classes.javascript_functions>`
    - :class:`CallbackFunction <highcharts_gantt.utility_classes.javascript_functions.CallbackFunction>`
      :class:`JavaScriptClass <highcharts_gantt.utility_classes.javascript_functions.JavaScriptClass>`
  * - :mod:`.utility_classes.jitter <highcharts_gantt.utility_classes.jitter>`
    - :class:`Jitter <highcharts_gantt.utility_classes.jitter.Jitter>`
  * - :mod:`.utility_classes.last_price <highcharts_gantt.utility_classes.last_price>`
    - :class:`LastPriceOptions <highcharts_gantt.utility_classes.last_price.LastPriceOptions>`
  * - :mod:`.utility_classes.line_styles <highcharts_gantt.utility_classes.line_styles>`
    - :class:`LineStylesWidth <highcharts_gantt.utility_classes.line_styles.LineStylesWidth>`
      :class:`LineStylesColorWidth <highcharts_gantt.utility_classes.line_styles.LineStylesColorWidth>`
      :class:`LineStylesColorWidthDash <highcharts_gantt.utility_classes.line_styles.LineStylesColorWidthDash>`
  * - :mod:`.utility_classes.markers <highcharts_gantt.utility_classes.markers>`
    - :class:`Marker <highcharts_gantt.utility_classes.markers.Marker>`
  * - :mod:`.utility_classes.menus <highcharts_gantt.utility_classes.menus>`
    - :class:`MenuObject <highcharts_gantt.utility_classes.menus.MenuObject>`
      :class:`MenuItem <highcharts_gantt.utility_classes.menus.MenuItem>`
  * - :mod:`.utility_classes.nodes <highcharts_gantt.utility_classes.nodes>`
    - :class:`NodeOptions <highcharts_gantt.utility_classes.nodes.NodeOptions>`
      :class:`DependencyWheelNodeOptions <highcharts_gantt.utility_classes.nodes.DependencyWheelNodeOptions>`
      :class:`OrganizationNodeOptions <highcharts_gantt.utility_classes.nodes.OrganizationNodeOptions>`
  * - :mod:`.utility_classes.partial_fill <highcharts_gantt.utility_classes.partial_fill>`
    - :class:`PartialFillOptions <highcharts_gantt.utility_classes.partial_fill.PartialFillOptions>`
  * - :mod:`.utility_classes.patterns <highcharts_gantt.utility_classes.patterns>`
    - :class:`Pattern <highcharts_gantt.utility_classes.patterns.Pattern>`
      :class:`PatternOptions <highcharts_gantt.utility_classes.patterns.PatternOptions>`
  * - :mod:`.utility_classes.position <highcharts_gantt.utility_classes.position>`
    - :class:`Position <highcharts_gantt.utility_classes.position.Position>`
  * - :mod:`.utility_classes.shadows <highcharts_gantt.utility_classes.shadows>`
    - :class:`ShadowOptions <highcharts_gantt.utility_classes.shadows.ShadowOptions>`
  * - :mod:`.utility_classes.states <highcharts_gantt.utility_classes.states>`
    - :class:`States <highcharts_gantt.utility_classes.states.States>`
      :class:`HoverState <highcharts_gantt.utility_classes.states.HoverState>`
      :class:`InactiveState <highcharts_gantt.utility_classes.states.InactiveState>`
      :class:`NormalState <highcharts_gantt.utility_classes.states.NormalState>`
      :class:`SelectState <highcharts_gantt.utility_classes.states.SelectState>`
  * - :mod:`.utility_classes.zones <highcharts_gantt.utility_classes.zones>`
    - :class:`Zone <highcharts_gantt.utility_classes.zones.Zone>`
      :class:`ClusterZone <highcharts_gantt.utility_classes.zones.ClusterZone>`

.. toctree::
  :hidden:
  :titlesonly:

  api/chart
  api/global_options/index
  api/headless_export
  api/highcharts
  api/options/index
  api/utility_classes/index

*********************
Library Internals
*********************

.. toctree::
  :hidden:

  Internal Reference <api/internals>

While most users will be interacting with the :ref:`Core Components <core_components>` of
**Highcharts Gantt for Python**, you may need (or choose to) work with various internals
of the library. If you're :doc:`contributing` to the library, then you will definitely
need to familiarize yourself with these internals.

.. list-table::
  :widths: 60 40
  :header-rows: 1

  * - Module
    - Classes / Functions
  * - :mod:`.metaclasses <highcharts_gantt.metaclasses>`
    - :class:`HighchartsMeta <highcharts_gantt.metaclasses.HighchartsMeta>`
      :class:`JavaScriptDict <highcharts_gantt.metaclasses.JavaScriptDict>`
  * - :mod:`.decorators <highcharts_gantt.decorators>`
    - :deco:`@class_sensitive() <highcharts_gantt.decorators.class_sensitive>`
      :func:`validate_types() <highcharts_gantt.decorators.validate_types>`
  * - :mod:`.js_literal_functions <highcharts_gantt.js_literal_functions>`
    - :func:`serialize_to_js_literal() <highcharts_gantt.js_literal_functions.serialize_to_js_literal>`
      :func:`attempt_variable_declaration() <highcharts_gantt.js_literal_functions.attempt_variable_declaration>`
      :func:`is_js_function_or_class() <highcharts_gantt.js_literal_functions.is_js_function_or_class>`
      :func:`get_js_literal() <highcharts_gantt.js_literal_functions.get_js_literal>`
      :func:`assemble_js_literal() <highcharts_gantt.js_literal_functions.assemble_js_literal>`
      :func:`convert_js_literal_to_python() <highcharts_gantt.js_literal_functions.convert_js_literal_to_python>`
      :func:`convert_js_property_to_python() <highcharts_gantt.js_literal_functions.convert_js_property_to_python>`
      :func:`convert_js_to_python() <highcharts_gantt.js_literal_functions.convert_js_to_python>`
      :func:`get_key_value_pairs() <highcharts_gantt.js_literal_functions.get_key_value_pairs>`
  * - :mod:`.monday <highcharts_gantt.monday>`
    - :func:`get_tasks() <highcharts_gantt.monday.get_tasks>`
      :func:`get_column_definitions() <highcharts_gantt.monday.get_column_definitions>`
      :func:`convert_item_to_task() <highcharts_gantt.monday.convert_item_to_task>`
      :func:`format_column() <highcharts_gantt.monday.format_column>`
      :func:`get_column_title() <highcharts_gantt.monday.get_column_title>`
      :func:`get_column_type() <highcharts_gantt.monday.get_column_type>`
      :func:`elevate_subtasks() <highcharts_gantt.monday.elevate_subtasks>`
      :func:`flatten_columns() <highcharts_gantt.monday.flatten_columns>`
  * - :mod:`.utility_functions <highcharts_gantt.utility_functions>`
    - :func:`mro_to_dict() <highcharts_gantt.utility_functions.mro_to_dict>`
      :func:`get_remaining_mro() <highcharts_gantt.utility_functions.get_remaining_mro>`
      :func:`mro__to_untrimmed_dict() <highcharts_gantt.utility_functions.mro__to_untrimmed_dict>`
      :func:`validate_color() <highcharts_gantt.utility_functions.validate_color>`
      :func:`to_camelCase() <highcharts_gantt.utility_functions.to_camelCase>`
      :func:`parse_csv() <highcharts_gantt.utility_functions.parse_csv>`
      :func:`parse_jira_issue() <highcharts_gantt.utility_functions.parse_jira_issue>`

.. target-notes::

.. include:: links.txt
