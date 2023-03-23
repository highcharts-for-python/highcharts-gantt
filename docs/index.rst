.. image:: _static/highcharts-for-python-light-150x149.png
  :alt: Highcharts Gantt for Python - High-end Gantt Chart Visualization for the Python Ecosystem
  :align: right
  :width: 150
  :height: 149

|
|

###################################################
Highcharts Gantt for Python
###################################################

**High-end Gantt chart visualization for the Python ecosystem**

.. include:: _unit_tests_code_coverage.rst

.. toctree::
  :hidden:
  :maxdepth: 3
  :caption: Contents

  Home <self>
  Quickstart: Patterns and Best Practices <quickstart>
  Supported Visualizations <visualizations>
  FAQ <faq>
  Toolkit Components and Roadmap <toolkit>
  Using Highcharts for Python <using>
  API Reference <api>
  Error Reference <errors>
  Getting Help <support>
  Contributor Guide <contributing>
  Testing Reference <testing>
  Release History <history>
  Glossary <glossary>
  License <license>

.. sidebar:: Version Compatibility

  **Highcharts Gantt for Python** is designed to be compatible with:

    * Python 3.10 or higher
    * Highcharts JS 10.2 or higher
    * Highcharts Stock for Python 1.0 or higher
    * Highcharts Core for Python 1.0 or higher
    * Jupyter Notebook 6.4 or higher
    * IPython 8.10 or higher
    * Pandas 1.3 or higher
    * PySpark 3.3 or higher
    * Asana 3.0 or higher
    * Monday 1.3 or higher
    * Python-Jira 3.4 or higher

**Highcharts Gantt for Python** is an extension to the
`Highcharts Stock for Python <https://stock-docs.highchartspython.com>`__ library, and provides
a Python wrapper for the fantastic
`Highcharts Gantt <https://www.highcharts.com/products/gantt/>`__
JavaScript data visualization library. **Highcharts Gantt for Python** also supports

  * **Highcharts Core** - the core Highcharts data visualization library
  * **Highcharts Stock** - the time-series data visualization extension to Highcharts Core
  * The **Highcharts Export Server** - enabling the programmatic creation of static
    (downloadable) data visualizations

In order to integrate **Highcharts Gantt for Python** into the Python ecosystem, the
library features native integration with:

  * **Asana**. Automatically generate :term:`Gantt charts <Gantt chart>` from your Asana projects.
  * **Monday.com**. Automatically generate Gantt charts from your Monday.com boards.
  * **JIRA**. Automatically generate Gantt charts from your Jira projects.
  * **Jupyter Labs/Notebook**. You can now produce high-end and interactive Gantt charts using the 
    full suite of Highcharts visualization capabilities.
  * **Pandas**. Automatically produce data visualizations from your Pandas dataframes
  * **PySpark**. Automatically produce data visualizations from data in a PySpark
    dataframe.

.. contents::
  :depth: 3
  :backlinks: entry

---------------------

*********************************
Installation
*********************************

.. include:: _installation.rst

Dependencies
===============

.. include:: _dependencies.rst

*********************************
Why Highcharts for Python?
*********************************

Odds are you are aware of
`Highcharts Gantt <https://www.highcharts.com/products/gantt/>`__. If not, why not? Built as an extension to 
`Highcharts Core <https://www.highcharts.com/products/highcharts/>`__, it is a powerful JavaScript data visualization 
library for rendering rich :term:`Gantt charts <Gantt chart>`.

If you are building a web or mobile app/dashboard that will be
visualizing project or timeline data in some fashion, you should absolutely take a
look at the Highcharts suite of solutions. Just take a look at some of their fantastic
`Highcharts Gantt demo visualizations <https://www.highcharts.com/demo/gantt>`__.

Highcharts Gantt is a JavaScript library, and is an extension of the
`Highcharts Core <https://www.highcharts.com/products/highcharts/>`__ JavaScript library. It
is written in JavaScript, and is specifically used to configure and render data
visualizations in a web browser (or other JavaScript-executing, like mobile app)
environment. As a JavaScript library, its audience is JavaScript developers. But what
about the broader ecosystem of Python developers and data scientists?

Python is increasingly used as the technology of choice for data science and for
the backends of leading enterprise-grade applications. In other words, Python is
often the backend that delivers data and content to the front-end...which then renders it
using JavaScript and HTML.

There are numerous Python frameworks (Django, Flask, Tornado, etc.) with specific
capabilities to simplify integration with Javascript frontend frameworks (React, Angular,
VueJS, etc.). But facilitating that with Highcharts has historically been very difficult.
Part of this difficulty is because the Highcharts JavaScript suite - while supporting JSON as a
serialization/deserialization format - leverages
:term:`JavaScript object literals <JavaScript Object Literal Notation>` to expose the
full power and interactivity of its data visualizations. And while it's easy to serialize
JSON from Python, serializing and deserializing to/from JavaScript object literal notation
is much more complicated. This means that Python developers looking to integrate with
Highcharts typically had to either invest a lot of effort, or were only able to leverage
a small portion of Highcharts' rich functionality.

So I wrote the **Highcharts for Python** toolkit to bridge that gap, and
**Highcharts Gantt for Python** to provide full support for the
`Highcharts Gantt <https://www.highcharts.com/products/gantt/>`__ library extension.

**Highcharts Gantt for Python** provides support for
the `Highcharts Gantt <https://www.highcharts.com/products/stock/>`__ extension, which is
designed to Gantt and timeline data visualization capabilities optimized for
project management data visualization, with extensive technical indicators and
robust interactivity. For ease of use, it also includes the full functionality of
**Highcharts Stock for Python** as well.

Key Highcharts Gantt for Python Features
==============================================

* **Clean and consistent API**. No reliance on "hacky" code, :class:`dict <python:dict>`
  and JSON serialization, or impossible to maintain / copy-pasted "spaghetti code".
* **Comprehensive Highcharts support**. Every single Highcharts chart type and every
  single configuration option is supported in **Highcharts Gantt for Python**. This
  includes the over 70 data visualization types supported by
  `Highcharts Core <https://www.highcharts.com/product/highcharts/>`__ and the
  50+ technical indicator visualizations available in
  `Highcharts Stock <https://www.highcharts.com/product/stock/>`__, with full support for
  the rich JavaScript formatter (JS :term:`callback functions <callback function>`)
  capabilities that are often needed to get the most out of Highcharts' visualization and
  interaction capabilities.

  .. seealso::

    * :doc:`Supported Visualizations <visualizations>`

* **Simple JavaScript Code Generation**. With one method call, produce production-ready
  JavaScript code to render your interactive visualizations using Highcharts' rich
  capabilities.
* **Easy Chart Download**. With one method call, produce high-end static
  visualizations that can be downloaded or shared as files with your audience. Produce
  static charts using the Highsoft-provided
  :term:`Highcharts Export Server <Export Server>`, or using your own private export
  server as needed.
* **Integration with Asana, Monday.com, and Jira**. Your project data likely lives in
  a modern project management platform like Asana, Monday.com, and Jira. You can easily
  pull data from those platforms into your **Highcharts Gantt** visualizations using
  one method call.
* **Integration with Pandas and PySpark**. With two lines of code, produce a high-end
  interactive visualization of your Pandas or PySpark dataframe.
* **Consistent Code Style**. For Python developers, switching between Pythonic code
  conventions and JavaScript code conventions can be...annoying. So
  **Highcharts for Python** applies Pythonic syntax with automatic conversion between
  Pythonic ``snake_case`` notation and JavaScript ``camelCase`` styles.

|

**Highcharts Gantt for Python** vs Alternatives
=====================================================

.. include:: _versus_alternatives.rst

---------------------

********************************
Hello World, and Basic Usage
********************************

1. Import Highcharts Gantt for Python
==========================================

.. include:: using/_importing.rst

2. Create Your Chart
================================

  .. code-block:: python

    # from a JavaScript file
    my_chart = highcharts.Chart.from_js_literal('my_js_literal.js')

    # from a JSON file
    my_chart = highcharts.Chart.from_json('my_json.json')

    # from a Python dict
    my_chart = highcharts.Chart.from_dict(my_dict_obj)

    # from Asana
    my_chart = highcharts.Chart.from_asana(project_gid = MY_ASANA_PROJECT_ID)

    # from Monday.com
    my_chart = highcharts.Chart.from_monday(board_id = MY_MONDAY_BOARD_ID)

    # from JIRA
    my_chart = highcharts.Chart.from_jira(project_id = MY_JIRA_PROJECT_KEY)

    # from a Pandas dataframe
    my_chart = highcharts.Chart.from_pandas(df,
                                            property_map = {
                                                'x': 'transactionDate',
                                                'y': 'invoiceAmt',
                                                'id': 'id'
                                            },
                                            series_type = 'line')

    # from a PySpark dataframe
    my_chart = highcharts.Chart.from_pyspark(df,
                                             property_map = {
                                                 'x': 'transactionDate',
                                                 'y': 'invoiceAmt',
                                                 'id': 'id'
                                             },
                                             series_type = 'line')

    # from a CSV
    my_chart = highcharts.Chart.from_csv('/some_file_location/filename.csv'
                                         column_property_map = {
                                            'x': 0,
                                            'y': 4,
                                            'id': 14
                                         },
                                         series_type = 'line')

    # from a HighchartsOptions configuration object
    my_chart = highcharts.Chart.from_options(my_options)

    # from a Series configuration
    my_chart = highcharts.Chart.from_series(my_series)


3. Configure Global Settings (optional)
=============================================

  .. code-block:: python

    # Import SharedGanttOptions
    from highcharts_gantt.global_options.shared_options import SharedGanttOptions

    # from a JavaScript file
    my_global_settings = SharedGanttOptions.from_js_literal('my_js_literal.js')

    # from a JSON file
    my_global_settings = SharedGanttOptions.from_json('my_json.json')

    # from a Python dict
    my_global_settings = SharedGanttOptions.from_dict(my_dict_obj)

    # from a HighchartsOptions configuration object
    my_global_settings = SharedGanttOptions.from_options(my_options)


4. Configure Your Chart / Global Settings
================================================

  .. code-block:: python

    from highcharts_gantt.options.title import Title
    from highcharts_gantt.options.credits import Credits

    # Using dicts
    my_chart.title = {
        'align': 'center'
        'floating': True,
        'text': 'The Title for My Chart',
        'use_html': False,
    }

    my_chart.credits = {
        'enabled': True,
        'href': 'https://www.highcharts.com/',
        'position': {
            'align': 'center',
            'vertical_align': 'bottom',
            'x': 123,
            'y': 456
        },
        'style': {
            'color': '#cccccc',
            'cursor': 'pointer',
            'font_size': '9px'
        },
        'text': 'Chris Modzelewski'
    }

    # Using direct objects
    from highcharts_gantt.options.title import Title
    from highcharts_gantt.options.credits import Credits

    my_title = Title(text = 'The Title for My Chart', floating = True, align = 'center')
    my_chart.options.title = my_title

    my_credits = Credits(text = 'Chris Modzelewski', enabled = True, href = 'https://www.highcharts.com')
    my_chart.options.credits = my_credits


5. Generate the JavaScript Code for Your Chart
=================================================

Now having configured your chart in full, you can easily generate the JavaScript code
that will render the chart wherever it is you want it to go:

  .. code-block:: python

    # as a string
    js_as_str = my_chart.to_js_literal()

    # to a file (and as a string)
    js_as_str = my_chart.to_js_literal(filename = 'my_target_file.js')


6. Generate the JavaScript Code for Your Global Settings (optional)
=========================================================================

  .. code-block:: python

    # as a string
    global_settings_js = my_global_settings.to_js_literal()

    # to a file (and as a string)
    global_settings_js = my_global_settings.to_js_literal('my_target_file.js')


7. Generate a Static Version of Your Chart
==============================================

  .. code-block:: python

    # as in-memory bytes
    my_image_bytes = my_chart.download_chart(format = 'png')

    # to an image file (and as in-memory bytes)
    my_image_bytes = my_chart.download_chart(filename = 'my_target_file.png',
                                             format = 'png')

--------------

***********************
Getting Help/Support
***********************

.. include:: _support.rst

-----------------

*********************
Contributing
*********************

We welcome contributions and pull requests! For more information, please see the
:doc:`Contributor Guide <contributing>`. And thanks to all those who've already
contributed:

.. include:: _contributors.rst

-------------------

*********************
Testing
*********************

We use `TravisCI <http://travisci.org>`_ for our build automation and
`ReadTheDocs <https://readthedocs.org>`_ for our documentation.

Detailed information about our test suite and how to run tests locally can be
found in our :doc:`Testing Reference <testing>`.

--------------------

********************
Indices and tables
********************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. target-notes::

.. include:: links.txt
