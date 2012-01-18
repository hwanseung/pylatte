# -*- coding: utf-8 -*- 
import formFile
class tutorial:
	result=""
	sessionDic=dict()
	def __init__(self,param,pyFile,session,headerInfo,lattedb):
		self.generate(param,pyFile,session,headerInfo,lattedb)

	def generate(self,param,pyFile,session,headerInfo,lattedb):

		self.result+=str("""<!DOCTYPE html>
		 """)
		self.result+=str("""<html>
			 """)
		self.result+=str("""<head>
			 """)
		self.result+=str("""<meta name="viewport" content="width=device-width, initial-scale=1">
			 """)
		self.result+=str("""<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
			 """)
		self.result+=str("""<title>Pylatte - Web framework based on Python3 """)
		self.result+=str("""</title>
			
			 """)
		self.result+=str("""<!-- favicon -->
			 """)
		self.result+=str("""<link rel="shortcut icon" href="../pyl/favicon.ico" type="image/x-icon">
			 """)
		self.result+=str("""<link rel="icon" href="../pyl/favicon.ico" type="image/x-icon">
		
			 """)
		self.result+=str("""<!-- Include required JS files -->
			 """)
		self.result+=str("""<script type="text/javascript" src="../pyl/syntaxhighlighter/js/xregexp.js"> """)
		self.result+=str("""</script>
			 """)
		self.result+=str("""<script type="text/javascript" src="../pyl/syntaxhighlighter/js/shCore.js"> """)
		self.result+=str("""</script>
			 
			 """)
		self.result+=str("""<!--
			    At least one brush, here we choose JS. You need to include a brush for every
			    language you want to highlight
			-->
			 """)
		self.result+=str("""<script type="text/javascript" src="../pyl/syntaxhighlighter/lang/shBrushXml.js"> """)
		self.result+=str("""</script>
			 """)
		self.result+=str("""<script type="text/javascript" src="../pyl/syntaxhighlighter/lang/shBrushBash.js"> """)
		self.result+=str("""</script>
			 
			 """)
		self.result+=str("""<!-- Include *at least* the core style and default theme -->
			 """)
		self.result+=str("""<link href="../pyl/syntaxhighlighter/css/shCore.css" rel="stylesheet" type="text/css" />
			 """)
		self.result+=str("""<link href="../pyl/syntaxhighlighter/css/shThemeDefault.css" rel="stylesheet" type="text/css" />
			
			
			
			 """)
		self.result+=str("""<link rel="stylesheet"  href="../pyl/css/jquery.mobile-1.0rc2.css"/>
			 """)
		self.result+=str("""<link rel="stylesheet"  href="../pyl/css/jqm-docs.css"/>
			
			 """)
		self.result+=str("""<script src="../pyl/js/jquery-1.6.4.min.js"> """)
		self.result+=str("""</script>
			 """)
		self.result+=str("""<script src="../pyl/js/jqm-docs.js"> """)
		self.result+=str("""</script>
			 """)
		self.result+=str("""<script src="../pyl/js/jquery.mobile.themeswitcher.js"> """)
		self.result+=str("""</script>
			 """)
		self.result+=str("""<script src="../pyl/js/jquery.mobile-1.0rc2.js"> """)
		self.result+=str("""</script>
			
			 """)
		self.result+=str("""<script type="text/javascript">
		
			  var _gaq = _gaq || [];
			  _gaq.push(['_setAccount', 'UA-26668199-1']);
			  _gaq.push(['_trackPageview']);
			
			  (function() {
			    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
			    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
			    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
			  })();
			
			 """)
		self.result+=str("""</script>
			
			 """)
		self.result+=str("""</head>
		
		 """)
		self.result+=str("""<body>
			 """)
		self.result+=str("""<div data-role="page" class="type-interior">
		
				 """)
		self.result+=str("""<div data-role="header" data-theme="b">
				 """)
		self.result+=str("""<h1>Pylatte Official Webpage """)
		self.result+=str("""</h1>
				 """)
		self.result+=str("""<a href="../../" target="_self" data-icon="home" data-iconpos="notext" data-direction="reverse" class="ui-btn-right jqm-home">Home """)
		self.result+=str("""</a>
			 """)
		self.result+=str("""</div> """)
		self.result+=str("""<!-- /header -->
		
			 """)
		self.result+=str("""<div data-role="content">
					 """)
		self.result+=str("""<div class="content-primary">
					 """)
		self.result+=str("""<h1>Tutorial """)
		self.result+=str("""</h1>
						
					 """)
		self.result+=str("""<h2>Hello Pylatte """)
		self.result+=str("""</h2>
						 """)
		self.result+=str("""<p>Let's print  """)
		self.result+=str("""<i>Hello Pylatte """)
		self.result+=str("""</i>on pylatte tutorial as a first step. First of all, open a text editor, and it will be saved as  """)
		self.result+=str("""<i>hellopy. """)
		self.result+=str("""<b>pyl """)
		self.result+=str("""</b> """)
		self.result+=str("""</i> """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<p>You can use python code in pyl file format on pylatte. pyl consists of HTML and python. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<p>To make pyl page working on pylatte, wrap python code with  """)
		self.result+=str("""<b>&lt;$ """)
		self.result+=str("""</b> and  """)
		self.result+=str("""<b>$&gt; """)
		self.result+=str("""</b>. And if you put your  """)
		self.result+=str("""<i>variable """)
		self.result+=str("""</i> between  """)
		self.result+=str("""<b>&lt;$= """)
		self.result+=str("""</b> and  """)
		self.result+=str("""<b>$&gt; """)
		self.result+=str("""</b> such as  """)
		self.result+=str("""<b>&lt;$= """)
		self.result+=str("""</b> """)
		self.result+=str("""<i>variable """)
		self.result+=str("""</i> """)
		self.result+=str("""<b>$&gt; """)
		self.result+=str("""</b>, the  """)
		self.result+=str("""<i>variable """)
		self.result+=str("""</i> will be automatically printed on the web page by pylatte translation module.  """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<p>Caution : If you use  """)
		self.result+=str("""<b>print() """)
		self.result+=str("""</b> function, it will be printed on web server console. """)
		self.result+=str("""</p>
					
						 """)
		self.result+=str("""<pre class="brush: xml">
						 """)
		self.result+='<$'
		self.result+=str("""
						hi="hello pylatte"
						$>
						 """)
		self.result+=str("""<h1> """)
		self.result+='<$'
		self.result+=str("""=hi$> """)
		self.result+=str("""</h1>
						 """)
		self.result+=str("""</pre>
						 """)
		self.result+=str("""<p>In python language, indentation is absolutely important. So we strongly recommend to use python code under  """)
		self.result+=str("""<b>&lt;$ """)
		self.result+=str("""</b>, and type  """)
		self.result+=str("""<b>$&gt; """)
		self.result+=str("""</b> on new line after python code. Refer to the following code. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<p>Type the code in hellopy.pyl and save it again. After running pylatte web server, you can see  """)
		self.result+=str("""<b>hello pylatte """)
		self.result+=str("""</b>.
					
					 """)
		self.result+=str("""<h2>Starting pylatte web server """)
		self.result+=str("""</h2>
						 """)
		self.result+=str("""<p>Basically, default port number is 80 on HTTP. If you want, you can change port number in  """)
		self.result+=str("""<i>pylatte_config.xml """)
		self.result+=str("""</i> """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<pre class="brush: xml">
							 """)
		self.result+=str("""<pylatte-server>
								 """)
		self.result+=str("""<port>80 """)
		self.result+=str("""</port>
							 """)
		self.result+=str("""</pylatte-server>
						 """)
		self.result+=str("""</pre>
						 """)
		self.result+=str("""<p>There are many options in  """)
		self.result+=str("""<i>pylatte_config.xml """)
		self.result+=str("""</i>. To change port number, we need to focus on only &lt;pylatte-server&gt; tag. Modify the value of &lt;port&gt; tag from default port(80) to what you want(e.g. 8000). """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<p>Caution : You have to check if the port number is being used by another program before you change. """)
		self.result+=str("""</p>
						
						 """)
		self.result+=str("""<p>To start pylatte web server, move to appropriate path where pylatte is installed and run following command into terminal. If operating system is Windows, just execute the latteServerStart.py file. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<pre class="brush: bash">
							sudo python3 latteServerStart.py
						 """)
		self.result+=str("""</pre>
						 """)
		self.result+=str("""<p>There are just one more step to see  """)
		self.result+=str("""<b>hello pylatte """)
		self.result+=str("""</b>. Take URL Mapping below. """)
		self.result+=str("""</p>
						
					 """)
		self.result+=str("""<h2>URL Mapping """)
		self.result+=str("""</h2>
						 """)
		self.result+=str("""<p>To make pylatte security safe, it is neccesary to fix &lt;pylatte&gt; and &lt;pylatte-mapping&gt; tag in  """)
		self.result+=str("""<i>pylatte_config.xml """)
		self.result+=str("""</i> """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<pre class="brush: xml">
							 """)
		self.result+=str("""<pylatte>
								 """)
		self.result+=str("""<pylatte-name>hello_pylatte """)
		self.result+=str("""</pylatte-name>
								 """)
		self.result+=str("""<pylatte-pyl>hellopy.pyl """)
		self.result+=str("""</pylatte-pyl>
							 """)
		self.result+=str("""</pylatte>
							 """)
		self.result+=str("""<pylatte-mapping>
								 """)
		self.result+=str("""<pylatte-name>hello_pylatte """)
		self.result+=str("""</pylatte-name>
								 """)
		self.result+=str("""<url-mapping>/py """)
		self.result+=str("""</url-mapping>
							 """)
		self.result+=str("""</pylatte-mapping>	
						 """)
		self.result+=str("""</pre>
						 """)
		self.result+=str("""<p>&lt;pylatte-name&gt; value(e.g. hello_pylatte) in &lt;pylatte&gt; and &lt;pylatte-mapping&gt; is just name to identify each mapping information. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<p>&lt;pylatte-pyl&gt; value(e.g. hellopy.pyl) in &lt;pylatte&gt; is real pyl page we make. it will be accessed by &lt;url-mapping&gt; value in &lt;pylatte-mapping&gt;. Once more, you have to access http://localhost/py, NOT to http://localhost/hellopy.pyl. This can hide original url, so we think it would make pylatte securtiy much higher. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<p>Congratulation, now you can access to  """)
		self.result+=str("""<a href="http://localhost/py">http://localhost/py """)
		self.result+=str("""</a> instead of http://localhost/hellopy.pyl to see hello pylatte. """)
		self.result+=str("""</p>
						
					 """)
		self.result+=str("""<h2>Filter """)
		self.result+=str("""</h2>
						 """)
		self.result+=str("""<p>Sometimes, we need to process one same function in many pages before the pages get started. Filter module on Pylatte perfectly supports this. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<p>It can be configured in  """)
		self.result+=str("""<i>pylatte_config.xml """)
		self.result+=str("""</i>. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<pre class="brush: xml">
							 """)
		self.result+=str("""<filter>
								 """)
		self.result+=str("""<filter-name>testFilter """)
		self.result+=str("""</filter-name>
								 """)
		self.result+=str("""<filter-pyl>filter/filter.pyl """)
		self.result+=str("""</filter-pyl>
							 """)
		self.result+=str("""</filter>
							 """)
		self.result+=str("""<filter-mapping>
								 """)
		self.result+=str("""<filter-name>testFilter """)
		self.result+=str("""</filter-name>
								 """)
		self.result+=str("""<filter-url>hellopy.pyl """)
		self.result+=str("""</filter-url>
								 """)
		self.result+=str("""<filter-url>byepy.pyl """)
		self.result+=str("""</filter-url>
							 """)
		self.result+=str("""</filter-mapping>
						 """)
		self.result+=str("""</pre>
						 """)
		self.result+=str("""<p>Look at this xml code. &lt;filter-name&gt; value(e.g. testFilter) in &lt;filter&gt; and &lt;filter-mapping&gt; is just name to identify each filter information. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<p>&lt;filter-pyl&gt; value will be executed at first when you access to &lt;filter-url&gt; values. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<p>For instance, filter/filter.pyl will be executed at first when you access to byepy.pyl or hellopy.pyl in the code. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<p>So you don't need to add same code to many pages which require same function anymore. """)
		self.result+=str("""</p>
						
					 """)
		self.result+=str("""<h2>GET & POST """)
		self.result+=str("""</h2>
						 """)
		self.result+=str("""<p>There are two kinds of method to deal with GET & POST parameter. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<p>When you request some parameter values using GET method or POST method, you can get the parameter values as following. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<pre class="brush: xml">
							 """)
		self.result+='<$'
		self.result+=str("""=param$>
						 """)
		self.result+=str("""</pre>
						 """)
		self.result+=str("""<p>The variable  """)
		self.result+=str("""<b>param """)
		self.result+=str("""</b> has all requested values as dictionary type like  """)
		self.result+=str("""<i>{"id":pylatte, "password":python} """)
		self.result+=str("""</i>. Definately, you can get specific value such as following. """)
		self.result+=str("""</p> 
						 """)
		self.result+=str("""<pre class="brush: xml">
							 """)
		self.result+='<$'
		self.result+=str("""=param["id"]$>
						 """)
		self.result+=str("""</pre>
						 """)
		self.result+=str("""<p>Pylatte does not support the other methods like PUT, DELETE. """)
		self.result+=str("""</p>
						
					 """)
		self.result+=str("""<h2>Session """)
		self.result+=str("""</h2>
						 """)
		self.result+=str("""<p>Pylatte supports sesson management allocating session datas for each accessor. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<p>This session data type is dictionary. The way to use is similar with GET & POST above. Refer to following code. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<pre class="brush: xml">
							session["name"] = "pylatte"
							session["age"] = 1
						 """)
		self.result+=str("""</pre>	
						 """)
		self.result+=str("""<p>Pylatte manages session data through session module. Usually, it is required to use in membership page to deal with each member's session data.  """)
		self.result+=str("""</p>
		
					 """)
		self.result+=str("""<h2>File Upload """)
		self.result+=str("""</h2>
						 """)
		self.result+=str("""<p>You can implement file upload function with a file upload module on Pylatte. When you use &lt;form&gt; tag, it is compulsory to put attribute :  """)
		self.result+=str("""<b>enctype="multipart/form-data """)
		self.result+=str("""</b> into the tag. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<pre class="brush: xml">
						
							 """)
		self.result+=str("""<form  method="post" enctype="multipart/form-data" action="http:/localhost/pageToProcessPost">
								 """)
		self.result+=str("""<input type="file" name="filepy" />
								 """)
		self.result+=str("""<input type="sudmit" value="click" />
							 """)
		self.result+=str("""</form>
						 """)
		self.result+=str("""</pre>
						 """)
		self.result+=str("""<p>Now you can upload a file as post parameters in pageToProcessPost(This is a mapped page name by mapping module at  """)
		self.result+=str("""<i>pylatte_config.xml """)
		self.result+=str("""</i>) page. Refer to following code. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<pre class="brush: xml">
							 """)
		self.result+='<$'
		self.result+=str("""
							pyformFile=formFile.formFile(pyFile)
							pyformFile.moveUploadFile("filepy","download","pylatte.jpg")
							$>
						 """)
		self.result+=str("""</pre>
						 """)
		self.result+=str("""<p>you can receive the file information to variable with using  """)
		self.result+=str("""<b>formFile.formFile(pyFile) """)
		self.result+=str("""</b>. And execute moveUploadFile mothod from the variable to complete upload file to server. Parameters of moveUploadFile are name, folder name, and file name in order. """)
		self.result+=str("""</p> 
						 """)
		self.result+=str("""<p>In addition, pyFile[ """)
		self.result+=str("""<i>name """)
		self.result+=str("""</i>] """)
		self.result+=str("""</p> has a little information about the file as dictionary type.
					
					 """)
		self.result+=str("""<h2>Database """)
		self.result+=str("""</h2>
						 """)
		self.result+=str("""<p>First of all, to set your database, it is needed to fix &lt;sql&gt; values in  """)
		self.result+=str("""<i>db_mapping.xml """)
		self.result+=str("""</i> about MySQL connection information. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<pre class="brush: xml">
							 """)
		self.result+=str("""<sql db="mysql">
								 """)
		self.result+=str("""<host>localhost """)
		self.result+=str("""</host>
								 """)
		self.result+=str("""<user>user """)
		self.result+=str("""</user>
								 """)
		self.result+=str("""<password>password """)
		self.result+=str("""</password>
								 """)
		self.result+=str("""<dbName>pylatte """)
		self.result+=str("""</dbName>
							 """)
		self.result+=str("""</sql>
						 """)
		self.result+=str("""</pre>
						 """)
		self.result+=str("""<p>Only MySQL is an available database on Pylatte now. In &lt;sql&gt;, it is required to fill with host, user, password, database name. """)
		self.result+=str("""</p>
						
						 """)
		self.result+=str("""<h3>Simple way to use database """)
		self.result+=str("""</h3>				
						 """)
		self.result+=str("""<p> """)
		self.result+=str("""<b>&lt;@latteDatabase&gt; """)
		self.result+=str("""</b> has to be written on the code specifically before using database. After that, execute SQL what you need through  """)
		self.result+=str("""<b>latteDB.query() """)
		self.result+=str("""</b> method. And then, use  """)
		self.result+=str("""<b>latteDB.store_result() """)
		self.result+=str("""</b> method which return result of processing the SQL. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<p>The result include not only result of SQL but also some methods. To see how to use a database, check example code below. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<pre class="brush: xml">
							 """)
		self.result+=str("<@latteDatabase>")
		self.result+=str("""
							 """)
		self.result+='<$'
		self.result+=str("""					
							latteDB.query("select * from test")
							result=latteDB.store_result()
							$>
							 """)
		self.result+=str("""<div id="dbdiv">
							 """)
		self.result+='<$'
		self.result+=str("""=result.fetch_row()$>
							 """)
		self.result+=str("""</div>
						 """)
		self.result+=str("""</pre>
						 """)
		self.result+=str("""<p>This code returns tuple type result by fetch_row() """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<p> """)
		self.result+=str("""<b>fetch_row() """)
		self.result+=str("""</b> method takes some additional parameters.  """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<p>The first one is, how many rows (maxrows) should be returned. By default, it returns one row. It may return fewer rows than you asked for, but never more. If you set maxrows=0, it returns all rows of the result set. If you ever get an empty tuple back, you ran out of rows. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<pt>The second parameter (how) tells it how the row should be represented. By default, it is zero which means, return as a tuple. how=1 means, return it as a dictionary, where the keys are the column names, or table.column if there are two columns with the same name (say, from a join). how=2 means the same as how=1 except that the keys are always table.column. """)
		self.result+=str("""</p>
						
						 """)
		self.result+=str("""<h3>Advanced way to use database """)
		self.result+=str("""</h3>
						 """)
		self.result+=str("""<p> """)
		self.result+=str("""<b>&lt;@latteDatabaseExt&gt; """)
		self.result+=str("""</b> has to be written on the code specifically before using database. 
						 """)
		self.result+=str("""<p>In this case, DBMappingParser class and db_mapping.xml file are required to use. Refer to following code. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<pre class="brush: xml">
							 """)
		self.result+=str("""<sqlMap id="user">
								 """)
		self.result+=str("""<select id="select1">SELECT * FROM table """)
		self.result+=str("""</select>
								 """)
		self.result+=str("""<select id="select2">SELECT * FROM table WHERE age = $age$ """)
		self.result+=str("""</select>
								 """)
		self.result+=str("""<insert id="insert1">INSERT INTO table VALUES ($name$, $age$) """)
		self.result+=str("""</insert>
								 """)
		self.result+=str("""<update id="update1">UPDATE table SET age = $age$ WHERE name = $name$ """)
		self.result+=str("""</update>
								 """)
		self.result+=str("""<delete id="delete1">DELETE FROM table WHERE age = $age$ """)
		self.result+=str("""</delete>
							 """)
		self.result+=str("""</sqlMap>
						 """)
		self.result+=str("""</pre>
						 """)
		self.result+=str("""<p>This is xml code in  """)
		self.result+=str("""<i>db_mapping.xml file """)
		self.result+=str("""</i>. &lt;sqlMap&gt; tag needs attribute 'id'. And its child nodes (e.g. select, insert, update, delete ...) also need attribute 'id'. These 'id' are used to call SQL which is values of the childe nodes. Let's see how to deal with database using these SQLs. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<pre class="brush: xml">
							 """)
		import DBMappingParser
		self.result+=str("""t>
							 """)
		self.result+='<$'
		self.result+=str("""
							db = DBMappingParser.pyLatteDBMappingParser()
							parameter = {"age":1, "name":"pylatte"}
							
							result1 = db.queryForList("user.select1")	
							result2 = db.queryForList("user.select2", parameter)
							$>
						 """)
		self.result+=str("""</pre>
						 """)
		self.result+=str("""<p>First of all, declare on variable and call DBMappingParser.pyLatteDBMappingParser() to save database object to the variable. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<p>Secondly, define dictionary type parameter. This will be replaced matched value in SQL. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<p>At last, call queryForList() method via the variable declared on first step. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<p>queryForList() method takes two parameters. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<p>First one indicates specific SQL in db_mapping.xml by id. For example, 'user.select1' indicates a value in specific tag which has id 'select1' in &lt;sqlMap&gt; tag having id 'user'. So 'user.select1' get replaced to "SELECT * FROM test" """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<p>Second parameter is optional. When SQL indicated by first parameter includes variable $keys$, this is mandatory. As you see above example code, second parameter is dictionary type. In the parameter, the each values automatically gets replaced with each matched $keys$ in SQL. So select2 will be traslated from  """)
		self.result+=str("""<b>SELECT * FROM test WHERE age = $age$ """)
		self.result+=str("""</b> to  """)
		self.result+=str("""<b>SELECT * FROM test WHERE age = 1 """)
		self.result+=str("""</b> """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<p>queryForList() method returns tuple type as a result. """)
		self.result+=str("""</p>
						
									
					 """)
		self.result+=str("""<h2>Server Information """)
		self.result+=str("""</h2>
						 """)
		self.result+=str("""<p>It is possible to get HTTP header information that you required to Pylatte web server. It is also saved as dictionary type. Refer to following code to see how to use it in pyl. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<pre class="brush: xml">
							 """)
		self.result+='<$'
		self.result+=str("""=headerInfo["User-Agent"]$>
							 """)
		self.result+='<$'
		self.result+=str("""=headerInfo["Accept-Encoding"]$>
						 """)
		self.result+=str("""</pre>
						 """)
		self.result+=str("""<p>There are planty of header information. Pylatte support most common header information. """)
		self.result+=str("""</p>
					 """)
		self.result+=str("""</div> """)
		self.result+=str("""<!--/content-primary -->
		
					 """)
		self.result+=str("""<div class="content-secondary">
		
						 """)
		self.result+=str("""<div data-role="collapsible" data-collapsed="true" data-theme="b" data-content-theme="d">
		
								 """)
		self.result+=str("""<h3>More in this section """)
		self.result+=str("""</h3>
		
								 """)
		self.result+=str("""<ul data-role="listview" data-theme="c" data-dividertheme="d">
									 """)
		self.result+=str("""<li data-role="list-divider">Menu """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<li> """)
		self.result+=str("""<a target="_self" href="../index">About """)
		self.result+=str("""</a> """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<li> """)
		self.result+=str("""<a target="_self" href="../download">Download """)
		self.result+=str("""</a> """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<li> """)
		self.result+=str("""<a target="_self" href="../install">Install """)
		self.result+=str("""</a> """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<li data-theme="b"> """)
		self.result+=str("""<a target="_self" href="../tutorial">Tutorial """)
		self.result+=str("""</a> """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<li> """)
		self.result+=str("""<a target="_self" href="../documentation">Documentation """)
		self.result+=str("""</a> """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<li> """)
		self.result+=str("""<a target="_self" href="../comment">Comment """)
		self.result+=str("""</a> """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<li> """)
		self.result+=str("""<a target="_self" href="../faq">F A Q """)
		self.result+=str("""</a> """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<li> """)
		self.result+=str("""<a target="_self" href="../contactus">Contact us """)
		self.result+=str("""</a> """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<img src="../pyl/image/pylatte.png"> """)
		self.result+=str("""</img>
								 """)
		self.result+=str("""</ul>
						 """)
		self.result+=str("""</div>
					 """)
		self.result+=str("""</div>
		
				 """)
		self.result+=str("""</div> """)
		self.result+=str("""<!-- /content -->
		
				 """)
		self.result+=str("""<div data-role="footer" class="footer-docs" data-theme="b">
						 """)
		self.result+=str("""<h4>&copy; 2011 The Pylatte Project """)
		self.result+=str("""</h4>
				 """)
		self.result+=str("""</div>
		
				 """)
		self.result+=str("""</div> """)
		self.result+=str("""<!-- /page -->
			
				 """)
		self.result+=str("""</body>
			 """)
		self.result+=str("""<!-- Finally, to actually run the highlighter, you need to include this JS on your page -->
			 """)
		self.result+=str("""<script type="text/javascript">
				SyntaxHighlighter.all()
			 """)
		self.result+=str("""</script>
		 """)
		self.result+=str("""</html>
		
		
		 """)
		self.sessionDic=session
		pass
	def getHtml(self):
		return self.result
		pass
	def getSession(self):
		return self.sessionDic
		pass
