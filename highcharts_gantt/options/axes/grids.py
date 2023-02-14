from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core.options.axes.x_axis import XAxis as XAxisBase
from highcharts_core.options.axes.y_axis import YAxis as YAxisBase

from highcharts_gantt.decorators import validate_types
from highcharts_gantt.metaclasses import HighchartsMeta


class GridOptions(HighchartsMeta):
    """Grid options for the axis labels."""

    def __init__(self, **kwargs):
        self._border_color = None
        self._border_width = None
        self._cell_height = None
        self._columns = None
        self._enabled = None

        self.border_color = kwargs.get('border_color', None)
        self.border_width = kwargs.get('border_width', None)
        self.cell_height = kwargs.get('cell_height', None)
        self.columns = kwargs.get('columns', None)
        self.enabled = kwargs.get('enabled', None)

    @property
    def border_color(self) -> Optional[str]:
        """Border color for the label grid lines. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        self._border_color = validators.string(value, allow_empty = True)

    @property
    def border_width(self) -> Optional[int | float | Decimal]:
        """The border width to apply to label grid lines. Defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_width

    @border_width.setter
    def border_width(self, value):
        self._border_width = validators.numeric(value,
                                                allow_empty = True,
                                                minimum = 0)

    @property
    def cell_height(self) -> Optional[int | float | Decimal]:
        """The cell height for grid axis labels. Defaults to :obj:`None <python:None>`,
        which calculates the cell height automatically based on the font size.

        .. note::

          This setting will be ignored for vertical axes.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._cell_height

    @cell_height.setter
    def cell_height(self, value):
        self._cell_height = validators.numeric(value,
                                               allow_empty = True,
                                               minimum = 0)

    @property
    def columns(self) -> Optional[XAxisBase | YAxisBase]:
        """Specific options for each column (or row for horizontal axes) in the grid. Each
        extra column/row is its own axis, and the axis options can be set here. Defaults
        to :obj:`None <python:None>`.

        :rtype: :class:`XAxis <highcharts_gantt.options.axes.x_axis.XAxis` or
          :class:`YAxis <highcharts_gantt.options.axes.y_axis.YAxis` or
          :obj:`None <python:None>`
        """
        return self._columns

    @columns.setter
    def columns(self, value):
        if not value:
            self._columns = None
        else:
            try:
                value = validate_types(value, YAxisBase)
            except (ValueError, TypeError):
                value = validate_types(value, XAxisBase)

            self._columns = value

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, enables the grid on axis labels. Defaults to ``True``.

        :rtype: :class:`bool <python:bool>`
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
            'border_color': as_dict.get('borderColor', None),
            'border_width': as_dict.get('borderWidth', None),
            'cell_height': as_dict.get('cellHeight', None),
            'columns': as_dict.get('columns', None),
            'enabled': as_dict.get('enabled', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'borderColor': self.border_color,
            'borderWidth': self.border_width,
            'cellHeight': self.cell_height,
            'columns': self.columns,
            'enabled': self.enabled,
        }

        return untrimmed
