# -*- coding: utf-8 -*- 
import formFile
class install:
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
		self.result+=str("""<h1>Installation """)
		self.result+=str("""</h1>
					 """)
		self.result+=str("""<p>This instruction is basically based on debian linux, Ubuntu. """)
		self.result+=str("""</p>
					
					 """)
		self.result+=str("""<h2>Python3.x Interpreter """)
		self.result+=str("""</h2>
					 """)
		self.result+=str("""<p>Pylatte is python3.x based framework. Therefore it is mandatory to install python3.x interpreter. """)
		self.result+=str("""</p>
					 """)
		self.result+=str("""<pre class="brush: bash">
						$sudo apt-get install python3
						$python3
					 """)
		self.result+=str("""</pre>
					 """)
		self.result+=str("""<p>Current version is python3.2. so it is up to you if you install python3 or python3.2. After installing, check out whether it is installed or not. """)
		self.result+=str("""</p>
			
					 """)
		self.result+=str("""<h2>Pylatte """)
		self.result+=str("""</h2>
					
					 """)
		self.result+=str("""<h2>MySQL modules for python3 """)
		self.result+=str("""</h2>
						 """)
		self.result+=str("""<p>It is required to install MySQL module for python3. It makes using database with MySQL on python3.x possible. """)
		self.result+=str("""</p>
						
						 """)
		self.result+=str("""<h3>Install MySQL """)
		self.result+=str("""</h3>
						 """)
		self.result+=str("""<pre class="brush: bash">
							$sudo apt-get install mysql-server mysql-client
						 """)
		self.result+=str("""</pre>
						 """)
		self.result+=str("""<p>During the installation, it is asked to enter root password. """)
		self.result+=str("""</p>
						
						 """)
		self.result+=str("""<h3>Install Distribute """)
		self.result+=str("""</h3>
						 """)
		self.result+=str("""<pre class="brush: bash">
							$sudo apt-get install curl
							$curl -0 http://python-distribute.org/distribute_setup.py
							$sudo python3 distribute_setup.py 
						 """)
		self.result+=str("""</pre>
						
						 """)
		self.result+=str("""<h3>Install MySQLdb for Python3 """)
		self.result+=str("""</h3>
						 """)
		self.result+=str("""<p>Some kind people contribute to development of python3 based MySQL module as open source. It helps developers connect between python3 and MySQL. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<p>Download here :  """)
		self.result+=str("""<a href="https://github.com/davispuh/MySQL-for-Python-3">https://github.com/davispuh/MySQL-for-Python-3 """)
		self.result+=str("""</a> """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<pre class="brush: bash">
							$tar -xzvf MySQL-python-1.2.3.tar.gz
							$cd MySQL-python-1.2.3
							
							$vim site.cfg 
						 """)
		self.result+=str("""</pre>
						 """)
		self.result+=str("""<p>Open  """)
		self.result+=str("""<i>site.cfg """)
		self.result+=str("""</i> file to configure. Next, find  """)
		self.result+=str("""<b>//mysql_config """)
		self.result+=str("""</b> and remove '//' to make it not a commnet. Then, input the path which mysql installed like  """)
		self.result+=str("""<b>mysql_config = /home/pylatte/mysql """)
		self.result+=str("""</b>
						 """)
		self.result+=str("""<p>After configuration, execute following command at path MySQL-python-1.2.3 is installed. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<pre class="brush: bash">
							$sudo python3 setup.py build
							$sudo python3 setup.py install
						 """)
		self.result+=str("""</pre>
						
						 """)
		self.result+=str("""<p>If EnvironmentError occured, check mysql_config configuration again, and execute following command. """)
		self.result+=str("""</p> 
						 """)
		self.result+=str("""<pre class="brush: bash">
							$sudo apt-get install python-setuptools python-dev libmysqlclient15-dev 
						 """)
		self.result+=str("""</pre>
						
						 """)
		self.result+=str("""<h3>Check if the installation is complete or not """)
		self.result+=str("""</h3>	
						 """)
		self.result+=str("""<p>Execute python3.x interpreter """)
		self.result+=str("""</p>			
						 """)
		self.result+=str("""<pre class="brush: bash">
							$python3
						 """)
		self.result+=str("""</pre>
						 """)
		self.result+=str("""<p>Then, import MySQLdb """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""<pre class="brush: bash">
							>>import MySQLdb 
						 """)
		self.result+=str("""</pre>
						 """)
		self.result+=str("""<p>If import is successful without any error message, congratulation! it is complete. """)
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
		self.result+=str("""<li data-theme="b"> """)
		self.result+=str("""<a target="_self" href="../install">Install """)
		self.result+=str("""</a> """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<li> """)
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
		self.result+=str("""<!-- Finally, to actually run the highlighter, you need to include this JS on your page -->
			 """)
		self.result+=str("""</body>
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
