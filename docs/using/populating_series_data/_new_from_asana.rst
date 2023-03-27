  .. note::

    The ``.from_asana()`` method is available on the :class:`Chart <highcharts_gantt.chart.Chart>` and 
    :class:`GanttSeries <highcharts_gantt.options.series.gantt.GanttSeries>` classes, allowing you to 
    either assemble a series or an entire chart from an Asana project with only one method call.

.. code-block:: python

  from highcharts_gantt.chart import Chart
  from highcharts_gantt.options.series.gantt import GanttSeries

  # Create a new GanttSeries instance from an Asana project with ID 123456
  # - note that this method will automatically read your Asana Personal Access Token from
  #   the ASANA_PERSONAL_ACCESS_TOKEN environment variable. You can also supply it
  #   directly using the "personal_access_token" keyword argument.
  my_series = GanttSeries.from_asana(project_gid = '123456')

  # Create a new Chart instance from an Asana project with ID 123456
  # - note that this method will automatically read your Asana Personal Access Token from
  #   the ASANA_PERSONAL_ACCESS_TOKEN environment variable. You can also supply it
  #   directly using the "personal_access_token" keyword argument.
  my_chart = Chart.from_asana(project_gid = '123456')

.. tip::

    **Where to find my Asana Project GID?**

    Of course, you can find your Asana Project GID using the Asana API, but that is typically
    a bit cumbersome. The easiest way to find it is to simply grab it out of your browser's URL
    bar:

    .. figure:: /_static/asana_project_gid.png
      :align: center
      :alt: Asana Project GID

.. collapse::  Method Signature

    .. seealso::

      * :meth:`Chart.from_asana() <highcharts_gantt.chart.Chart.from_asana>`
      * :meth:`GanttData.from_asana() <highcharts_gantt.options.series.data.GanttData.from_asana>`

    .. method:: .from_asana(cls, project_gid, section_gid = None, completed_since = None, use_html_description = True, personal_access_token = None, asana_client = None, api_request_params = None, connection_kwargs = None, connection_callback = None, series_kwargs = None)
      :noindex:
      :classmethod:

      Create a :class:`GanttSeries <highcharts_gantt.options.series.gantt.GanttSeries>`
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