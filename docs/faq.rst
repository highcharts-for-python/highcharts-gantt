################################
Frequently Asked Questions
################################

.. contents::
  :depth: 2
  :backlinks: entry

-------------------

************************************************************
Highcharts Core for Python vs Highcharts Gantt for Python
************************************************************

**What is the difference between Highcharts Core for Python and Highcharts Gantt for Python?**

The `Highcharts Core for Python <https://core-docs.highchartspython.com/>`__ library supports
`Highcharts Core <https://www.highcharts.com/products/highcharts/>`__, which is the core
data visualization library developed by `Highsoft <https://www.highcharts.com/>`__. It
provides over 60 different visualization types.

**Highcharts Gantt for Python** is an *extension* to **Highcharts Core for Python** in the same
way that `Highcharts Gantt <https://www.highcharts.com/products/gantt/>`__ is an
*extension* to `Highcharts Core <https://www.highcharts.com/products/highcharts/>`__. Technically,
it is actually an extension *to an extension*, in that it extends `Highcharts Stock for Python <https://stock-docs.highchartspython.com/>`__ to provide:

  * new series types, including :term:`Gantt charts <gantt chart>`
  * adds support for direct integration with popular project management platforms including 
    `Asana <https://www.asana.com>`__, `Monday.com <https://www.monday.com>`__, and 
    `Atlassian JIRA <https://www.atlassian.com>`__

.. tip::

  **Highcharts Gantt for Python** *includes* all of the functionality from
  `Highcharts Stock for Python <https://stock-docs.highchartspython.com>`__ using the exact same 
  API. As a result, the best practice is that if your application needs any of the features 
  included in **Highcharts Gantt for Python**, just use that library.

**Can I use the Navigator or Stock Tools on non-Stock charts?**

Yes, you can. If you are using the Highcharts Stock :term:`stock tools` or
:term:`navigator` features, you can still use them with non-stock charts, including in **Highcharts Gantt**'s 
:class:`GanttSeries <highcharts_gantt.options.series.gantt.GanttSeries>`__, 
:class:`OrganizationSeries <highcharts_gantt.options.series.organization.OrganizationSeries>`,
or :class:`GaugeSeries <highcharts_gantt.options.series.gauge.GaugeSeries>`). This can be
particualrly useful if you are using custom :term:`stock tools` and want to maintain a
consistent user experience in your application.

---------------

***********************
Getting Help
***********************

**Where can I get help using Highcharts for Python?**

This documentation is a great place to start, but we're here to help!

.. include:: _support.rst

-----------------

***********************
Licensing
***********************

**Is the Highcharts for Python toolkit free?**

If you are evaluating the **Highcharts for Python Toolkit**, you are welcome 
to install this library and use it free of charge. 

However, if you are using it for professional purposes - either to use 
Highcharts for your work, or to build an application that integrates the library - 
then you have to pay for both Highcharts Maps (JS) itself *and* for your right 
to use the **Highcharts for Python Toolkit**. 

You can purchase licenses for both from Highsoft A/S at: 
`https://shop.highcharts.com/ <https://shop.highcharts.com>`__.

**How much does Highcharts for Python cost?**

As a paid add-on to the Highcharts JavaScript libraries, the 
**Highcharts for Python Toolkit** toolkit is priced at 30% of the price you pay 
for your Highcharts JavaScript license/support contract.

**How do I license the Highcharts for Python toolkit?**

Licensing is super easy! You can go to 
`https://shop.highcharts.com <https://shop.highcharts.com>`__ and fill out the 
form, and that's it!

----------------------

******************************
Open Source
******************************

**Is Highcharts for Python open source?**

Yes. The **Highcharts for Python Toolkit** toolkit is open source (but not free - 
see :ref:`licensing <faq_licensing>` above). 

You are welcome to review the source code for any library in the toolkit on 
`Github <https://github.com/highcharts-for-python>`__, including for 
`Highcharts Gantt for Python <https://github.com/highcharts-for-python/highcharts-gantt>`__.


**Can I fork the toolkit?**

.. warning::

  Remember that if you fork the library and make modifications to the source code, that means that we will *not* be able to provide support or technical assistance for you should you run into trouble. So you will ultimately depend on
  forks at your own risk!

Yes. You are welcome to fork any of our repositories from `Github <https://github.com/highcharts-for-python>`__, 
provided that you adhere to the terms of our :doc:`license`.

.. tip::

  Bear in mind that if you fork the repository, that does not mean you are allowed to use it for professional purposes. Even if forked, you still need a license to do so. You can purchase a license `here <https://shop.highcharts.com>`__.

**Can I contribute to the Highcharts for Python toolkit?**

Absolutely! We encourage contributions to the toolkit from the community! For more information, please read our :doc:`Contributor Guide <contributing>`.

