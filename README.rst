###################################################
Highcharts Gantt for Python
###################################################

**High-end Gantt chart visualization for the Python ecosystem**

**Highcharts Gantt for Python** is an extension to the
`Highcharts Stock for Python <https://stock-docs.highchartspython.com>`__ library, and provides
a Python wrapper for the fantastic
`Highcharts Gantt <https://www.highcharts.com/products/gantt/>`__
JavaScript data visualization library. **Highcharts Gantt for Python** also supports

  * **Highcharts Core (JS)** - the core Highcharts data visualization library
  * **Highcharts Stock (JS)** - the Highcharts extension providing time series and asset price data visualization
  * The **Highcharts Export Server** - enabling the programmatic creation of static
    (downloadable) data visualizations

In order to integrate **Highcharts Gantt for Python** into the Python ecosystem, the
library features native integration with:

  * **Jupyter Labs/Notebook**. You can now produce high-end and interactive plots and
    renders using the full suite of Highcharts visualization capabilities.
  * **Pandas**. Automatically produce data visualizations from your Pandas dataframes
  * **PySpark**. Automatically produce data visualizations from data in a PySpark
    dataframe.
  * **Asana**. You can generate Gantt charts from your Asana projects using one simple method call.
  * **Monday.com**. Produce Gantt charts automatically from your Monday.com projects.
  * **JIRA**. Generate Gantt charts from your Atlassian JIRA Cloud projects.

**COMPLETE DOCUMENTATION:** http://gantt-docs.highchartspython.com/en/latest/index.html

--------------------

***************
Installation
***************

To install **Highcharts Gantt for Python**, just execute:

  .. code-block:: bash

    $ pip install highcharts-gantt

-------------

*********************************
Why Highcharts for Python?
*********************************

Odds are you are aware of
`Highcharts Gantt <https://www.highcharts.com/products/gantt/>`__. If not, why not?
It is the world's most popular, most powerful, category-defining JavaScript data
visualization library and - in particular - for time and resource allocation data.

If you are building a web or mobile app/dashboard that will be
visualizing time/resource data, you should absolutely take a
look at the Highcharts suite of solutions. Just take a look at some of their fantastic
`Highcharts Gantt demo visualizations <https://www.highcharts.com/demo/gantt>`__.

Highcharts Gantt is a JavaScript library, and is an extension of the
`Highcharts Stock <https://www.highcharts.com/products/stock/>`__ JavaScript library. It
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
Part of this difficulty is because the Highcharts JavaScript suite - while supporting JSON
as a serialization/deserialization format - leverages
JavaScript object literals to expose the
full power and interactivity of its data visualizations. And while it's easy to serialize
JSON from Python, serializing and deserializing to/from JavaScript object literal notation
is much more complicated. This means that Python developers looking to integrate with
Highcharts typically had to either invest a lot of effort, or were only able to leverage
a small portion of Highcharts' rich functionality.

So I wrote the **Highcharts for Python** toolkit to bridge that gap, and
**Highcharts Gantt for Python** to provide full support for the
`Highcharts Gantt <https://www.highcharts.com/products/gantt/>`__ library extension.

**Highcharts Gantt for Python** provides support for
the `Highcharts Gantt <https://www.highcharts.com/products/maps/>`__ extension, which is
designed to provide extensive data visualization capabilities optimized for project,
time, and resource allocation data visualization with robust interactivity. For ease of
use, it also includes the full functionality of **Highcharts for Python** as well.

Key Highcharts Gantt for Python Features
==============================================

* **Clean and consistent API**. No reliance on "hacky" code, ``dict``
  and JSON serialization, or impossible to maintain / copy-pasted "spaghetti code".
* **Comprehensive Highcharts support**. Every single Highcharts chart type and every
  single configuration option is supported in **Highcharts Gantt for Python**. This
  includes the over 70 data visualization types supported by
  `Highcharts Core <https://www.highcharts.com/product/highcharts/>`__, and the 50+ 
  visualizations supported by `Highcharts Stock <https://www.highcharts.com/products/stock/>`__ 
  and the multiple Gantt visualizations available in
  `Highcharts Gantt <https://www.highcharts.com/product/gantt/>`__, with full support for
  the rich JavaScript formatter (JS callback functions)
  capabilities that are often needed to get the most out of Highcharts' visualization and
  interaction capabilities.

  .. note::

    **See Also:**

    * `Supported Visualizations <https://gantt-docs.highchartspython.com/en/latest/visualizations.html>`__

* **Simple JavaScript Code Generation**. With one method call, produce production-ready
  JavaScript code to render your interactive visualizations using Highcharts' rich
  capabilities.
* **Easy Chart Download**. With one method call, produce high-end static
  visualizations that can be downloaded or shared as files with your audience. Produce
  static charts using the Highsoft-provided **Highcharts Export Server**, or using your own private export
  server as needed.
* **Consistent Code Style**. For Python developers, switching between Pythonic code
  conventions and JavaScript code conventions can be...annoying. So
  **Highcharts for Python** applies Pythonic syntax with automatic conversion between
  Pythonic ``snake_case`` notation and JavaScript ``camelCase`` styles.

|

**Highcharts Gantt for Python** vs Alternatives
===================================================

For a discussion of **Highcharts Gantt for Python** in comparison to alternatives, please see
the **COMPLETE DOCUMENTATION:** http://gantt-docs.highchartspython.com/en/latest/index.html

---------------------

********************************
Hello World, and Basic Usage
********************************

1. Import Highcharts Gantt for Python
==========================================

  .. code-block:: python
    
    # BEST PRACTICE!
    # PRECISE LOCATION PATTERN
    # This method of importing Highcharts Gantt for Python objects yields the fastest
    # performance for the import statement. However, it is more verbose and requires
    # you to navigate the extensive Highcharts Gantt for Python API.

    # Import classes using precise module indications. For example:
    from highcharts_gantt.chart import Chart
    from highcharts_gantt.global_options.shared_options import SharedGanttOptions
    from highcharts_gantt.options import HighchartsGanttOptions
    from highcharts_gantt.options.plot_options.gantt import GanttOptions
    from highcharts_gantt.options.series.gantt import GanttSeries

    # CATCH-ALL PATTERN
    # This method of importing Highcharts Gantt for Python classes has relatively slow
    # performance because it imports hundreds of different classes from across the entire
    # library. This is also a known anti-pattern, as it obscures the namespace within the
    # library. Both may be acceptable to you in your use-case, but do use at your own risk.

    # Import objects from the catch-all ".highcharts" module.
    from highcharts_gantt import highcharts

    # You can now access specific classes without individual import statements.
    highcharts.Chart
    highcharts.SharedGanttOptions
    highcharts.HighchartsGanttOptions
    highcharts.GanttOptions
    highcharts.GanttSeries


2. Create Your Chart
================================

  .. code-block:: python

    # from a JavaScript file
    my_chart = highcharts.Chart.from_js_literal('my_js_literal.js')

    # from a JSON file
    my_chart = highcharts.Chart.from_json('my_json.json')

    # from a Python dict
    my_chart = highcharts.Chart.from_dict(my_dict_obj)

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

*********************
Questions and Issues
*********************

You can ask questions and report issues on the project's
`Github Issues Page <https://github.com/highcharts-for-python/highcharts-gantt/issues>`_

-----------------

*********************
Contributing
*********************

We welcome contributions and pull requests! For more information, please see the
`Contributor Guide <https://gantt-docs.highchartspython.com/en/latest/contributing.html>`. And thanks to all those who've already contributed!

-------------------

*********************
Testing
*********************

We use `TravisCI <http://travisci.org>`_ for our build automation and
`ReadTheDocs <https://readthedocs.org>`_ for our documentation.

Detailed information about our test suite and how to run tests locally can be
found in our Testing Reference.
