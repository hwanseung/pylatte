============
Tutorial
============
Did you install pylatte module? If you don't install pylatte moudle, you must go install page to progress step.

we need least 3 files to execute pylatte. python code to execute pylatte server and xml file to setting pylatte server pyl(compose of HTML and Python) file to show webpage.

Hello Pylatte
===============
Let's print Hello Pylatteon pylatte tutorial as a first step. First of all, open a text editor, and it will be saved as hellopy.pyl in pyl directory.

You can use python code in pyl file format on pylatte. pyl consists of HTML and python.

To make pyl page working on pylatte, wrap python code with <$ and $>. And if you put your variable between <$= and $> such as <$=variable$>, the variable will be automatically printed on the web page by pylatte translation module.

Caution : If you use print() function, it will be printed on web server console.

.. code-block:: guess
   
	<p>Pylatte</p>
	{$
	hi="hello pylatte"
	$}
	<p>
	{$=hi$}
	</p>

In python language, indentation is absolutely important. So we strongly recommend to use python code under {$, and type $} on new line after python code. Refer to the following code.

Type the code in hellopy.pyl and save it again. After running pylatte web server, you can see hello pylatte.

Setting pylatte web server
=============================
Basically, default port number is 80 on HTTP. If you want, you can change port number in pylatte_config.xml

.. code-block:: guess
	
	<pylatte-server>
		<port>8080</port>
	</pylatte-server>
	
There are many options in pylatte_config.xml. To change port number, we need to focus on only <pylatte-server> tag. Modify the value of <port> tag from default port(80) to what you want(e.g. 8000).

Caution : You have to check if the port number is being used by another program before you change.

URL Mapping
============
To make pylatte security safe, it is neccesary to fix <pylatte> and <pylatte-mapping> tag in pylatte_config.xml

.. code-block:: guess
	
	<pylatte>
		<pylatte-name>hello_pylatte</pylatte-name>
		<pylatte-pyl>hellopy.pyl</pylatte-pyl>
	</pylatte>
	<pylatte-mapping>
		<pylatte-name>hello_pylatte</pylatte-name>
		<url-mapping>/py</url-mapping>
	</pylatte-mapping>  
	
<pylatte-name> value(e.g. hello_pylatte) in <pylatte> and <pylatte-mapping> is just name to identify each mapping information.

<pylatte-pyl> value(e.g. hellopy.pyl) in <pylatte> is real pyl page we make. it will be accessed by <url-mapping> value in <pylatte-mapping>. Once more, you have to access http://localhost/py, NOT to http://localhost/hellopy.pyl. This can hide original url, so we think it would make pylatte securtiy much higher.

Start Pylatte Server
======================
must be make python code to excute pylatte

.. code-block:: python

	import pylatte.web.latteServerStart as latteServerStart
	latteServerStart.start()

To start pylatte web server, move to appropriate path where pylatte is installed and run following command into terminal on ubuntu. if operating system is Windows, just execute the latteServerStart.py file.

Congratulation, now you can access to http://localhost/py instead of http://localhost/hellopy.pyl to see hello pylatte.

Filter
======
Sometimes, we need to process one same function in many pages before the pages get started. Filter module on Pylatte perfectly supports this.

It can be configured in pylatte_config.xml.

.. code-block:: guess

	<filter>
		<filter-name>testFilter</filter-name>
		<filter-pyl>filter/filter.pyl</filter-pyl>
	</filter>
	<filter-mapping>
		<filter-name>testFilter</filter-name>
		<filter-url>hellopy.pyl</filter-url>
		<filter-url>byepy.pyl</filter-url>
	</filter-mapping>
	
Look at this xml code. <filter-name> value(e.g. testFilter) in <filter> and <filter-mapping> is just name to identify each filter information.

<filter-pyl> value will be executed at first when you access to <filter-url> values.

For instance, filter/filter.pyl will be executed at first when you access to byepy.pyl or hellopy.pyl in the code.

So you don't need to add same code to many pages which require same function anymore.

GET & POST
===========
There are two kinds of method to deal with GET & POST parameter.

When you request some parameter values using GET method or POST method, you can get the parameter values as following.

.. code-block:: none
	
	{$=param$}

The variable param has all requested values as dictionary type like {"id":pylatte, "password":python}. Definately, you can get specific value such as following.

.. code-block:: none
	
	{$=param["id"]$}
	
Pylatte does not support the other methods like PUT, DELETE.

Session
========

Pylatte supports sesson management allocating session datas for each accessor.

This session data type is dictionary. The way to use is similar with GET & POST above. Refer to following code.

.. code-block:: python
	
	session["name"] = "pylatte"
	session["age"] = 1

Pylatte manages session data through session module. Usually, it is required to use in membership page to deal with each member's session data.

File Upload
============

You can implement file upload function with a file upload module on Pylatte. When you use <form> tag, it is compulsory to put attribute : enctype="multipart/form-data" into the tag.

.. code-block:: guess
	
	<form method="post" enctype="multipart/form-data" action="http:/localhost/pageToProcessPost">
		<input type="file" name="filepy">
		<input type="sudmit" value="click">
	</form>

Now you can upload a file as post parameters in pageToProcessPost(This is a mapped page name by mapping module at pylatte_config.xml) page. Refer to following code.

.. code-block:: none
	
	{$
	pyformFile=formFile.formFile()
	pyformFile.moveUploadFile(pyFile['file1'],"image","log.jpeg")
	$}

you can receive the file information to variable with using formFile.formFile(). And execute moveUploadFile mothod from the variable to complete upload file to server. Parameters of moveUploadFile are uploadFile, folder name, and file name in order.

Database
=========
First of all, to set your database, it is needed to fix <sql> values in db_mapping.xml about MySQL or MongoDB connection information.

.. code-block:: guess

	<sql db="mysql">
		<host>localhost</host>
		<user>user</user>
		<password>password</password>
		<dbname>pylatte</dbname>
	</sql>

.. code-block:: guess

	<sql db="mongodb">
		<host>localhost</host>
		<port>27017</port>
	</sql>
	
In <sql>, it is required to fill with host, user, password, database name in My SQL Setting. but MongoDB need host, port information

Simple way to use database
------------------------------
latteDatabase() has to be written on the code specifically before using database. 

mysql
^^^^^^

After that, execute SQL what you need through latteDB.query() method. And then, use latteDB.store_result() method which return result of processing the SQL.
The result include not only result of SQL but also some methods. To see how to use a database, check example code below.

.. code-block:: html

	<$
	latteDatabase()             
	latteDB.query("""select * from test""")
	result=latteDB.store_result()
	$>
	<div id="dbdiv">
	<$=result.fetch_row()$>
	</div>

This code returns tuple type result by fetch_row()
fetch_row() method takes some additional parameters.

The first one is, how many rows (maxrows) should be returned. By default, it returns one row. It may return fewer rows than you asked for, but never more. If you set maxrows=0, it returns all rows of the result set. If you ever get an empty tuple back, you ran out of rows.

The second parameter (how) tells it how the row should be represented. By default, it is zero which means, return as a tuple. how=1 means, return it as a dictionary, where the keys are the column names, or table.column if there are two columns with the same name (say, from a join). how=2 means the same as how=1 except that the keys are always table.column.

MongoDB
^^^^^^^^

collec=latteDB.test If you write this context, you can use "test" collection of MongoDB. you can access "test" Collecation into "collec" variable.

.. code-block:: none

	<$
	latteDatabase()
	collec = latteDB.test
	print(collec)
	$>

If you need more detail information, you can get more infomation in https://github.com/mongodb/mongo-python-driver.

Advanced way to use database
--------------------------------
caution : mongoDB is not support this way.
latteDatabaseExt() has to be written on the code specifically before using database.

In this case, DBMappingParser class and db_mapping.xml file are required to use. Refer to following code.

.. code-block:: guess

	<sqlMap id="demo">
		<select id="select">SELECT * FROM demo</select>
		<insert id="insert">insert into demo (name) values ($name$);</insert>
		<update id="update">UPDATE demo SET name = $name$ WHERE uid = $uid$</update>
		<delete id="delete">DELETE FROM demo WHERE uid = $uid$</delete>
	</sqlMap>
	
This is xml code in db_mapping.xml file. <sqlMap> tag needs attribute 'id'. And its child nodes (e.g. select, insert, update, delete ...) also need attribute 'id'. These 'id' are used to call SQL which is values of the childe nodes. Let's see how to deal with database using these SQLs.


.. code-block:: html

	{$
	latteDatabaseExt()
	$}
	{$
	contact = pyLatteDBMappingParser.pyLatteDBMappingParser()
	result = contact.queryForList("demo.select")
	$}
	{$
	for item in result:
	$}
	<div>
		<input type='radio' name='uid' id='radio-choice-{$=item["uid"]$}' value='{$=item["uid"]$}' />
		<label for='radio-choice-{$=item["uid"]$}'>{$=item["uid"]$} : {$=item["name"]$}</label>
	</div>
	{$
		pass
	$}
	
First of all, declare on variable and call DBMappingParser.pyLatteDBMappingParser() to save database object to the variable.

Secondly, define dictionary type parameter. This will be replaced matched value in SQL.

At last, call queryForList() method via the variable declared on first step.

queryForList() method takes two parameters.

First one indicates specific SQL in db_mapping.xml by id. For example, 'user.select1' indicates a value in specific tag which has id 'select1' in <sqlMap> tag having id 'user'. So 'user.select1' get replaced to "SELECT * FROM test"

Second parameter is optional. When SQL indicated by first parameter includes variable $keys$, this is mandatory. As you see above example code, second parameter is dictionary type. In the parameter, the each values automatically gets replaced with each matched $keys$ in SQL. So select2 will be traslated from SELECT * FROM test WHERE age = $age$ to SELECT * FROM test WHERE age = 1

queryForList() method returns tuple type as a result.

Server Information
====================
It is possible to get HTTP header information that you required to Pylatte web server. It is also saved as dictionary type. Refer to following code to see how to use it in pyl.

.. code-block:: guess

	<p>{$=headerInfo['PATH_INFO']$}</p>
	<p>{$=headerInfo['HTTP_ACCEPT']$}</p>
	<p>{$=headerInfo['SERVER_NAME']$}</p>
	<p>{$=headerInfo['HTTP_USER_AGENT']$}</p>

There are planty of header information. Pylatte support most common header information.
