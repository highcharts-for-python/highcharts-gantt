from typing import Optional, List
from collections import UserDict

from validator_collection import validators, checkers

from highcharts_stock.chart import Chart as ChartBase

from highcharts_gantt import errors, utility_functions
from highcharts_gantt.options import (HighchartsOptions, 
                                      HighchartsStockOptions,
                                      HighchartsGanttOptions)
from highcharts_gantt.decorators import validate_types
from highcharts_gantt.js_literal_functions import serialize_to_js_literal
from highcharts_gantt.headless_export import ExportServer
from highcharts_gantt.options.series.series_generator import (create_series_obj,
                                                              SERIES_CLASSES,
                                                              GANTT_SERIES_LIST)
from highcharts_gantt.global_options.shared_options import (SharedGanttOptions, 
                                                            SharedStockOptions, 
                                                            SharedOptions)
from highcharts_gantt.options.chart import ChartOptions


class Chart(ChartBase):
    """Python representation of a Highcharts ``Chart`` object."""

    def __init__(self, **kwargs):
        self._is_gantt_chart = None

        self.is_gantt_chart = kwargs.get('is_gantt_chart', False)

        super().__init__(**kwargs)

    def _jupyter_javascript(self, 
                            global_options = None, 
                            container = None,
                            random_slug = None,
                            retries = 3,
                            interval = 1000):
        """Return the JavaScript code which Jupyter Labs will need to render the chart.

        :param global_options: The :term:`shared options` to use when rendering the chart.
          Defaults to :obj:`None <python:None>`
        :type global_options: :class:`SharedOptions <highcharts_stock.global_options.shared_options.SharedOptions>`
          or :obj:`None <python:None>`
          
        :param container: The ID to apply to the HTML container when rendered in Jupyter Labs. Defaults to
          :obj:`None <python:None>`, which applies the :meth:`.container <highcharts_core.chart.Chart.container>` 
          property if set, and ``'highcharts_target_div'`` if not set.
        :type container: :class:`str <python:str>` or :obj:`None <python:None>`

        :param random_slug: The random sequence of characters to append to the container name to ensure uniqueness.
          Defaults to :obj:`None <python:None>`
        :type random_slug: :class:`str <python:str>` or :obj:`None <python:None>`
        
        :param retries: The number of times to retry rendering the chart. Used to avoid race conditions with the 
          Highcharts script. Defaults to 3.
        :type retries: :class:`int <python:int>`
        
        :param interval: The number of milliseconds to wait between retrying rendering the chart. Defaults to 1000 (1 
          seocnd).
        :type interval: :class:`int <python:int>`

        :rtype: :class:`str <python:str>`
        """
        original_container = self.container
        new_container = container or self.container or 'highcharts_target_div'
        if not random_slug:
            self.container = new_container
        else:
            self.container = f'{new_container}_{random_slug}'
        
        if global_options is not None:
            global_options = validate_types(global_options,
                                            types = (SharedGanttOptions, SharedStockOptions, SharedOptions))

        js_str = ''
        js_str += utility_functions.get_retryHighcharts()

        if global_options:
            js_str += '\n' + utility_functions.prep_js_for_jupyter(global_options.to_js_literal()) + '\n'

        js_str += utility_functions.prep_js_for_jupyter(self.to_js_literal(),
                                                        container = self.container,
                                                        random_slug = random_slug,
                                                        retries = retries,
                                                        interval = interval)

        self.container = original_container

        return js_str

    def get_required_modules(self, include_extension = False) -> List[str]:
        """Return the list of URLs from which the Highcharts JavaScript modules
        needed to render the chart can be retrieved.
        
        :param include_extension: if ``True``, will return script names with the 
          ``'.js'`` extension included. Defaults to ``False``.
        :type include_extension: :class:`bool <python:bool>`

        :rtype: :class:`list <python:list>`
        """
        initial_scripts = ['highcharts']
        if self.is_gantt_chart:
            initial_scripts.extend(['gantt/modules/gantt'])
        has_stock_tools = hasattr(self.options, 'stock_tools') and self.options.stock_tools
        if self.is_stock_chart or has_stock_tools:
            initial_scripts.append('modules/stock')

        scripts = self._process_required_modules(initial_scripts, include_extension)

        return scripts

    def _repr_html_(self):
        """Produce the HTML representation of the chart.

        .. note::

          Currently includes *all* `Highcharts JS <https://www.highcharts.com/>`__ or
          `Highcharts Gantt <https://www.highcharts.com/products/gantt/>`__ modules
          in the HTML. This issue will be addressed when roadmap issue :issue:`2` is
          released.

        :returns: The HTML representation of the chart.
        :rtype: :class:`str <python:str>`
        """
        if self.options.chart:
            height = self.options.chart.height or 400
        else:
            height = 400

        container_str = f"""<div id=\"{self.container}\" style=\"width:100%; height:{height};\"></div>\n"""
        as_str = self.to_js_literal()
        script_str = '<script>\n' + as_str + '\n</script>'

        html_str = container_str + script_str

        return html_str

    @property
    def is_gantt_chart(self) -> bool:
        """If ``True``, indicates that the chart should be rendered as a
        `Highcharts Gantt <https://www.highcharts.com/products/gantt/>`__ chart. If
        ``False``, the chart will be rendered using the standard
        `Highcharts JS <https://www.highcharts.com/products/highcharts/>`__ constructor.
        Defaults to ``False``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._is_gantt_chart

    @is_gantt_chart.setter
    def is_gantt_chart(self, value):
        self._is_gantt_chart = bool(value)

    @property
    def options(self) -> Optional[HighchartsOptions | HighchartsGanttOptions | HighchartsStockOptions]:
        """The Python representation of the
        `Highcharts Gantt <https://www.highcharts.com/products/gantt/>`__
        ``options`` `configuration object <https://api.highcharts.com/gantt/>`_
        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`HighchartsOptions` or :class:`HighchartsGanttOptions` or
          :obj:`None <python:None>`
        """
        return self._options

    @options.setter
    def options(self, value):
        if not value:
            self._options = None
        elif self.is_gantt_chart:
            self._options = validate_types(value, HighchartsGanttOptions)
            self.is_gantt_chart = True
        else:
            if checkers.is_type(value, 'HighchartsGanttOptions'):
                self._options = value
                self.is_gantt_chart = True
            elif checkers.is_type(value, 'HighchartsOptions'):
                self._options = value
            elif ('navigator' in value
                  or 'range_selector' in value
                  or 'rangeSelector' in value
                  or 'connectors' in value):
                self._options = validate_types(value, HighchartsGanttOptions)
                self.is_gantt_chart = True
            else:
                self._options = validate_types(value, HighchartsOptions)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'callback': as_dict.get('callback', None),
            'container': as_dict.get('container', None) or as_dict.get('renderTo', None),
            'options': as_dict.get('options', None) or as_dict.get('userOptions', None),
            'variable_name': as_dict.get('variable_name',
                                         None) or as_dict.get('variableName', None),

            'is_stock_chart': as_dict.get('is_stock_chart',
                                          None) or as_dict.get('isStockChart', False),
            'is_gantt_chart': as_dict.get('is_gantt_chart',
                                          None) or as_dict.get('isGanttChart', False)
        }

        return kwargs

    def to_js_literal(self,
                      filename = None,
                      encoding = 'utf-8',
                      careful_validation = False) -> Optional[str]:
        """Return the object represented as a :class:`str <python:str>` containing the
        JavaScript object literal.

        :param filename: The name of a file to which the JavaScript object literal should
          be persisted. Defaults to :obj:`None <python:None>`
        :type filename: Path-like

        :param encoding: The character encoding to apply to the resulting object. Defaults
          to ``'utf-8'``.
        :type encoding: :class:`str <python:str>`

        :param careful_validation: if ``True``, will carefully validate JavaScript values
          along the way using the
          `esprima-python <https://github.com/Kronuz/esprima-python>`__ library. Defaults
          to ``False``.
        
          .. warning::
        
            Setting this value to ``True`` will significantly degrade serialization
            performance, though it may prove useful for debugging purposes.

        :type careful_validation: :class:`bool <python:bool>`

        .. note::

          If :meth:`variable_name <Chart.variable_name>` is set, will render a string as
          a new JavaScript instance invocation in the (pseudo-code) form:

          .. code-block:: javascript

            new VARIABLE_NAME = new Chart(...);

          If :meth:`variable_name <Chart.variable_name>` is not set, will simply return
          the ``new Chart(...)`` portion in the string.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        if filename:
            filename = validators.path(filename)

        untrimmed = self._to_untrimmed_dict()
        as_dict = {}
        for key in untrimmed:
            item = untrimmed[key]
            serialized = serialize_to_js_literal(item,
                                                 encoding = encoding,
                                                 careful_validation = careful_validation)
            if serialized is not None:
                as_dict[key] = serialized

        signature_elements = 0

        container_as_str = ''
        if self.container:
            container_as_str = f"""'{self.container}'"""
        else:
            container_as_str = """null"""
        signature_elements += 1

        options_as_str = ''
        if self.options:
            options_as_str = self.options.to_js_literal(encoding = encoding,
                                                        careful_validation = careful_validation)
            options_as_str = f"""{options_as_str}"""
        else:
            options_as_str = """{}"""
        signature_elements += 1

        callback_as_str = ''
        if self.callback:
            callback_as_str = self.callback.to_js_literal(encoding = encoding,
                                                          careful_validation = careful_validation)
            callback_as_str = f"""{callback_as_str}"""
            signature_elements += 1

        signature = """Highcharts.chart("""
        if self.is_gantt_chart:
            signature = """Highcharts.ganttChart("""
        elif self.is_stock_chart:
            signature = """Highcharts.stockChart("""
        if container_as_str:
            signature += container_as_str
            if signature_elements > 1:
                signature += ',\n'
        if options_as_str:
            signature += options_as_str
            if signature_elements > 1:
                signature += ',\n'
        if callback_as_str:
            signature += callback_as_str
        signature += ');'

        constructor_prefix = ''
        if self.variable_name:
            constructor_prefix = f'var {self.variable_name} = '

        as_str = constructor_prefix + signature

        prefix = """document.addEventListener('DOMContentLoaded', function() {\n"""
        suffix = """});"""

        as_str = prefix + as_str + '\n' + suffix

        if filename:
            with open(filename, 'w', encoding = encoding) as file_:
                file_.write(as_str)

        return as_str

    def download_chart(self,
                       format_ = 'png',
                       scale = 1,
                       width = None,
                       filename = None,
                       auth_user = None,
                       auth_password = None,
                       timeout = 0.5,
                       server_instance = None,
                       **kwargs):
        """Export a downloaded form of the chart using a Highcharts :term:`Export Server`.

        :param filename: The name of the file where the exported chart should (optionally)
          be persisted. Defaults to :obj:`None <python:None>`.
        :type filename: Path-like or :obj:`None <python:None>`

        :param auth_user: The username to use to authenticate against the
          Export Server, using :term:`basic authentication`. Defaults to
          :obj:`None <python:None>`.
        :type auth_user: :class:`str <python:str>` or :obj:`None <python:None>`

        :param auth_password: The password to use to authenticate against the Export
          Server (using :term:`basic authentication`). Defaults to
          :obj:`None <python:None>`.
        :type auth_password: :class:`str <python:str>` or :obj:`None <python:None>`

        :param timeout: The number of seconds to wait before issuing a timeout error.
          The timeout check is passed if bytes have been received on the socket in less
          than the ``timeout`` value. Defaults to ``0.5``.
        :type timeout: numeric or :obj:`None <python:None>`

        :param server_instance: Provide an already-configured :class:`ExportServer`
          instance to use to programmatically produce the exported chart. Defaults to
          :obj:`None <python:None>`, which causes Highcharts for Python to instantiate
          a new :class:`ExportServer` instance.
        :type server_instance: :class:`ExportServer` or :obj:`None <python:None>`

        .. note::

          All other keyword arguments are as per the :class:`ExportServer` constructor.

        :returns: The exported chart image, either as a :class:`bytes <python:bytes>`
          binary object or as a base-64 encoded string (depending on the ``use_base64``
          keyword argument).
        :rtype: :class:`bytes <python:bytes>` or :class:`str <python:str>`
        """
        constructor = 'Chart'

        if not server_instance:
            return ExportServer.get_chart(filename = filename,
                                          auth_user = auth_user,
                                          auth_password = auth_password,
                                          timeout = timeout,
                                          options = self.options,
                                          constructor = constructor,
                                          scale = scale,
                                          width = width,
                                          format_ = format_,
                                          **kwargs)

        if not isinstance(server_instance, ExportServer):
            raise errors.HighchartsValueError(f'server_instance is expected to be an '
                                              f'ExportServer instance. Was: '
                                              f'{server_instance.__class__.__name__}')

        return server_instance.request_chart(filename = filename,
                                             auth_user = auth_user,
                                             auth_password = auth_password,
                                             timeout = timeout,
                                             options = self.options,
                                             constructor = constructor,
                                             format_ = format_,
                                             **kwargs)

    def add_series(self, *series):
        """Adds ``series`` to the
        :meth:`Chart.options.series <highcharts_core.options.HighchartsOptions.series>`
        property.

        :param series: One or more :term:`series` instances (descended from
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`) or an
          instance (e.g. :class:`dict <python:dict>`, :class:`str <python:str>`, etc.)
          coercable to one
        :type series: one or more
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`
          or coercable

        """
        new_series = []
        for item in series:
            item_series = create_series_obj(item)
            new_series.append(item_series)

        if self.options and self.options.series:
            existing_series = [x for x in self.options.series]
        elif self.options:
            existing_series = []
        else:
            existing_series = []
            if self.is_gantt_chart:
                self.options = HighchartsGanttOptions()
            else:
                self.options = HighchartsOptions()

        updated_series = existing_series + new_series

        self.options.series = updated_series

    @classmethod
    def from_array(cls,
                   value,
                   series_type = 'line',
                   series_kwargs = None,
                   options_kwargs = None,
                   chart_kwargs = None,
                   is_gantt_chart = False):
        """Create a :class:`Chart <highcharts_core.chart.Chart>` instance with
        one series populated from the array contained in ``value``.
        
        .. seealso::

          The specific structure of the expected array is highly dependent on the type of data
          point that the series needs, which itself is dependent on the series type itself.

          Please review the detailed :ref:`series documentation <series_documentation>` for
          series type-specific details of relevant array structures.

        :param value: The array to use to populate the series data.
        :type value: iterable
        
        :param series_type: Indicates the series type that should be created from the array
          data. Defaults to ``'line'``.
        :type series_type: :class:`str <python:str>`
        
        :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the series instance. Defaults
          to :obj:`None <python:None>`.

          .. warning::

            If ``series_kwargs`` contains a ``data`` key, its value will be *overwritten*.
            The ``data`` value will be created from ``df`` instead.

        :type series_kwargs: :class:`dict <python:dict>`

        :param options_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`HighchartsOptions`
          instance. Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``options_kwargs`` contains a ``series`` key, the ``series`` value will be
            *overwritten*. The ``series`` value will be created from the data in ``df``.

        :type options_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param chart_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`Chart` instance.
          Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``chart_kwargs`` contains an ``options`` key, ``options`` will be
            *overwritten*. The ``options`` value will be created from the
            ``options_kwargs`` and the data in ``df`` instead.

        :type chart_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param is_gantt_chart: if ``True``, enforces the use of 
          :class:`HighchartsGanttOptions <highcharts_stock.options.HighchartsGanttOptions>`.
          If ``False``, applies 
          :class:`HighchartsOptions <highcharts_stock.options.HighchartsOptions>`.
          Defaults to ``False``.

          .. note::

            The value given to this argument will override any values specified in
            ``chart_kwargs``.

        :type is_gantt_chart: :class:`bool <python:bool>`
        
        :returns: A :class:`Chart <highcharts_core.chart.Chart>` instance with its
          data populated from the data in ``value``.
        :rtype: :class:`Chart <highcharts_core.chart.Chart>`
        
        """
        series_type = validators.string(series_type, allow_empty = False)
        series_type = series_type.lower()
        if series_type not in SERIES_CLASSES:
            raise errors.HighchartsValueError(f'series_type expects a valid Highcharts '
                                              f'series type. Received: {series_type}')

        series_kwargs = validators.dict(series_kwargs, allow_empty = True) or {}
        options_kwargs = validators.dict(options_kwargs, allow_empty = True) or {}
        chart_kwargs = validators.dict(chart_kwargs, allow_empty = True) or {}

        series_cls = SERIES_CLASSES.get(series_type, None)

        series = series_cls.from_array(value, series_kwargs = series_kwargs)

        options_kwargs['series'] = [series]
        chart_kwargs['is_gantt_chart'] = is_gantt_chart

        if is_gantt_chart:
            options = HighchartsGanttOptions(**options_kwargs)
        else:
            options = HighchartsOptions(**options_kwargs)

        instance = cls(**chart_kwargs)
        instance.options = options

        return instance

    @classmethod
    def from_series(cls, *series, kwargs = None):
        """Creates a new :class:`Chart <highcharts_core.chart.Chart>` instance populated
        with ``series``.

        :param series: One or more :term:`series` instances (descended from
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`) or an
          instance (e.g. :class:`dict <python:dict>`, :class:`str <python:str>`, etc.)
          coercable to one
        :type series: one or more
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`
          or
          :class:`IndicatorSeriesBase <highcharts_gantt.options.series.base.IndicatorSeriesBase>`
          coercable

        :param kwargs: Other properties to use as keyword arguments for the instance to be
          created.

          .. warning::

            If ``kwargs`` sets the
            :meth:`options.series <highcharts_gantt.options.HighchartsOptions.series>`
            property, that setting will be *overridden* by the contents of ``series``.

        :type kwargs: :class:`dict <python:dict>`

        :returns: A new :class:`Chart <highcharts_gantt.chart.Chart>` instance
        :rtype: :class:`Chart <highcharts_gantt.chart.Chart>`
        """
        kwargs = validators.dict(kwargs, allow_empty = True) or {}
        instance = cls(**kwargs)

        instance.add_series(series)

    @staticmethod
    def _get_options_obj(series_type, options_kwargs):
        """Return an :class:`Options` descendent based on the series type.

        :param series_type: Indicates the series type that should be created from the CSV
          data.
        :type series_type: :class:`str <python:str>`

        :param options_kwargs: A :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`Options`
          instance. Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``options_kwargs`` contains a ``series`` key, the ``series`` value will be
            *overwritten*. The ``series`` value will be created from the CSV file instead.

        :type options_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :returns: An :class:`Options` descendent.
        :rtype: :class:`HighchartsOptions` or :class:`HighchartsGanttOptions`
        """
        series_type = validators.string(series_type, allow_empty = False)
        series_type = series_type.lower()
        if series_type not in SERIES_CLASSES:
            raise errors.HighchartsValueError(f'series_type expects a valid Highcharts '
                                              f'series type. Received: {series_type}')

        options_kwargs = validators.dict(options_kwargs, allow_empty = True) or {}

        if series_type not in GANTT_SERIES_LIST:
            options = HighchartsOptions(**options_kwargs)
        else:
            options = HighchartsGanttOptions(**options_kwargs)

        return options

    @classmethod
    def from_csv(cls,
                 as_string_or_file,
                 property_column_map = None,
                 series_type = 'line',
                 has_header_row = True,
                 series_kwargs = None,
                 options_kwargs = None,
                 chart_kwargs = None,
                 delimiter = ',',
                 null_text = 'None',
                 wrapper_character = "'",
                 line_terminator = '\r\n',
                 wrap_all_strings = False,
                 double_wrapper_character_when_nested = False,
                 escape_character = "\\",
                 is_gantt_chart = False,
                 series_in_rows = False,
                 **kwargs):
        """Create a new :class:`Chart <highcharts_core.chart.Chart>` instance with
        data populated from a CSV string or file.

          .. note::

            For an example
            :class:`LineSeries <highcharts_core.options.series.area.LineSeries>`, the
            minimum code required would be:

              .. code-block:: python

                my_chart = Chart.from_csv('some-csv-file.csv',
                                          property_column_map = {
                                              'x': 0,
                                              'y': 3,
                                              'id': 'id'
                                          },
                                          series_type = 'line')

            As the example above shows, data is loaded into the ``my_chart`` instance
            from the CSV file with a filename ``some-csv-file.csv``. The
            :meth:`x <CartesianData.x>`
            values for each data point will be taken from the first (index 0) column in
            the CSV file. The :meth:`y <CartesianData.y>` values will be taken from the
            fourth (index 3) column in the CSV file. And the :meth:`id <CartesianData.id>`
            values will be taken from a column whose header row is labeled ``'id'``
            (regardless of its index).

        :param as_string_or_file: The CSV data to use to pouplate data. Accepts either
          the raw CSV data as a :class:`str <python:str>` or a path to a file in the
          runtime environment that contains the CSV data.

          .. tip::

            Unwrapped empty column values are automatically interpreted as null
            (:obj:`None <python:None>`).

        :type as_string_or_file: :class:`str <python:str>` or Path-like

        :param property_column_map: A :class:`dict <python:dict>` used to indicate which
          data point property should be set to which CSV column. The keys in the
          :class:`dict <python:dict>` should correspond to properties in the data point
          class, while the value can either be a numerical index (starting with 0) or a
          :class:`str <python:str>` indicating the label for the CSV column. Defaults to
          :obj:`None <python:None>`.

          .. warning::

            If the ``property_column_map`` uses :class:`str <python:str>` values, the CSV
            file *must* have a header row (this is expected, by default). If there is no
            header row and a :class:`str <python:str>` value is found, a
            :exc:`HighchartsCSVDeserializationError` will be raised.

        :type property_column_map: :class:`dict <python:dict>`

        :param series_type: Indicates the series type that should be created from the CSV
          data. Defaults to ``'line'``.
        :type series_type: :class:`str <python:str>`

        :param has_header_row: If ``True``, indicates that the first row of
          ``as_string_or_file`` contains column labels, rather than actual data. Defaults
          to ``True``.
        :type has_header_row: :class:`bool <python:bool>`

        :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the series instance. Defaults
          to :obj:`None <python:None>`.

          .. warning::

            If ``series_kwargs`` contains a ``data`` key, its value will be *overwritten*.
            The ``data`` value will be created from the CSV file instead.

        :type series_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param options_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`HighchartsOptions`
          instance. Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``options_kwargs`` contains a ``series`` key, the ``series`` value will be
            *overwritten*. The ``series`` value will be created from the CSV file instead.

        :type options_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param chart_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`Chart` instance.
          Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``chart_kwargs`` contains an ``options`` key, ``options`` will be
            *overwritten*. The ``options`` value will be created from the
            ``options_kwargs`` and CSV file instead.

        :type chart_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param delimiter: The delimiter used between columns. Defaults to ``,``.
        :type delimiter: :class:`str <python:str>`

        :param wrapper_character: The string used to wrap string values when
          wrapping is applied. Defaults to ``'``.
        :type wrapper_character: :class:`str <python:str>`

        :param null_text: The string used to indicate an empty value if empty
          values are wrapped. Defaults to `None`.
        :type null_text: :class:`str <python:str>`

        :param line_terminator: The string used to indicate the end of a line/record in
          the CSV data. Defaults to ``'\\r\\n'``.

          .. note::

            The Python :mod:`csv <python:csv>` currently ignores the ``line_terminator``
            parameter and always applies ``'\\r\\n'``, by design. The Python docs say this
            may change in the future, so for future backwards compatibility we are
            including it here.

        :type line_terminator: :class:`str <python:str>`

        :param wrap_all_strings: If ``True``, indicates that the CSV file has all string
          data values wrapped in quotation marks. Defaults to ``False``.

          .. warning::

            If set to ``True``, the :mod:`csv <python:csv>` module will try to coerce
            any value that is *not* wrapped in quotation marks to a
            :class:`float <python:float>`. This can cause unexpected behavior, and
            typically we recommend leaving this as ``False`` and then re-casting values
            after they have been parsed.

        :type wrap_all_strings: :class:`bool <python:bool>`

        :param double_wrapper_character_when_nested: If ``True``, quote character is
          doubled when appearing within a string value. If ``False``, the
          ``escape_character`` is used to prefix quotation marks. Defaults to ``False``.
        :type double_wrapper_character_when_nested: :class:`bool <python:bool>`

        :param escape_character: A one-character string that indicates the character used
          to escape quotation marks if they appear within a string value that is already
          wrapped in quotation marks. Defaults to ``\\\\`` (which is Python for ``'\\'``,
          which is Python's native escape character).
        :type escape_character: :class:`str <python:str>`

        :param is_gantt_chart: If ``True``, indicates that the chart should be
          instantiated as a **Highcharts Stock for Python** chart. Defaults to ``False``.
        :type is_gantt_chart: :class:`bool <python:bool>`

        :param series_in_rows: if ``True``, will attempt a streamlined cartesian series
          with x-values taken from column names, y-values taken from row values, and
          the series name taken from the row index. Defaults to ``False``.
        :type series_in_rows: :class:`bool <python:bool>`

        :param **kwargs: Remaining keyword arguments will be attempted on the resulting
          :term:`series` instance and the data points it contains.

        :returns: A :class:`Chart <highcharts_core.chart.Chart>` instance with its
          data populated from the CSV data.
        :rtype: :class:`Chart <highcharts_core.chart.Chart>`

        :raises HighchartsCSVDeserializationError: if ``property_column_map`` references
          CSV columns by their label, but the CSV data does not contain a header row

        """
        series_type = validators.string(series_type, allow_empty = False)
        series_type = series_type.lower()
        if series_type not in SERIES_CLASSES:
            raise errors.HighchartsValueError(f'series_type expects a valid Highcharts '
                                              f'series type. Received: {series_type}')

        options_kwargs = validators.dict(options_kwargs, allow_empty = True) or {}
        chart_kwargs = validators.dict(chart_kwargs, allow_empty = True) or {}

        chart_kwargs['is_stock_chart'] = bool(is_gantt_chart)

        series_cls = SERIES_CLASSES.get(series_type, None)

        if series_in_rows:
            series = series_cls.from_csv_in_rows(
                as_string_or_file,
                has_header_row = has_header_row,
                series_kwargs = series_kwargs,
                delimiter = delimiter,
                null_text = null_text,
                wrapper_character = wrapper_character,
                line_terminator = line_terminator,
                wrap_all_strings = wrap_all_strings,
                double_wrapper_character_when_nested = double_wrapper_character_when_nested,
                escape_character = escape_character,
                **kwargs
            )
        else:
            series = series_cls.from_csv(as_string_or_file,
                                         property_column_map = property_column_map,
                                         has_header_row = has_header_row,
                                         series_kwargs = series_kwargs,
                                         delimiter = delimiter,
                                         null_text = null_text,
                                         wrapper_character = wrapper_character,
                                         line_terminator = line_terminator,
                                         wrap_all_strings = wrap_all_strings,
                                         double_wrapper_character_when_nested = double_wrapper_character_when_nested,
                                         escape_character = escape_character,
                                         **kwargs)

        if not isinstance(series, list):
            series = [series]

        options_kwargs['series'] = series

        options = cls._get_options_obj(series_type, options_kwargs)

        instance = cls(**chart_kwargs)
        instance.options = options

        return instance

    @classmethod
    def from_pandas(cls,
                    df,
                    property_map = None,
                    series_type = 'line',
                    series_kwargs = None,
                    options_kwargs = None,
                    chart_kwargs = None,
                    series_in_rows = False,
                    series_index = None,
                    **kwargs):
        """Create a :class:`Chart <highcharts_core.chart.Chart>` instance whose
        data is populated from a `pandas <https://pandas.pydata.org/>`_
        :class:`DataFrame <pandas:pandas.DataFrame>`.

        :param df: The :class:`DataFrame <pandas:pandas.DataFrame>` from which data should be
          loaded.
        :type df: :class:`DataFrame <pandas:pandas.DataFrame>`

        :param property_map: A :class:`dict <python:dict>` used to indicate which
          data point property should be set to which column in ``df``. The keys in the
          :class:`dict <python:dict>` should correspond to properties in the data point
          class, while the value should indicate the label for the
          :class:`DataFrame <pandas:pandas.DataFrame>` column. Defaults to 
          :obj:`None <python:None>`.
        :type property_map: :class:`dict <python:dict>`

        :param series_type: Indicates the series type that should be created from the data
          in ``df``. Defaults to ``'line'``.
        :type series_type: :class:`str <python:str>`

        :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the series instance. Defaults
          to :obj:`None <python:None>`.

          .. warning::

            If ``series_kwargs`` contains a ``data`` key, its value will be *overwritten*.
            The ``data`` value will be created from ``df`` instead.

        :type series_kwargs: :class:`dict <python:dict>`

        :param options_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`HighchartsOptions`
          instance. Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``options_kwargs`` contains a ``series`` key, the ``series`` value will be
            *overwritten*. The ``series`` value will be created from the data in ``df``.

        :type options_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param chart_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`Chart` instance.
          Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``chart_kwargs`` contains an ``options`` key, ``options`` will be
            *overwritten*. The ``options`` value will be created from the
            ``options_kwargs`` and the data in ``df`` instead.

        :type chart_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param series_in_rows: if ``True``, will attempt a streamlined cartesian series
          with x-values taken from column names, y-values taken from row values, and
          the series name taken from the row index. Defaults to 
          :obj:`False <python:False>`.
        :type series_in_rows: :class:`bool <python:bool>`

        :param series_index: If supplied, generate the chart with the series that 
          Highcharts for Python generated from ``df`` at the ``series_index`` position. 
          Defaults to :obj:`None <python:None>`, which includes all series generated 
          from ``df`` on the chart.

        :type series_index: :class:`int <python:int>`, slice, or 
          :obj:`None <python:None>`

        :param **kwargs: Additional keyword arguments that are - in turn - propagated to 
          the series created from the ``df``.

        :returns: A :class:`Chart <highcharts_core.chart.Chart>` instance with its
          data populated from the data in ``df``.
        :rtype: :class:`Chart <highcharts_core.chart.Chart>`

        :raises HighchartsPandasDeserializationError: if ``property_map`` references
          a column that does not exist in the data frame
        :raises HighchartsDependencyError: if `pandas <https://pandas.pydata.org/>`_ is
          not available in the runtime environment
        """
        if not series_type:
            raise errors.HighchartsValueError('series_type cannot be empty')
        series_type = str(series_type).lower()
        if series_type not in SERIES_CLASSES:
            raise errors.HighchartsValueError(f'series_type expects a valid Highcharts '
                                              f'series type. Received: {series_type}')

        if not isinstance(options_kwargs, (dict, UserDict, type(None))):
            raise errors.HighchartsValueError(f'options_kwarts expects a dict. '
                                              f'Received: {options_kwargs.__class__.__name__}')
        if not options_kwargs:
            options_kwargs = {}
            
        if not isinstance(chart_kwargs, (dict, UserDict, type(None))):
            raise errors.HighchartsValueError(f'chart_kwargs expects a dict. '
                                              f'Received: {chart_kwargs.__class__.__name__}')
        if not chart_kwargs:
            chart_kwargs = {}
            
        if not isinstance(kwargs, (dict, UserDict, type(None))):
            raise errors.HighchartsValueError(f'kwargs expects a dict. '
                                              f'Received: {kwargs.__class__.__name__}')
        if not kwargs:
            kwargs = {}

        series_cls = SERIES_CLASSES.get(series_type, None)

        if series_in_rows:
            series = series_cls.from_pandas_in_rows(df,
                                                    series_kwargs = series_kwargs,
                                                    series_index = series_index,
                                                    **kwargs)
        else:
            series = series_cls.from_pandas(df,
                                            property_map = property_map,
                                            series_kwargs = series_kwargs,
                                            series_index = series_index,
                                            **kwargs)

        if isinstance(series, series_cls):
            series = [series]

        options_kwargs['series'] = series
        options = cls._get_options_obj(series_type, options_kwargs)

        instance = cls(**chart_kwargs)
        instance.options = options

        return instance

    @classmethod
    def from_pyspark(cls,
                     df,
                     property_map,
                     series_type,
                     series_kwargs = None,
                     options_kwargs = None,
                     chart_kwargs = None):
        """Create a :class:`Chart <highcharts_core.chart.Chart>` instance whose
        data is populated from a
        `PySpark <https://spark.apache.org/docs/latest/api/python/>`_
        :class:`DataFrame <pyspark:pyspark.sql.DataFrame>`.

        :param df: The :class:`DataFrame <pyspark:pyspark.sql.DataFrame>` from which data
          should be loaded.
        :type df: :class:`DataFrame <pyspark:pyspark.sql.DataFrame>`

        :param property_map: A :class:`dict <python:dict>` used to indicate which
          data point property should be set to which column in ``df``. The keys in the
          :class:`dict <python:dict>` should correspond to properties in the data point
          class, while the value should indicate the label for the
          :class:`DataFrame <pyspark:pyspark.sql.DataFrame>` column.
        :type property_map: :class:`dict <python:dict>`

        :param series_type: Indicates the series type that should be created from the data
          in ``df``.
        :type series_type: :class:`str <python:str>`

        :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the series instance. Defaults
          to :obj:`None <python:None>`.

          .. warning::

            If ``series_kwargs`` contains a ``data`` key, its value will be *overwritten*.
            The ``data`` value will be created from ``df`` instead.

        :type series_kwargs: :class:`dict <python:dict>`

        :param options_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`HighchartsOptions`
          instance. Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``options_kwargs`` contains a ``series`` key, the ``series`` value will be
            *overwritten*. The ``series`` value will be created from the data in ``df``.

        :type options_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param chart_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`Chart` instance.
          Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``chart_kwargs`` contains an ``options`` key, ``options`` will be
            *overwritten*. The ``options`` value will be created from the
            ``options_kwargs`` and the data in ``df`` instead.

        :type chart_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :returns: A :class:`Chart <highcharts_core.chart.Chart>` instance with its
          data populated from the data in ``df``.
        :rtype: :class:`Chart <highcharts_core.chart.Chart>`

        :raises HighchartsPySparkDeserializationError: if ``property_map`` references
          a column that does not exist in the data frame
        :raises HighchartsDependencyError: if
          `PySpark <https://spark.apache.org/docs/latest/api/python/>`_ is not available
          in the runtime environment
        """
        chart_kwargs = validators.dict(chart_kwargs, allow_empty = True) or {}

        options = cls._get_options_obj(series_type, options_kwargs)

        series_cls = SERIES_CLASSES.get(series_type, None)

        series = series_cls.from_pyspark(df,
                                         property_map,
                                         series_kwargs)

        options = HighchartsOptions(**options_kwargs)
        options.series = [series]

        instance = cls(**chart_kwargs)
        instance.options = options

        return instance

    @classmethod
    def from_options(cls,
                     options,
                     chart_kwargs = None):
        """Create a :class:`Chart <highcharts_gantt.chart.Chart>` instance from a
        :class:`HighchartsOptions <highcharts_gantt.options.HighchartsOptions>` or
        :class:`HighchartsGanttOptions <highcharts_gantt.options.HighchartsGanttOptions>`
        object.

        :param options: The configuration options to use to instantiate the chart.
        :type options:
          :class:`HighchartsOptions <highcharts_core.options.HighchartsOptions>` or
          related or coercable

        :param chart_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the instance. Defaults to
          :obj:`None <python:None>`.

          .. warning::

            If ``chart_kwargs`` contains an ``options`` key, ``options`` will be
            *overwritten* by the contents of ``options``.

        :type chart_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :returns: The :class:`Chart <highcharts_core.chart.Chart>` instance
        :rtype: :class:`Chart <highcharts_core.chart.Chart>`
        """
        chart_kwargs = validators.dict(chart_kwargs, allow_empty = True) or {}
        if checkers.is_type(options, 'HighchartsGanttOptions'):
            options = options
            chart_kwargs['is_gantt_chart'] = True
        elif checkers.is_type(options, 'HighchartsOptions'):
            options = options
        elif ('navigator' in options
              or 'range_selector' in options
              or 'rangeSelector' in options
              or 'connectors' in options):
            options = validate_types(options, HighchartsGanttOptions)
            chart_kwargs['is_gantt_chart'] = True
        elif chart_kwargs.get('is_gantt_chart', False):
            options = validate_types(options, HighchartsGanttOptions)
            chart_kwargs['is_gantt_chart'] = True
        else:
            options = validate_types(options, HighchartsOptions)

        instance = cls(**chart_kwargs)
        instance.options = options

        return instance

    @classmethod
    def from_asana(cls,
                   project_gid,
                   section_gid = None,
                   completed_since = None,
                   use_html_description = True,
                   personal_access_token = None,
                   asana_client = None,
                   api_request_params = None,
                   connection_kwargs = None,
                   connection_callback = None,
                   series_kwargs = None,
                   options_kwargs = None,
                   chart_kwargs = None):
        """Create a Gantt :class:`Chart <highcharts_gantt.chart.Chart>`
        instance from an `Asana <https://www.asana.com/>`__ project.
        
        .. note::
        
          **Highcharts Gantt for Python** can create an Asana API client for you, 
          authenticating using the :term:`Personal Access Token`` method supported by
          the Asana API. However, if you wish to use the more-involved OAuth2 handshake
          process you will need to create your own Asana API client using the 
          `asana-python <https://pypi.org/project/asana/>`__ library. 
          
          The reason for this is because the OAuth2 handshake has various permutations
          involving redirects, token refreshes, etc. which are outside the scope of the
          **Highcharts Gantt for Python** library, and if you are integrating 
          **Highcharts Gantt for Python** into a larger application you are likely 
          already facilitating the OAuth2 dance in a fashion appropriate for your use 
          case.
          
        :param project_gid: The globally unique ID of the Project whose tasks should be
          used to assemble the Gantt chart.
        :type project_gid: :class:`str <python:str>`
        
        :param section_gid: The optional unique ID of the section whose tasks should be
          used to assemble the Gantt chart. Defaults to :obj:`None <python:None>`, which
          returns all tasks in the project.
        :type section_gid: :class:`str <python:str>` or :obj:`None <python:None>`
        
        :param completed_since: An optional filter which only returns tasks that have 
          been completed after this date. Defaults to :obj:`None <python:None>`, which
          returns all tasks.
        :type completed_since: :class:`datetime <python:datetime.datetime>` or 
          :obj:`None <python:None>`
          
        :param use_html_description: If ``True``, will use the Asana task's HTML notes 
          in the data point's 
          :meth:`.description <highcharts_gantt.options.series.data.gantt.GanttData.description>` 
          field. If ``False``, will use the non-HTML notes. Defaults to ``True``.
        :type use_html_description: :class:`bool <python:bool>`
        
        :param personal_access_token: A Personal Access Token created by Asana.
          Defaults to :obj:`None <python:None>`, which tries to determine its value
          by looking in the ``ASANA_PERSONAL_ACCESS_TOKEN`` environment variable.
        :type personal_access_token: :class:`str <python:str>` or 
          :obj:`None <python:None>`
          
        :param api_request_params: Collection of additional request parameters to 
          submit to the Asana API. Defaults to :obj:`None <python:None>`.
        :type api_request_params: :class:`dict <python:dict>` or 
          :obj:`None <python:None>`
          
        :param connection_kwargs: Set of keyword arugments to supply to the   
          :class:`DataConnection <highcharts_gantt.options.series.data.connect.DataConnection>`
          constructor, besides the :meth:`.to <highcharts_gantt.options.series.data.connect.DataConnection.to>` property which is derived from the task. Defaults
          to :obj:`None <python:None>`
        :type connection_kwargs: :class:`dict <python:dict>` or 
          :obj:`None <python:None>`
          
        :param connection_callback: A custom Python function or method which accepts two
          keyword arguments: ``connection_target`` (which expects the dependency 
          :class:`dict <python:dict>` object from the Asana task), and ``asana_task`` 
          (which expects the Asana task :class:`dict <pythoN:dict>` object). The 
          function should return a 
          :class:`DataConnection <highcharts_gantt.options.series.data.connect.DataConnection>` instance. Defaults to :obj:`None <python:None>`
          
          .. tip::
          
            The ``connection_callback`` argument is useful if you want to customize the
            connection styling based on properties included in the Asana task.
            
        :type connection_callback: Callable or :obj:`None <python:None>`
        
        :param series_kwargs: Collection of additional keyword arguments to use when 
          instantiating the 
          :class:`GanttSeries <highcharts_gantt.options.series.GanttSeries>` (besides 
          the ``data`` argument, which will be determined from the Asana tasks).
          Defaults to :obj:`None <python:None>`.
        :type series_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param options_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`HighchartsOptions`
          instance. Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``options_kwargs`` contains a ``series`` key, the ``series`` value will be
            *overwritten*. The ``series`` value will be created from the data in ``df``.

        :type options_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param chart_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`Chart` instance.
          Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``chart_kwargs`` contains an ``options`` key, ``options`` will be
            *overwritten*. The ``options`` value will be created from the
            ``options_kwargs`` and the data in ``df`` instead.

        :type chart_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :returns: A Gantt :class:`Chart <highcharts_gantt.chart.Chart>` instance
        :rtype: :class:`Chart <highcharts_gantt.chart.Chart>`
        """
        series_cls = SERIES_CLASSES.get('gantt', None)
        
        options_kwargs = validators.dict(options_kwargs, allow_empty = True) or {}
        chart_kwargs = validators.dict(chart_kwargs, allow_empty = True) or {}
        
        series = series_cls.from_asana(project_gid = project_gid,
                                       section_gid = section_gid,
                                       completed_since = completed_since,
                                       use_html_description = use_html_description,
                                       personal_access_token = personal_access_token,
                                       asana_client = asana_client,
                                       api_request_params = api_request_params,
                                       connection_kwargs = connection_kwargs,
                                       connection_callback = connection_callback,
                                       series_kwargs = series_kwargs)
        
        options = HighchartsGanttOptions(**options_kwargs)
        options.series = [series]
        
        instance = cls(**chart_kwargs)
        instance.options = options
        instance.is_gantt_chart = True
        
        return instance
      
    @classmethod
    def from_monday(cls,
                    board_id,
                    api_token = None,
                    template = None,
                    property_column_map = None,
                    connection_kwargs = None,
                    connection_callback = None,
                    series_kwargs = None,
                    options_kwargs = None,
                    chart_kwargs = None):
        """Create a :class:`Chart <highcharts_gantt.chart.Chart>` instance from a 
        `Monday.com <https://www.monday.com>`__ work board.
        
        :param board_id: The ID of the Monday.com board whose items should be retrieved
          to populate the Gantt series.
        :type board_id: :class:`int <python:int>`
        
        :param api_token: The Monday.com API token to use when authenticating your
          request against the Monday.com API. Defaults to :obj:`None <python:None>`,
          which will then try to determine the token from the ``MONDAY_API_TOKEN``
          environment variable.
          
          .. warning::
          
            If no token is either passed to the method *or* found in the 
            ``MONDAY_API_TOKEN`` environment variable, calling this method will raise
            an error.
            
        :type api_token: :class:`str <python:str>` or :obj:`None <python:None>`
        
        :param template: The name of a standard Mpnday.com board template supported by 
          **Highcharts for Python**. If supplied, will override the 
          ``property_column_map`` argument. Defaults to :obj:`None <python:None>`.
          
          .. note::
          
            If ``property_column_map`` is set, the ``template`` argument will be
            *ignored* and overridden by ``property_column_map``.

        :type template: :class:`str <python:str>` or :obj:`None <python:None>`
        
        :param property_column_map: A :class:`dict <python:dict>` used to map Monday.com
          columns to their corresponding 
          :class:`GanttSeries <highcharts_gantt.options.series.gantt.GanttSeries>` 
          properties. Keys are expected to be 
          :class:`GanttSeries <highcharts_gantt.options.series.gantt.GanttSeries>`
          properties, while values are expected to be Monday.com column field names. 
          Defaults to :obj:`None <python:None>`.
          
          .. note::
          
            If ``property_column_map`` is supplied, its settings *override* the 
            ``template`` setting.
            
        :type property_column_map: :class:`dict <python:dict>` or 
          :obj:`None <python:None>`
          
        :param connection_kwargs: Set of keyword arugments to supply to the   
          :class:`DataConnection <highcharts_gantt.options.series.data.connect.DataConnection>`
          constructor, besides the :meth:`.to <highcharts_gantt.options.series.data.connect.DataConnection.to>` 
          property which is derived from the task. Defaults to :obj:`None <python:None>`
        :type connection_kwargs: :class:`dict <python:dict>` or 
          :obj:`None <python:None>`
          
        :param connection_callback: A custom Python function or method which accepts two
          keyword arguments: ``connection_target`` (which expects the dependency 
          :class:`dict <python:dict>` object from the Asana task), and ``asana_task`` 
          (which expects the Asana task :class:`dict <pythoN:dict>` object). The 
          function should return a 
          :class:`DataConnection <highcharts_gantt.options.series.data.connect.DataConnection>` instance. Defaults to 
          :obj:`None <python:None>`
          
          .. tip::
          
            The ``connection_callback`` argument is useful if you want to customize the
            connection styling based on properties included in the Asana task.
            
        :type connection_callback: Callable or :obj:`None <python:None>`
        
        :param series_kwargs: Collection of additional keyword arguments to use when 
          instantiating the 
          :class:`GanttSeries <highcharts_gantt.options.series.GanttSeries>` (besides 
          the ``data`` argument, which will be determined from the Asana tasks).
          Defaults to :obj:`None <python:None>`.
        :type series_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param series_kwargs: Collection of additional keyword arguments to use when 
          instantiating the 
          :class:`GanttSeries <highcharts_gantt.options.series.GanttSeries>` (besides 
          the ``data`` argument, which will be determined from the Asana tasks).
          Defaults to :obj:`None <python:None>`.
        :type series_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param options_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`HighchartsOptions`
          instance. Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``options_kwargs`` contains a ``series`` key, the ``series`` value will be
            *overwritten*. The ``series`` value will be created from the data in ``df``.

        :type options_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param chart_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`Chart` instance.
          Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``chart_kwargs`` contains an ``options`` key, ``options`` will be
            *overwritten*. The ``options`` value will be created from the
            ``options_kwargs`` and the data in ``df`` instead.

        :type chart_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :returns: A Gantt :class:`Chart <highcharts_gantt.chart.Chart>` instance
        :rtype: :class:`GanttSeries <highcharts_gantt.options.series.gantt.GanttSeries>`
        
        :raises HighchartsDependencyError: if the 
          `monday <https://pypi.org/project/monday/>`__ Python library is not available 
          in the runtime environment
        :raises MondayAuthenticationError: if there is no Monday.com API token supplied
        :raises HighchartsValueError: if both ``template`` and ``property_column_map`` 
          are empty
        
        """
        series_cls = SERIES_CLASSES.get('gantt', None)

        options_kwargs = validators.dict(options_kwargs, allow_empty = True) or {}
        chart_kwargs = validators.dict(chart_kwargs, allow_empty = True) or {}

        series = series_cls.from_monday(board_id = board_id,
                                        api_token = api_token,
                                        template = template,
                                        property_column_map = property_column_map,
                                        connection_kwargs = connection_kwargs,
                                        connection_callback = connection_callback,
                                        series_kwargs = series_kwargs)

        options = HighchartsGanttOptions(**options_kwargs)
        options.series = [series]
        
        instance = cls(**chart_kwargs)
        instance.options = options
        instance.is_gantt_chart = True
        
        return instance

    @classmethod
    def from_jira(cls, 
                  project_key,
                  server = None,
                  jql = None,
                  username = None,
                  password_or_token = None,
                  oauth_dict = None,
                  client_kwargs = None,
                  jira_client = None,
                  connection_kwargs = None,
                  connection_callback = None,
                  series_kwargs = None,
                  options_kwargs = None,
                  chart_kwargs = None):
        """Create a :class:`Chart <highcharts_gantt.chart.Chart>` instance from an
        `Atlassian <https://www.atlassian.com>`__ JIRA project.
        
        .. note::
        
          **Highcharts Gantt for Python** can create a JIRA API client for you, 
          authenticating using either the :term:`Basic Authentication` or 
          :term:`Access Token` methods supported by the JIRA API. However, if you wish 
          to use the more-involved OAuth2  handshake, you can do so yourself and either
          
            * supply an ``oauth_dict`` argument containing the OAuth2 configuration 
              details, or
            * supply a fully-authenticated ``jira_client``
          
          The reason for this is because the OAuth2 handshake has various permutations
          involving redirects, token refreshes, etc. which are outside the scope of the
          **Highcharts Gantt for Python** library, and if you are integrating 
          **Highcharts Gantt for Python** into a larger application you are likely 
          already facilitating the OAuth2 dance in a fashion appropriate for your use 
          case.
          
        :param project_key: The globally unique key of the Project whose tasks should be
          used to assemble the Gantt chart. For example, ``JRA``.
        :type project_key: :class:`str <python:str>`
        
        :param server: The URL of the JIRA instance from which data should be retrieved.
          Defaults to :obj:`None <python:None>`, which looks for a value in the ``HIGHCHARTS_JIRA_SERVER`` environment 
          variable. If no value is found there, will then fallback to JIRA Cloud: ``'https://jira.atlasian.com'``.
          
          .. note::
          
            This argument will override the comparable setting in ``client_kwargs`` if
            ``client_kwargs`` is supplied.

        :type server: :class:`str <python:str>` or :obj:`None <python:None>`
        
        :param jql: An optional :term:`JIRA Query Language` query string to further 
          narrow the issues returned from JIRA. Defaults to :obj:`None <python:None>`.
        :type jql: :class:`str <python:str>` or :obj:`None <python:None>`
        
        :param username: The username to use when authenticating using either ``basic`` 
          or ``token`` authentication. Defaults to :obj:`None <python:None>`, which 
          looks for a value in the ``HIGHCHARTS_JIRA_USERNAME`` environment variable.
          
          .. note::
          
            If ``oauth2_dict`` is supplied, the ``username`` argument will be ignored
            since OAuth2 authentication will be used.
            
        :type username: :class:`str <python:str>` or :obj:`None <python:None>`
        
        :param password_or_token: The password or access token to use when 
          authenticating using either ``basic`` or ``token`` authentication. Defaults 
          to :obj:`None <python:None>`, which looks for a vlaue in the 
          ``HIGHCHARTS_JIRA_TOKEN`` environment variable.
          
          .. note::
          
            If ``oauth_dict`` is supplied, the ``password_or_token`` will be ignored
            since OAuth2 authentication will be used.
            
        :type password_or_token: :class:`str <python:str>` or :obj:`None <python:None>`
        
        :param oauth_dict: A :class:`dict <python:dict>` of key/value pairs providing
          configuration of the Oauth2 authentication details. Expected keys are:
          
            * ``'access_token'``
            * ``'access_token_secret'``
            * ``'consumer_key'``
            * ``'key_cert'``
          
          Defaults to :obj:`None <python:None>`.
          
          .. note::
          
            To use OAuth2 authentication, an ``oauth_dict`` *must* be supplied. If you 
            wish to force either basic or token authentication, make sure this argument
            remains :obj:`None <python:None>`.
          
        :type oauth_dict: :class:`dict <python:dict>` or :obj:`None <python:None>`
        
        :param client_kwargs: An optional :class:`dict <python:dict>` providing keyword 
          arguments to use when instantiating the JIRA client.
        :type client_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`
        
        :param jira_client: A fully-configured and fully-authenticated JIRA API client.
          Defaults to :obj:`None <python:None>`.
        :type jira_client: :class:`jira.client.JIRA <jira:jira.client.JIRA>` instance 
          that has been fully authenticated
          
        :param connection_kwargs: Set of keyword arugments to supply to the   
          :class:`DataConnection <highcharts_gantt.options.series.data.connect.DataConnection>`
          constructor, besides the 
          :meth:`.to <highcharts_gantt.options.series.data.connect.DataConnection.to>` 
          property which is derived from the task. Defaults to :obj:`None <python:None>`
        :type connection_kwargs: :class:`dict <python:dict>` or 
          :obj:`None <python:None>`
          
        :param connection_callback: A custom Python function or method which accepts two
          keyword arguments: ``connection_target`` (which expects the dependency 
          :class:`Issue <jira:jira.resources.Issue>` object from the initial 
          :class:`Issue <jira:jira.resources.Issue>`), and ``issue`` 
          (which expects the initial :class:`Issue <jira:jira.resources.Issue>` 
          object). The function should return a 
          :class:`DataConnection <highcharts_gantt.options.series.data.connect.DataConnection>` 
          instance. Defaults to :obj:`None <python:None>`.
          
          .. tip::
          
            The ``connection_callback`` argument is useful if you want to customize the
            connection styling based on properties included in the target issue.
            
        :type connection_callback: Callable or :obj:`None <python:None>`
        
        :param series_kwargs: Collection of additional keyword arguments to use when 
          instantiating the 
          :class:`GanttSeries <highcharts_gantt.options.series.GanttSeries>` (besides 
          the ``data`` argument, which will be determined from the JIRA issues).
          Defaults to :obj:`None <python:None>`.
        :type series_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :returns: A Gantt :class:`Chart <highcharts_gantt.chart.Chart>` instance
        :rtype: :class:`GanttSeries <highcharts_gantt.options.series.gantt.GanttSeries>`
        
        :raises HighchartsDependencyError: if the 
          `jira <https://pypi.org/project/jira/>`__ Python library is not available 
          in the runtime environment
        :raises JIRAAuthenticationError: if authentication against the JIRA server fails
        :raises HighchartsValueError: if both ``template`` and ``property_column_map`` 
          are empty
          
        """
        series_cls = SERIES_CLASSES.get('gantt', None)

        options_kwargs = validators.dict(options_kwargs, allow_empty = True) or {}
        chart_kwargs = validators.dict(chart_kwargs, allow_empty = True) or {}

        series = series_cls.from_jira(project_key = project_key,
                                      server = server,
                                      jql = jql,
                                      username = username,
                                      password_or_token = password_or_token,
                                      oauth_dict = oauth_dict,
                                      client_kwargs = client_kwargs,
                                      jira_client = jira_client,
                                      connection_kwargs = connection_kwargs,
                                      connection_callback = connection_callback,
                                      series_kwargs = series_kwargs)

        options = HighchartsGanttOptions(**options_kwargs)
        options.series = [series]
        
        instance = cls(**chart_kwargs)
        instance.options = options
        instance.is_gantt_chart = True
        
        return instance
