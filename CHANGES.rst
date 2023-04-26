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

