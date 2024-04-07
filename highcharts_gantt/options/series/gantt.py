import os
from typing import Optional, List

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from validator_collection import validators, checkers

try:
    import asana
    HAS_ASANA = True
except ImportError:
    HAS_ASANA = False
    
try:
  import jira
  HAS_JIRA = True
except ImportError:
  HAS_JIRA = False

from highcharts_core.options.series.base import SeriesBase

from highcharts_gantt import errors, monday
from highcharts_gantt.options.plot_options.gantt import GanttOptions
from highcharts_gantt.options.series.data.gantt import GanttData, GanttDataCollection
from highcharts_gantt.utility_functions import mro__to_untrimmed_dict, is_ndarray


class GanttSeries(SeriesBase, GanttOptions):
    """Options to configure a Gantt series.

    Gantt charts are a type of chart used to visualize efforts executed in a sequence.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def data(self) -> Optional[List[GanttData] | GanttDataCollection]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`GanttData` instances,
        it accepts as input an iterable of :class:`GanttData` instances or
        :class:`dict <python:dict>` instances that can be coerced to :class:`GanttData`.

        :rtype: :class:`list <python:list>` of :class:`GanttData` or
          :class:`GanttDataCollection` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not is_ndarray(value) and not value:
            self._data = None
        else:
            self._data = GanttData.from_array(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'allow_point_select': as_dict.get('allowPointSelect', None),
            'animation': as_dict.get('animation', None),
            'class_name': as_dict.get('className', None),
            'clip': as_dict.get('clip', None),
            'color': as_dict.get('color', None),
            'cursor': as_dict.get('cursor', None),
            'custom': as_dict.get('custom', None),
            'dash_style': as_dict.get('dashStyle', None),
            'data_labels': as_dict.get('dataLabels', None),
            'description': as_dict.get('description', None),
            'enable_mouse_tracking': as_dict.get('enableMouseTracking', None),
            'events': as_dict.get('events', None),
            'include_in_data_export': as_dict.get('includeInDataExport', None),
            'keys': as_dict.get('keys', None),
            'label': as_dict.get('label', None),
            'legend_symbol': as_dict.get('legendSymbol', None),
            'linked_to': as_dict.get('linkedTo', None),
            'marker': as_dict.get('marker', None),
            'on_point': as_dict.get('onPoint', None),
            'opacity': as_dict.get('opacity', None),
            'point': as_dict.get('point', None),
            'point_description_formatter': as_dict.get('pointDescriptionFormatter', None),
            'selected': as_dict.get('selected', None),
            'show_checkbox': as_dict.get('showCheckbox', None),
            'show_in_legend': as_dict.get('showInLegend', None),
            'skip_keyboard_navigation': as_dict.get('skipKeyboardNavigation', None),
            'states': as_dict.get('states', None),
            'sticky_tracking': as_dict.get('stickyTracking', None),
            'threshold': as_dict.get('threshold', None),
            'tooltip': as_dict.get('tooltip', None),
            'turbo_threshold': as_dict.get('turboThreshold', None),
            'visible': as_dict.get('visible', None),

            'animation_limit': as_dict.get('animationLimit', None),
            'boost_blending': as_dict.get('boostBlending', None),
            'boost_threshold': as_dict.get('boostThreshold', None),
            'color_axis': as_dict.get('colorAxis', None),
            'color_index': as_dict.get('colorIndex', None),
            'color_key': as_dict.get('colorKey', None),
            'connect_ends': as_dict.get('connectEnds', None),
            'connect_nulls': as_dict.get('connectNulls', None),
            'crisp': as_dict.get('crisp', None),
            'crop_threshold': as_dict.get('cropThreshold', None),
            'data_sorting': as_dict.get('dataSorting', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'fill_color': as_dict.get('fillColor', None),
            'fill_opacity': as_dict.get('fillOpacity', None),
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'get_extremes_from_all': as_dict.get('getExtremesFromAll', None),
            'inactive_other_points': as_dict.get('inactiveOtherPoints', None),
            'linecap': as_dict.get('linecap', None),
            'line_color': as_dict.get('lineColor', None),
            'line_width': as_dict.get('lineWidth', None),
            'negative_color': as_dict.get('negativeColor', None),
            'negative_fill_color': as_dict.get('negativeFillColor', None),
            'point_interval': as_dict.get('pointInterval', None),
            'point_interval_unit': as_dict.get('pointIntervalUnit', None),
            'point_placement': as_dict.get('pointPlacement', None),
            'point_start': as_dict.get('pointStart', None),
            'relative_x_value': as_dict.get('relativeXValue', None),
            'shadow': as_dict.get('shadow', None),
            'soft_threshold': as_dict.get('softThreshold', None),
            'stacking': as_dict.get('stacking', None),
            'step': as_dict.get('step', None),
            'track_by_area': as_dict.get('trackByArea', None),
            'zone_axis': as_dict.get('zoneAxis', None),
            'zones': as_dict.get('zones', None),

            'border_color': as_dict.get('borderColor', None),
            'border_radius': as_dict.get('borderRadius', None),
            'border_width': as_dict.get('borderWidth', None),
            'center_in_category': as_dict.get('centerInCategory', None),
            'color_by_point': as_dict.get('colorByPoint', None),
            'colors': as_dict.get('colors', None),
            'grouping': as_dict.get('grouping', None),
            'group_padding': as_dict.get('groupPadding', None),
            'max_point_width': as_dict.get('maxPointWidth', None),
            'min_point_length': as_dict.get('minPointLength', None),
            'point_padding': as_dict.get('pointPadding', None),
            'point_range': as_dict.get('pointRange', None),
            'point_width': as_dict.get('pointWidth', None),

            'group_z_padding': as_dict.get('groupZPadding', None),
            'partial_fill': as_dict.get('partialFill', None),

            'data_as_columns': as_dict.get('dataAsColumns', None),

            'data': as_dict.get('data', None),
            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'name': as_dict.get('name', None),
            'z_index': as_dict.get('zIndex', None),
            
            'connectors': as_dict.get('connectors', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = mro__to_untrimmed_dict(self, in_cls = in_cls)

        return untrimmed

    def load_from_asana(self,
                        project_gid,
                        section_gid = None,
                        completed_since = None,
                        use_html_description = True,
                        personal_access_token = None,
                        asana_client = None,
                        api_request_params = None,
                        connection_kwargs = None,
                        connection_callback = None):
        """Replace the data in the
        :class:`GanttSeries <highcharts_gantt.options.series.gantt.GanttSeries>`
        instance with data from an `Asana <https://www.asana.com/>`__ project.
        
        .. note::
        
          **Highcharts Gantt for Python** can create an Asana API client for you, 
          authenticating using the :term:`Personal Access Token` method supported by
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
          used to assemble the Gantt series.
          
          .. tip::
          
            You can find your Asana Project GID in your browser URL bar:
            
            .. figure:: /_static/asana-project-gid.png
              :align: center
              :alt: Asana Project GID

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
          constructor, besides the :meth:`.to <highcharts_gantt.options.series.data.connect.DataConnection.to>` 
          property which is derived from the task. Defaults
          to :obj:`None <python:None>`
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
        
        :returns: A :class:`GanttSeries <highcharts_gantt.options.series.gantt.GanttSeries>`
          populated with data from the indicated Asana project/section.
        :rtype: :class:`GanttSeries <highcharts_gantt.options.series.gantt.GanttSeries>`
        
        :raises HighchartsDependencyError: if the 
          `asana <https://pypi.org/project/asana/>`__ Python library is not available 
          in the runtime environment.
          
        :raises HighchartsValueError: if ``connection_callback`` is not 
          :obj:`None <python:None>`, but is not callable
        :raises HighchartsValueError: if ``asana_client`` is not 
          :obj:`None <python:None>`, but is not a valid :class:`asana.client.Client>`
          instance
        :raises AsanaAuthenticationError: if ``asana_client`` is not authenticated or 
          if no personal access token is supplied
        """
        if not HAS_ASANA:
            raise errors.HighchartsDependencyError('The .from_asana() method requires '
                                                   'the asana Python library. However '
                                                   'your runtime environment does not '
                                                   'seem to have it. Please install and'
                                                   ' try again.')

        project_gid = validators.string(project_gid, coerce_value = True)
        
        section_gid = validators.string(section_gid, 
                                        allow_empty = True, 
                                        coerce_value = True)
        
        completed_since = validators.datetime(completed_since, allow_empty = True)
        
        api_request_params = validators.dict(api_request_params, 
                                             allow_empty = True) or {}
        
        if not personal_access_token:
            personal_access_token = os.getenv('ASANA_PERSONAL_ACCESS_TOKEN', None)
            
        if asana_client and not isinstance(asana_client, asana.client.Client):
            raise errors.HighchartsValueError(f'asana_client must be a valid asana '
                                              f'Client instance. Was: '
                                              f'{asana_client.__class__.__name__}')
        if asana_client and not asana_client.session.token:
            raise errors.AsanaAuthenticationError('asana_client is not authenticated')
          
        if asana_client:
            client = asana_client
        elif not personal_access_token:
            raise errors.AsanaAuthenticationError('from_asana() requires either a '
                                                  'personal access token or an '
                                                  'authenticated Asana client. '
                                                  'Neither was supplied.')
        else:
            client = asana.Client.access_token(personal_access_token)
            
        client.LOG_ASANA_CHANGE_WARNINGS = False
    
        if section_gid:
            request = client.tasks.get_tasks_for_section
            request_params = {
                'section_gid': section_gid
            }
        else:
            request = client.tasks.get_tasks_for_project
            request_params = {
                'project_gid': project_gid
            }
            
        request_params['params'] = {}
        if completed_since:
            request_params['params']['completed_since'] = completed_since.isoformat()
            
        opt_fields = ['approval_status',
                      'assignee_status',
                      'completed',
                      'completed_at',
                      'dependencies',
                      'dependents',
                      'due_at',
                      'due_on',
                      'html_notes',
                      'name',
                      'notes',
                      'start_at',
                      'start_on',
                      'assignee',
                      'assignee_section',
                      'parent',
                      'permalink_url',
                      'custom_fields',
                      'resource_type',
                      'resource_subtype']
        request_params['params']['opt_fields'] = opt_fields
        for key in request_params:
            api_request_params[key] = request_params[key]

        try:
            tasks = [x for x in request(**api_request_params)]
        except asana.error.NoAuthorizationError:
            raise errors.AsanaAuthenticationError('the authentication method supplied returned as unauthorized')
        data_points = [GanttData.from_asana(x,
                                            use_html_description = use_html_description,
                                            connection_callback = connection_callback,
                                            connection_kwargs = connection_kwargs)
                       for x in tasks]

        self.data = data_points

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
                   series_kwargs = None):
        """Create a 
        :class:`GanttSeries <highcharts_gantt.options.series.gantt.GanttSeries>`
        instance from an `Asana <https://www.asana.com/>`__ project.
        
        .. note::
        
          **Highcharts Gantt for Python** can create an Asana API client for you, 
          authenticating using the :term:`Personal Access Token` method supported by
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
          
          .. tip::
          
            You can find your Asana Project GID in your browser URL bar:
            
            .. figure:: /_static/asana-project-gid.png
              :align: center
              :alt: Asana Project GID

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
          constructor, besides the :meth:`.to <highcharts_gantt.options.series.data.connect.DataConnection.to>` 
          property which is derived from the task. Defaults
          to :obj:`None <python:None>`
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

        :returns: A :class:`GanttSeries <highcharts_gantt.options.series.gantt.GanttSeries>`
          populated with data from the indicated Asana project/section.
        :rtype: :class:`GanttSeries <highcharts_gantt.options.series.gantt.GanttSeries>`
        
        :raises HighchartsDependencyError: if the 
          `asana <https://pypi.org/project/asana/>`__ Python library is not available 
          in the runtime environment.
          
        :raises HighchartsValueError: if ``connection_callback`` is not 
          :obj:`None <python:None>`, but is not callable
        :raises HighchartsValueError: if ``asana_client`` is not 
          :obj:`None <python:None>`, but is not a valid :class:`asana.client.Client>`
          instance
        :raises AsanaAuthenticationError: if ``asana_client`` is not authenticated or 
          if no personal access token is supplied
        """
        series_kwargs = validators.dict(series_kwargs, allow_empty = True) or {}
        
        instance = cls(**series_kwargs)
        instance.load_from_asana(project_gid,
                                 section_gid = section_gid,
                                 completed_since = completed_since,
                                 use_html_description = use_html_description,
                                 personal_access_token = personal_access_token,
                                 asana_client = asana_client,
                                 api_request_params = api_request_params,
                                 connection_kwargs = connection_kwargs,
                                 connection_callback = connection_callback)

        return instance

    def load_from_monday(self,
                         board_id,
                         api_token = None,
                         template = None,
                         property_column_map = None,
                         connection_kwargs = None,
                         connection_callback = None):
        """Update the :class:`GanttSeries <highcharts_gantt.options.series.gantt.GanttSeries>` instance 
        with data from a `Monday.com <https://www.monday.com>`__ work board.
        
        :param board_id: The ID of the Monday.com board whose items should be retrieved
          to populate the Gantt series.
          
          .. tip::
            
            You can find your Asana Project GID in your browser URL bar:
              
            .. figure:: /_static/monday-board-id.png
              :align: center
              :alt: Monday.com Board ID

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
          property which is derived from the task. Defaults
          to :obj:`None <python:None>`
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
        
        :raises HighchartsDependencyError: if the 
          `monday <https://pypi.org/project/monday/>`__ Python library is not available 
          in the runtime environment
        :raises MondayAuthenticationError: if there is no Monday.com API token supplied
        :raises HighchartsValueError: if both ``template`` and ``property_column_map`` 
          are empty
        
        """
        tasks = monday.get_tasks(board_id, api_token = api_token)

        data_points = [GanttData.from_monday(tasks[x],
                                             template = template,
                                             property_column_map = property_column_map,
                                             connection_kwargs = connection_kwargs,
                                             connection_callback = connection_callback) for x in tasks]

        self.data = data_points

    @classmethod
    def from_monday(cls,
                    board_id,
                    api_token = None,
                    template = None,
                    property_column_map = None,
                    connection_kwargs = None,
                    connection_callback = None,
                    series_kwargs = None):
        """Create a :class:`GanttSeries <highcharts_gantt.options.series.gantt.GanttSeries>` instance from a 
        `Monday.com <https://www.monday.com>`__ work board.
        
        :param board_id: The ID of the Monday.com board whose items should be retrieved
          to populate the Gantt series.
          
          .. tip::
            
            You can find your Asana Project GID in your browser URL bar:
              
            .. figure:: /_static/monday-board-id.png
              :align: center
              :alt: Monday.com Board ID

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
          property which is derived from the task. Defaults
          to :obj:`None <python:None>`
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

        :returns: A :class:`GanttSeries <highcharts_gantt.options.series.gantt.GanttSeries>`
          populated with data from the indicated Asana project/section.
        :rtype: :class:`GanttSeries <highcharts_gantt.options.series.gantt.GanttSeries>`
        
        :raises HighchartsDependencyError: if the 
          `monday <https://pypi.org/project/monday/>`__ Python library is not available 
          in the runtime environment
        :raises MondayAuthenticationError: if there is no Monday.com API token supplied
        :raises HighchartsValueError: if both ``template`` and ``property_column_map`` 
          are empty
        
        """
        series_kwargs = validators.dict(series_kwargs, allow_empty = True) or {}

        tasks = monday.get_tasks(board_id, api_token = api_token)
        data_points = [GanttData.from_monday(tasks[x],
                                             template = template,
                                             property_column_map = property_column_map,
                                             connection_kwargs = connection_kwargs,
                                             connection_callback = connection_callback) for x in tasks]
        
        instance = cls(**series_kwargs)
        instance.data = data_points

        return instance

    def load_from_jira(self,
                       project_key,
                       server = None,
                       jql = None,
                       username = None,
                       password_or_token = None,
                       oauth_dict = None,
                       client_kwargs = None,
                       jira_client = None,
                       connection_kwargs = None,
                       connection_callback = None):
        """Update the
        :class:`GanttSeries <highcharts_gantt.options.series.gantt.GanttSeries>`
        instance with data from an `Atlassian JIRA <https://www.atlassian.com/>`__ project.
        
        .. note::
        
          **Highcharts Gantt for Python** can create a JIRA API client for you, 
          authenticating using either the :term:`Basic Authentication` or 
          :term:`Access Token` methods supported by the JIRA API. However, if you wish to 
          use the more-involved OAuth2 handshake, you can do so yourself and either
          
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
        
        :raises HighchartsDependencyError: if the `jira <https://jira.readthedocs.io/>`__
          Python library is not available in the runtime environment.
        :raises JIRAAuthenticationError: if no authentication details are provided or if
          the authentication process fails
        :raises JIRAProjectNotFoundError: if the ``project_key`` is not found in the JIRA
          ``server`` indicated
          
          .. tip::
          
            This can happen if authentication fails silently, which can happen when using the
            JIRA Cloud environment.
          
        :raises HighchartsValueError: if other keyword arguments are misconfigured

        """
        if not HAS_JIRA:
            raise errors.HighchartsDependencyError('The .from_jira() method depends '
                                                   'on the jira Python library. This '
                                                   'library was not found in the '
                                                   'runtime environment. Please install'
                                                   ' and try again.')

        if not jira_client:
            client_kwargs = validators.dict(client_kwargs, allow_empty = True) or {}
            if not server:
                server = os.getenv('HIGHCHARTS_JIRA_SERVER',
                                   client_kwargs.get('server', 'https://jira.atlassian.com'))

            client_kwargs['server'] = validators.url(server, allow_special_ips = True)

            project_key = validators.string(project_key)

            username = validators.string(username, allow_empty = True) \
                or os.getenv('HIGHCHARTS_JIRA_USERNAME', None)
            password_or_token = validators.string(password_or_token, allow_empty = True) \
                or os.getenv('HIGHCHARTS_JIRA_TOKEN', None)

            use_basic = oauth_dict is None and username is not None
            use_token = oauth_dict is None and username is None
            
            if use_basic:
                client_kwargs['basic_auth'] = (username, password_or_token)
            elif use_token:
                client_kwargs['token_auth'] = password_or_token
            elif oauth_dict is not None:
                client_kwargs['oauth'] = validators.dict(oauth_dict, 
                                                         allow_empty = False)
            else:
                raise errors.JIRAAuthenticationError('no authentication details '
                                                     'provided')
            try:
                jira_client = jira.JIRA(**client_kwargs)
            except jira.JIRAError as error:
                if error.status_code == 401:
                    raise errors.JIRAAuthenticationError('JIRA failed to authenticate')
                else:
                    raise error
        else:
            if not isinstance(jira_client, jira.client.JIRA):
                raise errors.HighchartsValueError(f'jira_client must be a valid '
                                                  f'jira.client.JIRA instance. Was: '
                                                  f'{jira_client.__class__.__name__}')

        if not jira_client._session:
            raise errors.JIRAAuthenticationError('jira_client is not authenticated')

        if jql and f'project = {project_key}' not in jql and f'project={project_key}' not in jql:
            raise errors.HighchartsValueError(f'jql contains a project reference '
                                                f'that does not match project_key '
                                                f'("{project_key}").')    
        elif not jql:
            jql = f'project = {project_key}'

        try:
            issues = jira_client.search_issues(jql)
        except jira.JIRAError as error:
            if error.status_code == 400:
                raise errors.JIRAProjectNotFoundError(f'No JIRA project with key "{project_key}" '
                                                      f'was found. Note that this may be because '
                                                      f'your authentication failed silently, '
                                                      f'a common issue when using JIRA Cloud.')
            else:
                raise error

        if issues.total > len(issues):
            issues.extend(jira_client.search_issues(jql, startAt = len(issues)))

        data_points_with_none = [
            GanttData.from_jira(x,
                                connection_kwargs = connection_kwargs,
                                connection_callback = connection_callback)
            for x in issues
        ]

        data_points = [x for x in data_points_with_none if x is not None]

        self.data = data_points
        
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
                  series_kwargs = None):
        """Create a 
        :class:`GanttSeries <highcharts_gantt.options.series.gantt.GanttSeries>`
        instance from an `Atlassian JIRA <https://www.atlassian.com/>`__ project.
        
        .. note::
        
          **Highcharts Gantt for Python** can create a JIRA API client for you, 
          authenticating using either the :term:`Basic Authentication` or 
          :term:`Access Token` methods supported by the JIRA API. However, if you wish to use the more-involved OAuth2 
          handshake, you can do so yourself and either
          
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

        :returns: A :
          class:`GanttSeries <highcharts_gantt.options.series.gantt.GanttSeries>`
          populated with data from the indicated JIRA project.
        :rtype: :class:`GanttSeries <highcharts_gantt.options.series.gantt.GanttSeries>`

        :raises HighchartsDependencyError: if the `jira <https://jira.readthedocs.io/>`__
          Python library is not available in the runtime environment.
        :raises JIRAAuthenticationError: if no authentication details are provided or if
          the authentication process fails
        :raises JIRAProjectNotFoundError: if the ``project_key`` is not found in the JIRA
          ``server`` indicated
          
          .. tip::
          
            This can happen if authentication fails silently, which can happen when using the
            JIRA Cloud environment.
          
        :raises HighchartsValueError: if other keyword arguments are misconfigured

        """
        series_kwargs = validators.dict(series_kwargs, allow_empty = True) or {}
        
        instance = cls(**series_kwargs)

        instance.load_from_jira(project_key = project_key,
                                server = server,
                                jql = jql,
                                username = username,
                                password_or_token = password_or_token,
                                oauth_dict = oauth_dict,
                                client_kwargs = client_kwargs,
                                jira_client = jira_client,
                                connection_kwargs = connection_kwargs,
                                connection_callback = connection_callback)

        return instance

    @classmethod
    def _data_collection_class(cls):
        """Returns the class object used for the data collection.
        
        :rtype: :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
          descendent
        """
        return GanttDataCollection

    @classmethod
    def _data_point_class(cls):
        """Returns the class object used for individual data points.
        
        :rtype: :class:`DataBase <highcharts_core.options.series.data.base.DataBase>` 
          descendent
        """
        return GanttData
