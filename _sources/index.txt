.. pylatte documentation master file, created by
   sphinx-quickstart on Thu Jan 31 14:26:23 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pylatte
===================================

.. image:: http://pylatte.org/image/pylatte.png

Pylatte : A Web Framework Based on Python 3 Pylatte is a web framework created specifically for Python 3. Pylatte is used pyl code to make web site. pyl code is compose to python and HTML. so pyl code seem like php code. easy to learn, easy to run.
        
Sample code
-----------
The following code is a example pyl file.

.. code-block:: guess
   
	<p>Pylatte</p>
	{$
	pyl = "HTML" + " + " + "python"
	$}
	<p>
	{$=pyl$}
	</p>

The pyl code is translated by Pylatte to HTML in the browser.

.. code-block:: guess
        
   <p>Pylatte</p>
   <p>
   HTML + python
   </p>
        
Functions
---------
Translation Engine Pylatte uses pyl file format. pyl consists of HTML and Python. pyl is fully translated by the Pylatte engine into HTML. It is unique feature of Pylatte.
        
Database
--------
To use the database, external library must be installed: the mysql(for mysql) module or pymongo3(for MonogoDB) module for Python 3.
        
Simple and advanced SQL via specific functions that are similar to iBATIS are provided.
        
Session
-------
A session is needed to distinguish each client.
        
Filter
------
If a filter is set, select pages pass through the filter.
        
Form File
---------
It is possible to upload a file to server via POST.
        
URL Mapping
-----------
For security purposes, URL mapping transfers virtual URLs accessed by clients to web pages.



Download
===================================

.. toctree::
   :maxdepth: 2

   download

Install
===================================

.. toctree::
   :maxdepth: 2

   install

Tutorial
===================================
.. toctree::
   :maxdepth: 2

   tutorial

F A Q
===================================

.. toctree::
   :maxdepth: 2

   faq

Contact us
===================================

.. toctree::
   :maxdepth: 2

   contact

history
===================================
*2011. 05. 13
	The Pylatte project is created in Busan, South Korea.
*2011. 09. 02
	Initial design and development of the Pylatte project.
*2011. 10. 31
	Pylatte v0.9 released.
*2012. 03. 09
	Pylatte v0.95 released. PLY code translate engine is change. we adapt PYL(Python Lex-YACC) at PLY code translate engine
*2012. 06. 27
	Pylatte is supported MongoDB.
*2012. 08. 06
	Pylatte is released as pylatte module.
*2012. 08. 27
	Pylatte is registered in pypi. http://pypi.python.org/pypi/Pylatte/0.9.7
*2013. 02. 03
	Pylatte v1.0 released. pylatte is used wsgi.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

