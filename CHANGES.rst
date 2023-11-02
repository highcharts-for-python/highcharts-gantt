
Release 1.5.0
=========================================

* **ENHANCEMENT:** Align the API to **Highcharts (JS) v.11.2** (#127). In particular, this includes:

  * Added ``.radius`` support to Connectors.
  * Added Navigator ``.accessibility`` support.
  * Added ``.class_name`` to Stock Tools definitions.
  * Added reversal support to Fibonacci Stock Tools.
  * Added ``AxisEvents.point_break_out`` property.
  * Added ``.node_alignment`` property to ``SankeyOptions`` and ``SankeySeries``.
  * Added ``.link_color_mode`` property to ``SankeyOptions`` and ``SankeySeries``.
  * Added ``.inactive_other_points`` property to multiple series types.
  * Added ``.grouping`` property to Lollipop series type.
  * Added ``.low_marker`` property Area Range and Dumbell series types.
  * Added ``.show_export_in_progress`` and ``.export_in_progress`` support.
  * Added ``.drag`` annotation event support.
  
* **BUGFIX:** Fixed missing ``.levels`` support in ``TreegraphOptions`` and ``TreegraphSeries``.

-----------------------

Release 1.4.0
=========================================

* **MAJOR** performance gains in the ``.to_js_literal()`` method. Implementation seems to
  improve performance by 50 - 90%.
* *SIGNIFICANT* performance gains in the ``.to_json()`` method. Implementation seems to 
  improve performance by 30 - 90%.
* **ENHANCEMENT:** Significantly simplified use of the ``.from_pandas()`` method to support:

  * creation of multiple series from one DataFrame in one method call
  * creation of series without needing to specify a full property map
  * support for creating series by DataFrame row, rather than just by DataFrame column

* **ENHANCEMENT:** Added the ``.from_pandas_in_rows()`` method to support creation of
  charts and series from simple two-dimensional DataFrames laid out in rows.
* **ENHANCEMENT:** Added one-shot chart creation and rendering from Series objects.
* **ENHANCEMENT:** Added one-shot chart creation using ``series`` and ``data``/``series_type`` keywords.
* **ENHANCEMENT:** Added ``.convert_to()`` convenience method to Series objects.
* **ENHANCEMENT:** Added ``CallbackFunction.from_python()`` method which converts a Python function
  to its JavaScript equivalent using generative AI, with support for both OpenAI and Anthropic.
* **BUGFIX:** Fixed instability issues in Jupyter Notebooks, both when operating as a Notebook (outside of 
  Jupyter Lab) and when saved to a static HTML file.

---------------------

Release 1.3.0
=========================================

* **ENHANCEMENT:** Modified the way that data points are serialized to JavaScript literal objects. Now, they are serialized to a JavaScript array if their configured properties are those that Highcharts (JS) supports in JavaScript array notation. Otherwise, the code falls back to serialize the data point as a JavaScript object literal. This change is intended to improve performance and reduce the size of the serialized data. (#32)
* **ENHANCEMENT:** Added ``__repr__()`` method for Highcharts Core for Python classes.
* **ENHANCEMENT:** Added ``__str__()`` method with special handling for difficult-to-read classes.
* **ENHANCEMENT:** Added ``Chart.get_script_tags()`` to retrieve Javascript ``<script>`` tags.
* **ENHANCEMENT:** Added ``utility_functions.to_snake_case()`` function.
* **BUGFIX:** Fixed incorrect serialization of datetime and Pandas ``Timestamp`` objects in ``.to_dict()`` and ``.to_json()``.
* **BUGFIX:** Fixed incorrect serialization of ``EnforcedNull`` in ``.to_dict()`` and ``.to_json()``.

------------------

Release 1.2.3
=========================================

* **BUGFIX:** Fixed refernece bug in serialization of ``GanttData`` instances with timezone-naive ``datetime`` instances in ``start and ``end``.

------------------

Release 1.2.2
=========================================

* **BUGFIX:** Fixed support for serialization of ``GanttData`` instances with timezone-naive ``datetime`` instances in ``start and ``end``. Closes #29.
* **DOCS:** Fixed broken links in documentation to ``options.series.gantt.GanttSeries`` and ``options.series.data.gantt.GanttData``. Closes #28.

------------------

Release 1.2.1
=========================================

* **BUGFIX:** Fixed incorrect ``datetime`` serialization to SECONDS from Unix epoch. Now serializing to JS-compatible MILLISECONDS from Unix epoch.

------------------

Release 1.2.0
=========================================

* **ENHANCEMENT:** Align the API to **Highcharts (JS) v.11.1** (#22). In particular, this includes:

  * Changes inherited from **Highcharts Core for Python v.1.2.0**. See `here <https://core-docs.highchartspython.com/en/latest/history.html#release-1-2-0>`__.

* **ENHANCEMENT:** Added support for the inclusion of scripts based on features used in the chart (#7).
* **ENHANCEMENT:** Added ``dict`` support to ``.style`` property on labels and titles.
* **DOCS:** Various documentation updates and fixes.
* **DEPENDENCY:** Bumped ``requests`` version for security patch.

---------------

Release 1.1.0
=========================================

* Align the API to **Highcharts (JS) v.11**. In particular, this includes:

  * Changes inherited from **Highcharts Core for Python v.1.1.0**. See `here <https://core-docs.highchartspython.com/en/latest/history.html#release-1-1-0>`__.

* **FIXED:** Fixed missing ``TreegraphOptions`` / ``TreegraphSeries`` series type.

---------------

Release 1.0.1
=========================================

* Added documentation of "hard" dependencies to the README.
* Fixed broken links in documentation to ``options.plot_options.heatmap.HeatmapOptions`` 
  and ``options.plot_options.heatmap.TilemapOptions``.

------------------

Release 1.0.0
=========================================

* **First official release!**
* Fixed over-eager logical filtering on ``options.series.data.GanttData`` instantiation.

---------------

Release 1.0.0-rc6
=========================================

* Added demos to documentation.
* Fixed ``options.series.gantt.GanttSeries`` documentation.
* Aligned Jupyter display to new Highcharts Core signature.
* Added ``datetime.date`` (as opposed to ``datetime.datetime`` 
  support for ``GanttSeries.start`` and ``GanttSeries.end``.

---------------

Release 1.0.0-rc5
=========================================

* Further tweaks to documentation CSS for better accessibility.

---------------

Release 1.0.0-rc4
=========================================

* Added CSS overrides to documentation for better accessibility.
* Added jQuery to documentation to address issue in Sphinx 6.0 and Sphinx RTD Theme.

-----------------

Release 1.0.0-rc3
=========================================

* Fixed unneeded ``python-dotenv`` import.
* Suppressed Asana irrelevant deprecation warnings.
* Suppressed Asana custom ``dict`` population (possibly revisit in a later version).
* Fixed JavaScript module inclusion logic in Jupyter context.

-----------------

Release 1.0.0-rc2
=========================================

* Revised documentation.

-----------------

Release 1.0.0-rc1
=========================================

* First public release: **Release Candidate 1**

