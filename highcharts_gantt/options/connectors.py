from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_gantt.options.plot_options.connectors import (
    ConnectorOptions as ConnectorBase
)


class ConnectorOptions(ConnectorBase):
    """**Highcharts Gantt for Python** allows you to define a connection between two
    points, with the connection represented as a line with optional markers for the
    start and end of that line. Multiple algorithms are available for calculating 
    how connecting lines should be drawn."""

    def __init__(self, **kwargs):
        self._algorithm_margin = None
        self._enabled = None
        self._radius = None
        
        self.algorithm_margin = kwargs.get('algorithm_margin', None)
        self.enabled = kwargs.get('enabled', None)
        self.radius = kwargs.get('radius', None)
        
        super().__init__(**kwargs)

    @property
    def algorithm_margin(self) -> Optional[int | float | Decimal]:
        """Determines the margin to use, in pixels, between the connector line and 
        obstacles encountered. Defaults to :obj:`None <python:None>`, which computes
        the margin automatically based on the size of the obstacles encountered.
        
        .. note::
        
          Not all pathfinder algorithms avoid obstacles, but the ones that do use this 
          margin value to determine how close lines can be to an obstacle.
          
        .. tip::
        
          To draw connecting lines close to existing points, set this to a low number. 
          For more space around existing points, set this number higher.
          
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._algorithm_margin

    @algorithm_margin.setter
    def algorithm_margin(self, value):
        self._algorithm_margin = validators.numeric(value, allow_empty = True)

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, enables the use of markers on connectors. Defaults to ``True``.
        
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enabled
    
    @enabled.setter
    def enabled(self, value):
        if value is None:
            self._enabled = None
        else:
            self._enabled = bool(value)
            
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
            
            'algorithm_margin': as_dict.get('algorithmMargin', None),
            'enabled': as_dict.get('enabled', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'algorithmMargin': self.algorithm_margin,
            'enabled': self.enabled,
        }
        
        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls) or {}
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
