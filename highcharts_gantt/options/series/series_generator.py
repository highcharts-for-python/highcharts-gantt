from typing import Optional

import json

from validator_collection import validators, checkers

from highcharts_gantt import errors

from highcharts_gantt.options.series.base import SeriesBase
from highcharts_gantt.options.series.arcdiagram import ArcDiagramSeries
from highcharts_gantt.options.series.area import AreaSeries
from highcharts_gantt.options.series.area import AreaRangeSeries
from highcharts_gantt.options.series.area import AreaSplineSeries
from highcharts_gantt.options.series.area import AreaSplineRangeSeries
from highcharts_gantt.options.series.area import LineSeries
from highcharts_gantt.options.series.area import StreamGraphSeries
from highcharts_gantt.options.series.bar import BarSeries
from highcharts_gantt.options.series.bar import ColumnSeries
from highcharts_gantt.options.series.bar import ColumnPyramidSeries
from highcharts_gantt.options.series.bar import ColumnRangeSeries
from highcharts_gantt.options.series.bar import CylinderSeries
from highcharts_gantt.options.series.bar import VariwideSeries
from highcharts_gantt.options.series.bar import WaterfallSeries
from highcharts_gantt.options.series.bar import WindBarbSeries
from highcharts_gantt.options.series.bar import XRangeSeries
from highcharts_gantt.options.series.bellcurve import BellCurveSeries
from highcharts_gantt.options.series.boxplot import BoxPlotSeries
from highcharts_gantt.options.series.boxplot import ErrorBarSeries
from highcharts_gantt.options.series.bubble import BubbleSeries
from highcharts_gantt.options.series.bullet import BulletSeries
from highcharts_gantt.options.series.dependencywheel import DependencyWheelSeries
from highcharts_gantt.options.series.dumbbell import DumbbellSeries
from highcharts_gantt.options.series.dumbbell import LollipopSeries
from highcharts_gantt.options.series.funnel import FunnelSeries
from highcharts_gantt.options.series.funnel import Funnel3DSeries
from highcharts_gantt.options.series.gauge import GaugeSeries
from highcharts_gantt.options.series.gauge import SolidGaugeSeries
from highcharts_gantt.options.series.heatmap import HeatmapSeries
from highcharts_gantt.options.series.heatmap import TilemapSeries
from highcharts_gantt.options.series.histogram import HistogramSeries
from highcharts_gantt.options.series.item import ItemSeries
from highcharts_gantt.options.series.networkgraph import NetworkGraphSeries
from highcharts_gantt.options.series.organization import OrganizationSeries
from highcharts_gantt.options.series.packedbubble import PackedBubbleSeries
from highcharts_gantt.options.series.pareto import ParetoSeries
from highcharts_gantt.options.series.pictorial import PictorialSeries
from highcharts_gantt.options.series.pie import PieSeries
from highcharts_gantt.options.series.pie import VariablePieSeries
from highcharts_gantt.options.series.polygon import PolygonSeries
from highcharts_gantt.options.series.pyramid import PyramidSeries
from highcharts_gantt.options.series.pyramid import Pyramid3DSeries
from highcharts_gantt.options.series.sankey import SankeySeries
from highcharts_gantt.options.series.scatter import ScatterSeries
from highcharts_gantt.options.series.scatter import Scatter3DSeries
from highcharts_gantt.options.series.spline import SplineSeries
from highcharts_gantt.options.series.sunburst import SunburstSeries
from highcharts_gantt.options.series.timeline import TimelineSeries
from highcharts_gantt.options.series.treegraph import TreegraphSeries
from highcharts_gantt.options.series.treemap import TreemapSeries
from highcharts_gantt.options.series.vector import VectorSeries
from highcharts_gantt.options.series.venn import VennSeries
from highcharts_gantt.options.series.wordcloud import WordcloudSeries

from highcharts_gantt.options.series.gantt import GanttSeries


SERIES_CLASSES = {
    'arcdiagram': ArcDiagramSeries,
    'areaseries': AreaSeries,
    'arearange': AreaRangeSeries,
    'areaspline': AreaSplineSeries,
    'areasplinerange': AreaSplineRangeSeries,
    'line': LineSeries,
    'streamgraph': StreamGraphSeries,
    'bar': BarSeries,
    'column': ColumnSeries,
    'columnpyramid': ColumnPyramidSeries,
    'columnrange': ColumnRangeSeries,
    'cylinder': CylinderSeries,
    'variwide': VariwideSeries,
    'waterfall': WaterfallSeries,
    'windbarb': WindBarbSeries,
    'xrange': XRangeSeries,
    'bellcurve': BellCurveSeries,
    'boxplot': BoxPlotSeries,
    'errorbar': ErrorBarSeries,
    'bubble': BubbleSeries,
    'bullet': BulletSeries,
    'dependencywheel': DependencyWheelSeries,
    'dumbbell': DumbbellSeries,
    'lollipop': LollipopSeries,
    'funnel': FunnelSeries,
    'funnel3d': Funnel3DSeries,
    'gauge': GaugeSeries,
    'solidgauge': SolidGaugeSeries,
    'heatmap': HeatmapSeries,
    'tilemap': TilemapSeries,
    'histogram': HistogramSeries,
    'item': ItemSeries,
    'networkgraph': NetworkGraphSeries,
    'organization': OrganizationSeries,
    'packedbubble': PackedBubbleSeries,
    'pareto': ParetoSeries,
    'pictorial': PictorialSeries,
    'pie': PieSeries,
    'variablepie': VariablePieSeries,
    'polygon': PolygonSeries,
    'pyramid': PyramidSeries,
    'pyramid3d': Pyramid3DSeries,
    'sankey': SankeySeries,
    'scatter': ScatterSeries,
    'scatter3d': Scatter3DSeries,
    'spline': SplineSeries,
    'sunburst': SunburstSeries,
    'timeline': TimelineSeries,
    'treegraph': TreegraphSeries,
    'treemap': TreemapSeries,
    'vector': VectorSeries,
    'venn': VennSeries,
    'wordcloud': WordcloudSeries,

    # Highcharts Gantt Series Types
    'gantt': GanttSeries,
}

GANTT_SERIES_LIST = [
    # Highcharts Gantt Series Types
    'gantt'
]


def create_series_obj(value,
                      default_type = None) -> Optional[SeriesBase]:
    """Create an instance descended from
    :class:`SeriesBase <highcharts_gantt.options.series.base.SeriesBase>` or
    :class:`IndicatorSeriesBase <highcharts_gantt.options.series.base.IndicatorSeriesBase>`.

    :param value: The input that should be de-serialized to a
      :class:`SeriesBase <highcharts_gantt.options.series.base.SeriesBase>` or
      :class:`IndicatorSeriesBase <highcharts_gantt.options.series.base.IndicatorSeriesBase>`
      instance. Expected to be either a
      :class:`SeriesBase <highcharts_gantt.options.series.base.SeriesBase>` or
      :class:`IndicatorSeriesBase <highcharts_gantt.options.series.base.IndicatorSeriesBase>`
      instance, a :class:`dict <python:dict>`, or a JSON :class:`str <python:str>`.

    :param default_type: The default series type to apply if not specified in
      ``value``. Defaults to :obj:`None <python:None>`
    :type default_type: :class:`str <python:str>` or :obj:`None <python:None>`

    :returns: A :class:`SeriesBase <highcharts_gantt.options.series.base.SeriesBase>`
      (descendant) instance or
      :class:`IndicatorSeriesBase <highcharts_gantt.options.series.base.IndicatorSeriesBase>`
      (descendant) instance
    :rtype: :class:`SeriesBase <highcharts_gantt.options.series.base.SeriesBase>` or
      :class:`IndicatorSeriesBase <highcharts_gantt.options.series.base.IndicatorSeriesBase>`
      or :obj:`None <python:None>`
    """
    if not value:
        return None

    if isinstance(value, (SeriesBase)):
        return value

    if isinstance(value, dict):
        type_ = value.get('type', default_type)
        if not type_:
            raise errors.HighchartsValueError('To instantiate a Series, the "type" must '
                                              'be provided. No "type" key was found.')
        cls = SERIES_CLASSES.get(type_, default_type)
        if not cls:
            raise errors.HighchartsValueError(f'create_series_obj expects a value with '
                                              f'a recognized "type". However, received a '
                                              f'"type" value that was not recognized: '
                                              f'{type_}')

        instance = cls.from_dict(value)
    elif isinstance(value, str):
        if 'data:' in value:
            try:
                preliminary = SeriesBase.from_js_literal(value)
                type_ = preliminary.type
            except errors.HighchartsParseError:
                preliminary_as_dict = json.loads(value)

                type_ = preliminary_as_dict.get('type', default_type)
        else:
            preliminary_as_dict = json.loads(value)
            type_ = preliminary_as_dict.get('type', default_type)

        if not type_:
            raise errors.HighchartsValueError('To instantiate a Series, the "type" must '
                                              'be provided. No "type" key was found.')
        cls = SERIES_CLASSES.get(type_, default_type)
        if not cls:
            raise errors.HighchartsValueError(f'create_series_obj expects a value with '
                                              f'a recognized "type". However, received a '
                                              f'"type" value that was not recognized: '
                                              f'{type_}')

        try:
            instance = cls.from_js_literal(value)
        except errors.HighchartsParseError:
            instance = cls.from_json(value)

    return instance
