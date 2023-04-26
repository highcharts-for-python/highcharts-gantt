################################################################
:mod:`.plot_options <highcharts_gantt.options.plot_options>`
################################################################

.. contents:: Module Contents
  :local:
  :depth: 3
  :backlinks: entry

.. toctree::
  :titlesonly:

  abands
  accessibility
  ad
  arcdiagram
  area
  aroon
  atr
  averages
  bar
  base
  bellcurve
  boxplot
  bubble
  bullet
  candlestick
  data_sorting
  dependencywheel
  disparity_index
  dmi
  drag_drop
  dumbbell
  flags
  funnel
  gantt
  gauge
  generic
  heatmap
  histogram
  hlc
  indicators
  item
  levels
  linear_regressions
  link
  momentum/index
  networkgraph
  organization
  oscillators/index
  packedbubble
  pareto
  pictorial
  pie
  pivot_points
  points
  polygon
  price_envelopes
  psar
  pyramid
  sankey
  scatter
  series
  sonification
  spline
  sunburst
  timeline
  treegraph
  treemap
  vbp
  vector
  venn
  wordcloud
  zigzag

-------------------------

.. module:: highcharts_gantt.options.plot_options

********************************************************************************************************************
class: :class:`PlotOptions <highcharts_gantt.options.plot_options.PlotOptions>`
********************************************************************************************************************

.. autoclass:: PlotOptions
  :members:
  :inherited-members:

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: PlotOptions
      :top-classes: highcharts_gantt.metaclasses.HighchartsMeta, highcharts_core.metaclasses.HighchartsMeta
      :parts: -1

  |

--------------

***************************
Sub-components
***************************

.. list-table::
  :widths: 60 40
  :header-rows: 1

  * - Module
    - Classes / Functions
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
