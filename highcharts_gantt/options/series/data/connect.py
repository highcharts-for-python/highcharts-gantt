from typing import Optional

from validator_collection import validators

from highcharts_gantt.metaclasses import HighchartsMeta
from highcharts_gantt.options.plot_options.connectors import ConnectorOptions


class DataConnection(ConnectorOptions):
    """Configuration of the connection between two data points."""

    def __init__(self, **kwargs):
        self._to = None
        self._type = None

        self.to = kwargs.get('to', None)
        self.type = kwargs.get('type', None)

        super().__init__(**kwargs)

    @property
    def to(self) -> Optional[str]:
        """The ID of the data point to connect to. Defaults to :obj:`None <python:None>`

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._to

    @to.setter
    def to(self, value):
        self._to = validators.string(value, allow_empty = True)

    @property
    def type(self) -> Optional[str]:
        """Determines the pathfinder algorithm to use to find a connection between the
        data points. By default, accepts the following values:

          * ``'straight'`` which draws a straight line between the connecting points. Does
            *not* avoid other data points when drawing.
          * ``'simpleConnect'`` which draws a path between the two points using right
            angles only. Takes only the starting/ending points into account, and will
            *not* avoid other points.
          * ``'fastAvoid'`` which draws a path between the two points using right angles
            only. Will attempt to avoid other data points, but it priorities performance
            over accuracy. Best to use for less-dense datasets.

        .. note::

          It is possible to define your own custom pathfinder algorithm by using the
          :meth:`chart.add_pathfinder_algorithm() <highcharts_gantt.chart.add_pathfinder_algorithm>`
          method.

        .. warning::

          This method does not validate that the value supplied matches a defined
          algorithm name.

        Defaults to :obj:`None <python:None>`, which applies ``'straight'`` for most
        series types and ``'simpleConnect'`` for
        :class:`GanttSeries <highcharts_gantt.options.series.gantt.GanttSeries>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._type

    @type.setter
    def type(self, value):
        self._type = validators.variable_name(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'dash_style': as_dict.get('dashStyle', None),
            'end_marker': as_dict.get('endMarker', None),
            'line_color': as_dict.get('lineColor', None),
            'line_width': as_dict.get('lineWidth', None),
            'marker': as_dict.get('marker', None),
            'start_marker': as_dict.get('startMarker', None),

            'to': as_dict.get('to', None),
            'type': as_dict.get('type', None),

        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'to': self.to,
            'type': self.type,
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls) or {}
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
