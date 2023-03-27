.. code-block:: python

  # Given a GanttSeries named "my_series" and a JIRA project key of "ABCD"
  my_series.load_from_jira(project_key = 'ABCD')

.. collapse::  Method Signature

    .. seealso::

      * :meth:`GanttSeries.from_jira() <highcharts_gantt.options.series.gantt.GanttSeries.from_jira>`
      * :meth:`Chart.from_jira() <highcharts_gantt.chart.Chart.from_jira>`
      * :meth:`GanttData.from_jira() <highcharts_gantt.options.series.data.GanttData.from_jira>`

    .. method:: .load_from_jira(self, project_key, server = None, jql = None, username = None, password_or_token = None, oauth_dict = None, client_kwargs = None, jira_client = None, connection_kwargs = None, connection_callback = None)
      :noindex:

      Update the :class:`GanttSeries <highcharts_gantt.options.series.gantt.GanttSeries>`
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
