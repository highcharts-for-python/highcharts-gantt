from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_gantt import constants, errors

from highcharts_gantt.decorators import class_sensitive
from highcharts_gantt.metaclasses import HighchartsMeta
from highcharts_gantt.utility_classes.markers import Marker


class ConnectorOptions(HighchartsMeta):
    """Configuration of the connector lines between objects within a series."""

    def __init__(self, **kwargs):
        self._dash_style = None
        self._end_marker = None
        self._line_color = None
        self._line_width = None
        self._marker = None
        self._radius = None
        self._start_marker = None

        self.dash_style = kwargs.get('dash_style', None)
        self.end_marker = kwargs.get('end_marker', None)
        self.line_color = kwargs.get('line_color', None)
        self.line_width = kwargs.get('line_width', None)
        self.marker = kwargs.get('marker', None)
        self.radius = kwargs.get('radius', None)
        self.start_marker = kwargs.get('start_marker', None)

    @property
    def dash_style(self) -> Optional[str]:
        """Name of the dash style to use for the lines. Defaults to ``Solid``.

        Accepts one of the following values:

          * 'Dash',
          * 'DashDot',
          * 'Dot',
          * 'LongDash',
          * 'LongDashDot',
          * 'LongDashDotDot',
          * 'ShortDash',
          * 'ShortDashDot',
          * 'ShortDashDotDot',
          * 'ShortDot',
          * 'Solid'

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._dash_style

    @dash_style.setter
    def dash_style(self, value):
        if not value:
            self._dash_style = None
        else:
            value = validators.string(value)
            if value not in constants.SUPPORTED_DASH_STYLE_VALUES:
                raise errors.HighchartsValueError(f'dash_style expects a '
                                                  f'recognized value, but received: '
                                                  f'{value}')
            self._dash_style = value

    @property
    def end_marker(self) -> Optional[Marker]:
        """Configuration of the marker to use at the end of the connector.

        .. note::

          If not :obj:`None <python:None>`, overrides the generic
          :meth:`.marker <highcharts_gantt.options.plot_options.connectors.Connector.marker>`
          property.

        :rtype: :class:`Marker <highcharts_gantt.utility_classes.markers.Marker>` or
          :obj:`None <python:None>`
        """
        return self._end_marker

    @end_marker.setter
    @class_sensitive(Marker)
    def end_marker(self, value):
        self._end_marker = value

    @property
    def line_color(self) -> Optional[str]:
        """The color of the connector line. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._line_color

    @line_color.setter
    def line_color(self, value):
        self._line_color = validators.string(value, allow_empty = True)

    @property
    def line_width(self) -> Optional[int | float | Decimal]:
        """The width of the connector line, in pixels. Defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._line_width

    @line_width.setter
    def line_width(self, value):
        self._line_width = validators.numeric(value,
                                              allow_empty = True,
                                              minimum = 0)

    @property
    def marker(self) -> Optional[Marker]:
        """Configuration of the markers to use at both the start and end of the connector.

        .. note::

          Will be overridden by both
          :meth:`.end_marker <highcharts_gantt.options.plot_options.connectors.Connector.end_marker>`
          and
          :meth:`.start_marker <highcharts_gantt.options.plot_options.connectors.Connector.start_marker>`
          if they are not :obj:`None <python:None>`

        :rtype: :class:`Marker <highcharts_gantt.utility_classes.markers.Marker>` or
          :obj:`None <python:None>`
        """
        return self._marker

    @marker.setter
    @class_sensitive(Marker)
    def marker(self, value):
        self._marker = value

    @property
    def radius(self) -> Optional[int | float | Decimal]:
        """The corner radius for the connector line.
        
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._radius
    
    @radius.setter
    def radius(self, value):
        self._radius = validators.numeric(value,
                                          allow_empty = True)

    @property
    def start_marker(self) -> Optional[Marker]:
        """Configuration of the marker to use at the start of the connector.

        .. note::

          If not :obj:`None <python:None>`, overrides the generic
          :meth:`.marker <highcharts_gantt.options.plot_options.connectors.Connector.marker>`
          property.

        :rtype: :class:`Marker <highcharts_gantt.utility_classes.markers.Marker>` or
          :obj:`None <python:None>`
        """
        return self._start_marker

    @start_marker.setter
    @class_sensitive(Marker)
    def start_marker(self, value):
        self._start_marker = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'dash_style': as_dict.get('dashStyle', None),
            'end_marker': as_dict.get('endMarker', None),
            'line_color': as_dict.get('lineColor', None),
            'line_width': as_dict.get('lineWidth', None),
            'marker': as_dict.get('marker', None),
            'radius': as_dict.get('radius', None),
            'start_marker': as_dict.get('startMarker', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'dashStyle': self.dash_style,
            'endMarker': self.end_marker,
            'lineColor': self.line_color,
            'lineWidth': self.line_width,
            'marker': self.marker,
            'radius': self.radius,
            'startMarker': self.start_marker,
        }

        return untrimmed
