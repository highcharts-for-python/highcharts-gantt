from typing import Optional, List

from validator_collection import checkers, validators

from highcharts_stock.options.series.data.bar import (BarData,
                                                      BarDataCollection,
                                                      WaterfallData,
                                                      WaterfallDataCollection,
                                                      WindBarbData,
                                                      WindBarbDataCollection,
                                                      XRangeData as XRangeDataBase,
                                                      XRangeDataCollection as XRangeDataCollectionBase)

from highcharts_gantt.options.series.data.connect import DataConnection
from highcharts_gantt.decorators import validate_types


class XRangeData(XRangeDataBase):
    """Variant of :class:`CartesianData` which is used for data points in an X-Range
    series."""

    def __init__(self, **kwargs):
        self._connect = None

        self.connect = kwargs.get('connect', None)

        super().__init__(**kwargs)

    @property
    def connect(self) -> Optional[DataConnection | str | List[DataConnection | str]]:
        """Connects the data point to another data point.

        Accepts either a :class:`str <python:str>` which corresponds to the ID of a
        different data point, a
        :class:`DataConnection <highcharts_gantt.options.series.data.connect.DataConnection>`
        object configuring the connection, an array of either, or
        :obj:`None <python:None>`. Defaults to :obj:`None <python:None>`

        :rtype: :class:`str <python:str>` or
          :class:`DataConnection <highcharts_gantt.options.series.data.connect.DataConnection>`
          or an iterable of :class:`str <python:str>` or
          :class:`DataConnection <highcharts_gantt.options.series.data.connect.DataConnection>`
          or :obj:`None <python:None>`
        """
        return self._connect

    @connect.setter
    def connect(self, value):
        if not value:
            self._connect = None
        else:
            if not checkers.is_iterable(value, forbid_literals = (str, bytes, dict)):
                try:
                    value = validators.string(value)
                except (ValueError, TypeError):
                    value = validate_types(value, DataConnection)

                self._connect = value
            else:
                processed_value = []
                for item in value:
                    try:
                        item = validators.string(item)
                    except (ValueError, TypeError):
                        item = validate_types(item, DataConnection)
                    processed_value.append(item)

                self._connect = [x for x in processed_value]

    @classmethod
    def from_ndarray(cls, value):
        """Creates a collection of data points from a `NumPy <https://numpy.org>`__ 
        :class:`ndarray <numpy:ndarray>` instance.
        
        :returns: A collection of data point values.
        :rtype: :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
        """
        return XRangeDataCollection.from_ndarray(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        """Convenience method which returns the keyword arguments used to initialize the
        class from a Highcharts Javascript-compatible :class:`dict <python:dict>` object.

        :param as_dict: The HighCharts JS compatible :class:`dict <python:dict>`
          representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :returns: The keyword arguments that would be used to initialize an instance.
        :rtype: :class:`dict <python:dict>`

        """
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'class_name': as_dict.get('className', None),
            'color': as_dict.get('color', None),
            'color_index': as_dict.get('colorIndex', None),
            'custom': as_dict.get('custom', None),
            'description': as_dict.get('description', None),
            'events': as_dict.get('events', None),
            'id': as_dict.get('id', None),
            'label_rank': as_dict.get('labelRank',
                                      None) or as_dict.get('labelrank',
                                                           None),
            'name': as_dict.get('name', None),
            'selected': as_dict.get('selected', None),

            'data_labels': as_dict.get('dataLabels', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'drilldown': as_dict.get('drilldown', None),
            'marker': as_dict.get('marker', None),
            'x': as_dict.get('x', None),
            'y': as_dict.get('y', None),

            'partial_fill': as_dict.get('partialFill', None),
            'x2': as_dict.get('x2', None),

            'connect': as_dict.get('connect', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'connect': self.connect
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls) or {}
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class XRangeDataCollection(XRangeDataCollectionBase):
    """A collection of :class:`XRangeData` objects.

    .. note::
    
      When serializing to JS literals, if possible, the collection is serialized to a primitive
      array to boost performance within Python *and* JavaScript. However, this may not always be
      possible if data points have non-array-compliant properties configured (e.g. adjusting their 
      style, names, identifiers, etc.). If serializing to a primitive array is not possible, the
      results are serialized as JS literal objects.

    """

    @classmethod
    def _get_data_point_class(cls):
        """The Python class to use as the underlying data point within the Collection.
        
        :rtype: class object
        """
        return XRangeData
