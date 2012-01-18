# -*- coding: utf-8 -*- 
import formFile
class documentation:
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
		self.result+=str("""<h1>Documentation """)
		self.result+=str("""</h1>
						 """)
		self.result+=str("""<div data-role="collapsible-set" data-theme="c" data-content-theme="d">
						 """)
		self.result+=str("""<div data-role="listview" data-inset="true" data-filter="true" data-filter-theme="c">
							 """)
		self.result+=str("""<div data-role="collapsible" data-collapsed="true">
								 """)
		self.result+=str("""<h3>pylatte_config.xml """)
		self.result+=str("""</h3>
								 """)
		self.result+=str("""<p>Configuration about Server port number, URL Mapping, and Filter """)
		self.result+=str("""</p>
								 """)
		self.result+=str("""<pre class="brush: xml">
									 """)
		self.result+=str("""<config>
										 """)
		self.result+=str("""<pylatte-server>
											 """)
		self.result+=str("""<port>80 """)
		self.result+=str("""</port>	 """)
		self.result+=str("""<!-- Pylatte web server port number. 80 set by default -->
										 """)
		self.result+=str("""</pylatte-server>
									
										 """)
		self.result+=str("""<latteUrl> """)
		self.result+=str("""<!-- URL Mapping pairs -->
											 """)
		self.result+=str("""<!-- From hostname/pylatte to hostname/sample.pyl -->
											 """)
		self.result+=str("""<!-- pylatte-name is a just name of each pair. -->
											 """)
		self.result+=str("""<pylatte>
												 """)
		self.result+=str("""<pylatte-name>mapping_test """)
		self.result+=str("""</pylatte-name>
												 """)
		self.result+=str("""<pylatte-pyl>sample.pyl """)
		self.result+=str("""</pylatte-pyl>
											 """)
		self.result+=str("""</pylatte>
											 """)
		self.result+=str("""<pylatte-mapping>
												 """)
		self.result+=str("""<pylatte-name>mapping_test """)
		self.result+=str("""</pylatte-name>
												 """)
		self.result+=str("""<url-mapping>/pylatte """)
		self.result+=str("""</url-mapping>
											 """)
		self.result+=str("""</pylatte-mapping>	
										 """)
		self.result+=str("""</latteUrl>
										
										 """)
		self.result+=str("""<latteFilter> """)
		self.result+=str("""<!-- Filter pairs -->
											 """)
		self.result+=str("""<!-- filter-pyl code are executed first before filter-url pages are accessed -->
											 """)
		self.result+=str("""<!-- filter-name is a just name of each pair. -->
											 """)
		self.result+=str("""<filter>
												 """)
		self.result+=str("""<filter-name>filter_test """)
		self.result+=str("""</filter-name>
												 """)
		self.result+=str("""<filter-pyl>filter/sample_filter.pyl """)
		self.result+=str("""</filter-pyl>
											 """)
		self.result+=str("""</filter>
											 """)
		self.result+=str("""<filter-mapping>
												 """)
		self.result+=str("""<filter-name>filter_test """)
		self.result+=str("""</filter-name>
												 """)
		self.result+=str("""<filter-url>documenation.pyl """)
		self.result+=str("""</filter-url>
												 """)
		self.result+=str("""<filter-url>tutorial.pyl """)
		self.result+=str("""</filter-url>
												 """)
		self.result+=str("""<filter-url>contact.pyl """)
		self.result+=str("""</filter-url>
											 """)
		self.result+=str("""</filter-mapping>
										 """)
		self.result+=str("""</latteFilter>
									 """)
		self.result+=str("""</config>
								 """)
		self.result+=str("""</pre>
							 """)
		self.result+=str("""</div>
							 """)
		self.result+=str("""<div data-role="collapsible"  data-collapsed="true">
								 """)
		self.result+=str("""<h3>db_mapping.xml """)
		self.result+=str("""</h3>
								 """)
		self.result+=str("""<p>Configuration about database information and using advanced SQL """)
		self.result+=str("""</p>
								 """)
		self.result+=str("""<pre class="brush: xml">
									 """)
		self.result+=str("""<database>
										 """)
		self.result+=str("""<sql db="mysql"> """)
		self.result+=str("""<!-- information about MySQL to connect database -->
											 """)
		self.result+=str("""<host>localhost """)
		self.result+=str("""</host>
											 """)
		self.result+=str("""<user>root """)
		self.result+=str("""</user>
											 """)
		self.result+=str("""<password>pylatte """)
		self.result+=str("""</password>
											 """)
		self.result+=str("""<dbName>pylatte """)
		self.result+=str("""</dbName>
										 """)
		self.result+=str("""</sql>
										
										 """)
		self.result+=str("""<sqlmap id="user"> """)
		self.result+=str("""<!-- SQL set-->
											 """)
		self.result+=str("""<!-- SQL list to use -->
											 """)
		self.result+=str("""<!-- $variable$ is replaced with python variable -->
										     """)
		self.result+=str("""<seIect id="select1">SELECT * FROM table """)
		self.result+=str("""</select>
										     """)
		self.result+=str("""<seIect id="select2">SELECT * FROM table WHERE age = $age$ """)
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
		self.result+=str("""</sqlmap>
									 """)
		self.result+=str("""</database>
								 """)
		self.result+=str("""</pre>
							 """)
		self.result+=str("""</div>
							 """)
		self.result+=str("""<div data-role="collapsible"  data-collapsed="true">
								 """)
		self.result+=str("""<h3>latteServerStart.py """)
		self.result+=str("""</h3>
								 """)
		self.result+=str("""<p>Turn on Pylatte web server """)
		self.result+=str("""</p>
								 """)
		self.result+=str("""<ul>
									 """)
		self.result+=str("""<li>parseServerPort() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Set a server port number by reading pylatte_config.xml """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>worker() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Work a server """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>my_service() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>checking a command from interective prompt. """)
		self.result+=str("""</p>
								 """)
		self.result+=str("""</ul>
							 """)
		self.result+=str("""</div>
							 """)
		self.result+=str("""<div data-role="collapsible"  data-collapsed="true">
								 """)
		self.result+=str("""<h3>pyLatteConfigParser Class """)
		self.result+=str("""</h3>
								 """)
		self.result+=str("""<p>This class is just for a test. """)
		self.result+=str("""</p>
								 """)
		self.result+=str("""<ul>
									 """)
		self.result+=str("""<li>__init__() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Set a Mapping information and Filter information by reading pylatte_config.xml """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>parserUrlMappingExcute() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Bring the path to access(execute) pyl file actually from a xml file """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>parseUrlMappingUrl() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Bring the virtual URL to link to one pyl file from a xml file """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>makeUrlMap() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Make dictionay mapping data pairs """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>parseFilterPyl() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Bring the path to filter pyl file actually from a xml file """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>parseFilterUrl() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Bring the path to be filtered pyl files from a xml file """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>makeFilterMap() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Make dictionay filter data pairs """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>getUrlMap() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p> """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>getDataBaseInfo() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p> """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>getFilterMap() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p> """)
		self.result+=str("""</p>
								 """)
		self.result+=str("""</ul>
							 """)
		self.result+=str("""</div>
							 """)
		self.result+=str("""<div data-role="collapsible"  data-collapsed="true">
								 """)
		self.result+=str("""<h3>pyLatteDBMappingParser Class """)
		self.result+=str("""</h3>
								 """)
		self.result+=str("""<p>To deal with database based on MySQL """)
		self.result+=str("""</p>
								 """)
		self.result+=str("""<ul>
									 """)
		self.result+=str("""<li>__init__() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Ready for reading database information """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>loadXmlFromFile() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Load XML document about database information and SQL Mapping information """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>parseDataBaseInfo() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Get database information(host, user, password, database name) from XML document
		        And Connect to MySQL to use the database """)
		self.result+=str("""</p>
		        					 """)
		self.result+=str("""<li>queryProcessing """)
		self.result+=str("""</li>
		        					 """)
		self.result+=str("""<p>Execute SQL with replacing variables in SQL. """)
		self.result+=str("""</p>
		        					 """)
		self.result+=str("""<li>queryForList() """)
		self.result+=str("""</li>
		        					 """)
		self.result+=str("""<p>Looking for matched SQL with specified id from XML document """)
		self.result+=str("""</p>
								 """)
		self.result+=str("""</ul>
							 """)
		self.result+=str("""</div>
							 """)
		self.result+=str("""<div data-role="collapsible"  data-collapsed="true">
								 """)
		self.result+=str("""<h3>formFile Class """)
		self.result+=str("""</h3>
								 """)
		self.result+=str("""<p>This class is just for a test. """)
		self.result+=str("""</p>
								 """)
		self.result+=str("""<ul>
									 """)
		self.result+=str("""<li>__init__() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Initializing variables. """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>moveUploadFile() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Upload files to indicated path. """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>getError """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Return an error message. """)
		self.result+=str("""</p>
								 """)
		self.result+=str("""</ul>
							 """)
		self.result+=str("""</div>
							 """)
		self.result+=str("""<div data-role="collapsible" data-collapsed="true">
								 """)
		self.result+=str("""<h3>latteServer Class """)
		self.result+=str("""</h3>
								 """)
		self.result+=str("""<p>This class is just for a test. """)
		self.result+=str("""</p>
								 """)
		self.result+=str("""<ul>
									 """)
		self.result+=str("""<li>__init__() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Read URL mapping and database information """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>do_GET() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>GET parameter processing """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>do_POST() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>POST parameter processing """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>do_HEAD() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Head in formation processing """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>send_head() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>This sends the response code and MIME headers. """)
		self.result+=str("""</p>
								 """)
		self.result+=str("""</ul>
							 """)
		self.result+=str("""</div>
							 """)
		self.result+=str("""<div data-role="collapsible" data-collapsed="true">
								 """)
		self.result+=str("""<h3>latteSocketServer Class """)
		self.result+=str("""</h3>
								 """)
		self.result+=str("""<p>This class is just for a test. """)
		self.result+=str("""</p>
								 """)
		self.result+=str("""<ul>
									 """)
		self.result+=str("""<li>__init__() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Server started entierly. """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>server_bind() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Binding a server """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>shutdown() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Shut down a server """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>sessionFileRemove() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Remove session files generated before """)
		self.result+=str("""</p>
								 """)
		self.result+=str("""</ul>
							 """)
		self.result+=str("""</div>
							 """)
		self.result+=str("""<div data-role="collapsible" data-collapsed="true">
								 """)
		self.result+=str("""<h3>methodGetGetParam Class """)
		self.result+=str("""</h3>
								 """)
		self.result+=str("""<p>Reading GET parameters """)
		self.result+=str("""</p>
								 """)
		self.result+=str("""<ul>
									 """)
		self.result+=str("""<li>__init__() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Parsing GET parameters from accessed URL. """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>getParam() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Return GET parameters as dictionary type. """)
		self.result+=str("""</p>
								 """)
		self.result+=str("""</ul>
							 """)
		self.result+=str("""</div>
							 """)
		self.result+=str("""<div data-role="collapsible" data-collapsed="true">
								 """)
		self.result+=str("""<h3>methodGetPostParam Class """)
		self.result+=str("""</h3>
								 """)
		self.result+=str("""<p>Reading POST parameters """)
		self.result+=str("""</p>
								 """)
		self.result+=str("""<ul>
									 """)
		self.result+=str("""<li>__init__() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Get POST parameters from a loaded page """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li> """)
		self.result+=str("""</li>getParam """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Return POST parameters as dictionary type """)
		self.result+=str("""</p>
								 """)
		self.result+=str("""</ul>
							 """)
		self.result+=str("""</div>
							 """)
		self.result+=str("""<div data-role="collapsible" data-collapsed="true">
								 """)
		self.result+=str("""<h3>postMultipartForm Class """)
		self.result+=str("""</h3>
								 """)
		self.result+=str("""<p>This class is used to send multipart/form """)
		self.result+=str("""</p>
								 """)
		self.result+=str("""<ul>
									 """)
		self.result+=str("""<li>__init__() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Save payload datas in the start """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>__splitPayload() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Split received datas """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>__analysisData() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Analysis splited datas """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>__getTmpHashKey() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Make a temporary file name. """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>getFileInfo() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Return file information. """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>getParam() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Retrun input data except for file information """)
		self.result+=str("""</p>
								 """)
		self.result+=str("""</ul>
							 """)
		self.result+=str("""</div>
							 """)
		self.result+=str("""<div data-role="collapsible" data-collapsed="true">
								 """)
		self.result+=str("""<h3>pylToPy Class """)
		self.result+=str("""</h3>
								 """)
		self.result+=str("""<p>Translation module from pyl file to py(python) file """)
		self.result+=str("""</p>
								 """)
		self.result+=str("""<ul>
									 """)
		self.result+=str("""<li>__init__() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Read a pyl file """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>translationPy() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Translate code from .pyl to .py """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>outPy() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Get original pyl name to save py file. """)
		self.result+=str("""</p>
								 """)
		self.result+=str("""</ul>
							 """)
		self.result+=str("""</div>
							 """)
		self.result+=str("""<div data-role="collapsible" data-collapsed="true">
								 """)
		self.result+=str("""<h3>requestHeaderInfo Class """)
		self.result+=str("""</h3>
								 """)
		self.result+=str("""<p>Information of request header """)
		self.result+=str("""</p>
								 """)
		self.result+=str("""<ul>
									 """)
		self.result+=str("""<li>__init__() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Generate head information from header """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>getHeaderInfo() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Return header information as dictionary type """)
		self.result+=str("""</p>
								 """)
		self.result+=str("""</ul>
							 """)
		self.result+=str("""</div>
							 """)
		self.result+=str("""<div data-role="collapsible" data-collapsed="true">
								 """)
		self.result+=str("""<h3>session Class """)
		self.result+=str("""</h3>
								 """)
		self.result+=str("""<p>Dealing with session information """)
		self.result+=str("""</p>
								 """)
		self.result+=str("""<ul>
									 """)
		self.result+=str("""<li>checkAvailableSession() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Check whether the session is valid or not. """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>genSessionKey() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Generate session file. """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>setSessionData() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Save file using generated key string """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>getSessionData() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Get session data using the session key. """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>dictToSessionData() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Change form from dictionary type to session data type """)
		self.result+=str("""</p>
									 """)
		self.result+=str("""<li>sessionDataTodict() """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<p>Change form from session data type to dictionary type """)
		self.result+=str("""</p>
								 """)
		self.result+=str("""</ul>
							 """)
		self.result+=str("""</div>
						 """)
		self.result+=str("""</div>
						 """)
		self.result+=str("""</div>
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
		self.result+=str("""<li> """)
		self.result+=str("""<a target="_self" href="../tutorial">Tutorial """)
		self.result+=str("""</a> """)
		self.result+=str("""</li>
								 """)
		self.result+=str("""<li data-theme="b"> """)
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
		self.result+=str("""<!-- Finally, to actually run the highlighter, you need to include this JS on your page -->
				 """)
		self.result+=str("""<script type="text/javascript">
				     SyntaxHighlighter.all()
				 """)
		self.result+=str("""</script>
			 """)
		self.result+=str("""</body>
			
		
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
