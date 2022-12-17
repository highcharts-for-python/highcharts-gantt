import os
from typing import Optional, List

from dotenv import load_dotenv
from validator_collection import validators, checkers

try:
    import asana
    HAS_ASANA = True
except ImportError:
    HAS_ASANA = False
    
try:
    import monday
    HAS_MONDAY = True
except ImportError:
    HAS_MONDAY = False

from highcharts_python.options.series.base import SeriesBase

from highcharts_gantt import errors
from highcharts_gantt.options.plot_options.gantt import GanttOptions
from highcharts_gantt.options.series.data.gantt import GanttData
from highcharts_gantt.options.series.data.connect import DataConnection
from highcharts_gantt.utility_functions import mro__to_untrimmed_dict

load_dotenv()


class GanttSeries(SeriesBase, GanttOptions):
    """Options to configure a Gantt series.

    Gantt charts are a type of chart used to visualize efforts executed in a sequence.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def data(self) -> Optional[List[GanttData]]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`GanttData` instances,
        it accepts as input an iterable of :class:`GanttData` instances or
        :class:`dict <python:dict>` instances that can be coerced to :class:`GanttData`.

        :rtype: :class:`list <python:list>` of :class:`GanttData` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not value:
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
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = mro__to_untrimmed_dict(self, in_cls = in_cls)

        return untrimmed

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

        :returns: A :class:`GanttSeries <highcharts_gantt.options.series.gantt.GanttSeries>`
          populated with data from the indicated Asana project/section.
        :rtype: :class:`GanttSeries <highcharts_gantt.options.series.gantt.GanttSeries>`
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
        
        connection_kwargs = validators.dict(connection_kwargs,
                                            allow_empty = True) or {}
        
        if connection_callback and not checkers.is_callable(connection_callback):
            raise errors.HighchartsValueError('connection_callback - if supplied - '
                                              'must be callable.')

        series_kwargs = validators.dict(series_kwargs, allow_empty = True) or {}
        
        if not personal_access_token:
            personal_access_token = os.getenv('ASANA_PERSONAL_ACCESS_TOKEN', None)
            
        if asana_client and not isinstance(asana_client, asana.client.Client):
            raise errors.HighchartsValueError(f'asana_client must be a valid asana '
                                              f'Client instance. Was: '
                                              f'{asana_client.__class__.__name__}')
        elif asana_client and not asana_client.session.token:
            raise errors.AsanaAuthenticationError('asana_client is not authenticated')
        elif asana_client:
            client = asana_client
        elif not personal_access_token:
            raise errors.AsanaAuthenticationError('from_asana() requires either a '
                                                  'personal access token or an '
                                                  'authenticated Asana client. '
                                                  'Neither was supplied.')
        else:
            client = asana.Client.access_token(personal_access_token)
    
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

        tasks = [x for x in request(**api_request_params)]
        data_points = []
        for task in tasks:
            is_milestone = task.get('resource_subtype', None) == 'milestone'
            data_point = GanttData(end = task.get('due_on', 
                                                  None) or task.get('due_at',
                                                                    None),
                                   start = task.get('start_on', 
                                                    None) or task.get('start_at',
                                                                      None),
                                   parent = task.get('parent', None),
                                   completed = task.get('completed', None),
                                   milestone = is_milestone,
                                   id = task['gid'],
                                   name = task['name'])
            if use_html_description:
                data_point.description = task.get('html_notes', None)
            else:
                data_point.description = task.get('notes', None)
            dependencies = []
            for item in task['dependencies']:
                if connection_callback:
                    connection = connection_callback(connection_target = item, 
                                                     asana_task = task)
                elif connection_kwargs:
                    connection_kwargs['to'] = item['gid']
                    connection = DataConnection(**connection_kwargs)
                else:
                    connection = item['gid']
                dependencies.append(connection)
            
            data_point.custom = task
            data_points.append(task)
        series_kwargs['data'] = data_points
        
        return cls(**series_kwargs)
