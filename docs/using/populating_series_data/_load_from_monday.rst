.. code-block:: python

  # Given a GanttSeries named "my_series" and an Monday.com Board ID of "123456"
  my_series.load_from_monday(board_id = '123456')

.. tip::

    **Where to find my Monday.com Board ID?**

    Of course, you can find your Monday.com Board ID using the Monday.com API, but that is typically
    a bit cumbersome. The easiest way to find it is to simply grab it out of your browser's URL
    bar:

    .. figure:: /_static/monday_board_id.png
      :align: center
      :alt: Monday.com Board ID

.. collapse::  Method Signature

    .. seealso::

      * :meth:`GanttSeries.from_monday() <highcharts_gantt.options.series.gantt.GanttSeries.from_monday>`
      * :meth:`Chart.from_monday() <highcharts_gantt.chart.Chart.from_monday>`
      * :meth:`GanttData.from_monday() <highcharts_gantt.options.series.data.GanttData.from_monday>`

    .. method:: .load_from_monday(self, board_id, api_token = None, template = None, property_column_map = None, connection_kwargs = None, connection_callback = None)
      :noindex:
    
      Update the :class:`GanttSeries <highcharts_gantt.options.series.gantt.GanttSeries>` instance 
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
      
