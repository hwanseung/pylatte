# -*- coding: utf-8 -*- 
import Pylatte.WebServer.formFile as formFile
class install:
	pylToHtmlResult=""
	sessionDic=dict()
	def __init__(self,param,pyFile,session,headerInfo,lattedb):
		self.generate(param,pyFile,session,headerInfo,lattedb)

	def generate(self,param,pyFile,session,headerInfo,lattedb):
		self.pylToHtmlResult+=str("""<!DOCTYPE html>""")
		self.pylToHtmlResult+=str("""
<html>""")
		self.pylToHtmlResult+=str("""
	<head>""")
		self.pylToHtmlResult+=str("""
	<meta name="viewport" content="width=device-width, initial-scale=1">""")
		self.pylToHtmlResult+=str("""
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">""")
		self.pylToHtmlResult+=str("""
	<title>""")
		self.pylToHtmlResult+=str("""Pylatte""")
		self.pylToHtmlResult+=str(""" -""")
		self.pylToHtmlResult+=str(""" Web""")
		self.pylToHtmlResult+=str(""" framework""")
		self.pylToHtmlResult+=str(""" based""")
		self.pylToHtmlResult+=str(""" on""")
		self.pylToHtmlResult+=str(""" Python3""")
		self.pylToHtmlResult+=str("""</title>""")
		self.pylToHtmlResult+=str("""
	
	<!-- favicon -->""")
		self.pylToHtmlResult+=str("""
	<link rel="shortcut icon" href="../pyl/favicon.ico" type="image/x-icon">""")
		self.pylToHtmlResult+=str("""
	<link rel="icon" href="../pyl/favicon.ico" type="image/x-icon">""")
		self.pylToHtmlResult+=str("""

	<!-- Include required JS files -->""")
		self.pylToHtmlResult+=str("""
	<script type="text/javascript" src="../pyl/syntaxhighlighter/js/xregexp.js">""")
		self.pylToHtmlResult+=str("""</script>""")
		self.pylToHtmlResult+=str("""
	<script type="text/javascript" src="../pyl/syntaxhighlighter/js/shCore.js">""")
		self.pylToHtmlResult+=str("""</script>""")
		self.pylToHtmlResult+=str("""
	 
	<!--
	    At least one brush, here we choose JS. You need to include a brush for every
	    language you want to highlight
	-->""")
		self.pylToHtmlResult+=str("""
	<script type="text/javascript" src="../pyl/syntaxhighlighter/lang/shBrushXml.js">""")
		self.pylToHtmlResult+=str("""</script>""")
		self.pylToHtmlResult+=str("""
	<script type="text/javascript" src="../pyl/syntaxhighlighter/lang/shBrushBash.js">""")
		self.pylToHtmlResult+=str("""</script>""")
		self.pylToHtmlResult+=str("""
	 
	<!-- Include *at least* the core style and default theme -->""")
		self.pylToHtmlResult+=str("""
	<link href="../pyl/syntaxhighlighter/css/shCore.css" rel="stylesheet" type="text/css" />""")
		self.pylToHtmlResult+=str("""
	<link href="../pyl/syntaxhighlighter/css/shThemeDefault.css" rel="stylesheet" type="text/css" />""")
		self.pylToHtmlResult+=str("""
	
	
	
	<link rel="stylesheet"  href="../pyl/css/jquery.mobile-1.2.0.css"/>""")
		self.pylToHtmlResult+=str("""
	<link rel="stylesheet"  href="../pyl/css/jqm-docs.css"/>""")
		self.pylToHtmlResult+=str("""
	
	<script src="../pyl/js/jquery.js">""")
		self.pylToHtmlResult+=str("""</script>""")
		self.pylToHtmlResult+=str("""
	<script src="../pyl/js/jqm-docs.js">""")
		self.pylToHtmlResult+=str("""</script>""")
		self.pylToHtmlResult+=str("""
	<script src="../pyl/js/jquery.mobile.themeswitcher.js">""")
		self.pylToHtmlResult+=str("""</script>""")
		self.pylToHtmlResult+=str("""
	<script src="../pyl/js/jquery.mobile-1.2.0.min.js">""")
		self.pylToHtmlResult+=str("""</script>""")
		self.pylToHtmlResult+=str("""
	
	<script type="text/javascript">""")
		self.pylToHtmlResult+=str("""

	  var""")
		self.pylToHtmlResult+=str(""" _gaq""")
		self.pylToHtmlResult+=str(""" =""")
		self.pylToHtmlResult+=str(""" _gaq""")
		self.pylToHtmlResult+=str(""" ||""")
		self.pylToHtmlResult+=str(""" [];""")
		self.pylToHtmlResult+=str("""
	  _gaq.push(['_setAccount',""")
		self.pylToHtmlResult+=str(""" 'UA-26668199-1']);""")
		self.pylToHtmlResult+=str("""
	  _gaq.push(['_trackPageview']);""")
		self.pylToHtmlResult+=str("""
	
	  (function()""")
		self.pylToHtmlResult+=str(""" {""")
		self.pylToHtmlResult+=str("""
	    var""")
		self.pylToHtmlResult+=str(""" ga""")
		self.pylToHtmlResult+=str(""" =""")
		self.pylToHtmlResult+=str(""" document.createElement('script');""")
		self.pylToHtmlResult+=str(""" ga.type""")
		self.pylToHtmlResult+=str(""" =""")
		self.pylToHtmlResult+=str(""" 'text/javascript';""")
		self.pylToHtmlResult+=str(""" ga.async""")
		self.pylToHtmlResult+=str(""" =""")
		self.pylToHtmlResult+=str(""" true;""")
		self.pylToHtmlResult+=str("""
	    ga.src""")
		self.pylToHtmlResult+=str(""" =""")
		self.pylToHtmlResult+=str(""" ('https:'""")
		self.pylToHtmlResult+=str(""" ==""")
		self.pylToHtmlResult+=str(""" document.location.protocol""")
		self.pylToHtmlResult+=str(""" ?""")
		self.pylToHtmlResult+=str(""" 'https://ssl'""")
		self.pylToHtmlResult+=str(""" :""")
		self.pylToHtmlResult+=str(""" 'http://www')""")
		self.pylToHtmlResult+=str(""" +""")
		self.pylToHtmlResult+=str(""" '.google-analytics.com/ga.js';""")
		self.pylToHtmlResult+=str("""
	    var""")
		self.pylToHtmlResult+=str(""" s""")
		self.pylToHtmlResult+=str(""" =""")
		self.pylToHtmlResult+=str(""" document.getElementsByTagName('script')[0];""")
		self.pylToHtmlResult+=str(""" s.parentNode.insertBefore(ga,""")
		self.pylToHtmlResult+=str(""" s);""")
		self.pylToHtmlResult+=str("""
	  })();""")
		self.pylToHtmlResult+=str("""
	
	</script>""")
		self.pylToHtmlResult+=str("""
	
	</head>""")
		self.pylToHtmlResult+=str("""


	<body>""")
		self.pylToHtmlResult+=str("""

	<div data-role="page" class="type-interior">""")
		self.pylToHtmlResult+=str("""
		<div data-role="header" data-theme="b">""")
		self.pylToHtmlResult+=str("""
		<h1>""")
		self.pylToHtmlResult+=str("""Pylatte""")
		self.pylToHtmlResult+=str(""" Official""")
		self.pylToHtmlResult+=str(""" Webpage""")
		self.pylToHtmlResult+=str("""</h1>""")
		self.pylToHtmlResult+=str("""
		<a href="../../" target="_self" data-icon="home" data-iconpos="notext" data-direction="reverse" class="ui-btn-right jqm-home">""")
		self.pylToHtmlResult+=str("""Home""")
		self.pylToHtmlResult+=str("""</a>""")
		self.pylToHtmlResult+=str("""
	</div>""")
		self.pylToHtmlResult+=str("""<!-- /header -->""")
		self.pylToHtmlResult+=str("""

	<div data-role="content">""")
		self.pylToHtmlResult+=str("""
			<div class="content-primary">""")
		self.pylToHtmlResult+=str("""
			
			<h1>""")
		self.pylToHtmlResult+=str("""Installation""")
		self.pylToHtmlResult+=str("""</h1>""")
		self.pylToHtmlResult+=str("""
			<p>""")
		self.pylToHtmlResult+=str("""This""")
		self.pylToHtmlResult+=str(""" instruction""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" basically""")
		self.pylToHtmlResult+=str(""" based""")
		self.pylToHtmlResult+=str(""" on""")
		self.pylToHtmlResult+=str(""" debian""")
		self.pylToHtmlResult+=str(""" linux,""")
		self.pylToHtmlResult+=str(""" Ubuntu.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
			
			<h2>""")
		self.pylToHtmlResult+=str("""Python3.x""")
		self.pylToHtmlResult+=str(""" Interpreter""")
		self.pylToHtmlResult+=str("""</h2>""")
		self.pylToHtmlResult+=str("""
			<p>""")
		self.pylToHtmlResult+=str("""Pylatte""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" python3.x""")
		self.pylToHtmlResult+=str(""" based""")
		self.pylToHtmlResult+=str(""" framework.""")
		self.pylToHtmlResult+=str(""" Therefore""")
		self.pylToHtmlResult+=str(""" it""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" mandatory""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" install""")
		self.pylToHtmlResult+=str(""" python3.x""")
		self.pylToHtmlResult+=str(""" interpreter.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
			<pre class="brush: bash">""")
		self.pylToHtmlResult+=str("""
				$sudo""")
		self.pylToHtmlResult+=str(""" apt-get""")
		self.pylToHtmlResult+=str(""" install""")
		self.pylToHtmlResult+=str(""" python3""")
		self.pylToHtmlResult+=str("""
				$python3""")
		self.pylToHtmlResult+=str("""
			</pre>""")
		self.pylToHtmlResult+=str("""
			<p>""")
		self.pylToHtmlResult+=str("""Current""")
		self.pylToHtmlResult+=str(""" version""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" python3.2.""")
		self.pylToHtmlResult+=str(""" so""")
		self.pylToHtmlResult+=str(""" it""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" up""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" you""")
		self.pylToHtmlResult+=str(""" if""")
		self.pylToHtmlResult+=str(""" you""")
		self.pylToHtmlResult+=str(""" install""")
		self.pylToHtmlResult+=str(""" python3""")
		self.pylToHtmlResult+=str(""" or""")
		self.pylToHtmlResult+=str(""" python3.2.""")
		self.pylToHtmlResult+=str(""" After""")
		self.pylToHtmlResult+=str(""" installing,""")
		self.pylToHtmlResult+=str(""" check""")
		self.pylToHtmlResult+=str(""" out""")
		self.pylToHtmlResult+=str(""" whether""")
		self.pylToHtmlResult+=str(""" it""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" installed""")
		self.pylToHtmlResult+=str(""" or""")
		self.pylToHtmlResult+=str(""" not.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
	
			<h2>""")
		self.pylToHtmlResult+=str("""Pylatte""")
		self.pylToHtmlResult+=str("""</h2>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""first,""")
		self.pylToHtmlResult+=str(""" you""")
		self.pylToHtmlResult+=str(""" must""")
		self.pylToHtmlResult+=str(""" download""")
		self.pylToHtmlResult+=str(""" pylatte.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				<h3>""")
		self.pylToHtmlResult+=str("""install""")
		self.pylToHtmlResult+=str(""" Pylatte""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""you""")
		self.pylToHtmlResult+=str(""" can""")
		self.pylToHtmlResult+=str(""" download""")
		self.pylToHtmlResult+=str(""" install""")
		self.pylToHtmlResult+=str(""" file""")
		self.pylToHtmlResult+=str(""" at""")
		self.pylToHtmlResult+=str(""" <a href="http://code.google.com/p/pylatte/downloads/list">""")
		self.pylToHtmlResult+=str("""http://code.google.com/p/pylatte/downloads/list""")
		self.pylToHtmlResult+=str("""</a>""")
		self.pylToHtmlResult+=str(""" and""")
		self.pylToHtmlResult+=str(""" unzip""")
		self.pylToHtmlResult+=str(""" the""")
		self.pylToHtmlResult+=str(""" file""")
		self.pylToHtmlResult+=str(""" and""")
		self.pylToHtmlResult+=str(""" install.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				<pre class="brush: bash">""")
		self.pylToHtmlResult+=str("""
					$sudo""")
		self.pylToHtmlResult+=str(""" python3""")
		self.pylToHtmlResult+=str(""" setup.py""")
		self.pylToHtmlResult+=str(""" install""")
		self.pylToHtmlResult+=str("""
				</pre>""")
		self.pylToHtmlResult+=str("""
				<h3>""")
		self.pylToHtmlResult+=str("""Check""")
		self.pylToHtmlResult+=str(""" if""")
		self.pylToHtmlResult+=str(""" the""")
		self.pylToHtmlResult+=str(""" installation""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" complete""")
		self.pylToHtmlResult+=str(""" or""")
		self.pylToHtmlResult+=str(""" not""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""Execute""")
		self.pylToHtmlResult+=str(""" python3.x""")
		self.pylToHtmlResult+=str(""" interpreter""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				<pre class="brush: bash">""")
		self.pylToHtmlResult+=str("""
					$python3""")
		self.pylToHtmlResult+=str("""
				</pre>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""Then,""")
		self.pylToHtmlResult+=str(""" import""")
		self.pylToHtmlResult+=str(""" Pylatte""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				<pre class="brush: bash">""")
		self.pylToHtmlResult+=str("""
					>""")
		self.pylToHtmlResult+=str(""">""")
		self.pylToHtmlResult+=str("""import""")
		self.pylToHtmlResult+=str(""" Pylatte""")
		self.pylToHtmlResult+=str("""
				</pre>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""If""")
		self.pylToHtmlResult+=str(""" import""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" successful""")
		self.pylToHtmlResult+=str(""" without""")
		self.pylToHtmlResult+=str(""" any""")
		self.pylToHtmlResult+=str(""" error""")
		self.pylToHtmlResult+=str(""" message,""")
		self.pylToHtmlResult+=str(""" congratulation!""")
		self.pylToHtmlResult+=str(""" it""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" complete.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
			
			<h2>""")
		self.pylToHtmlResult+=str("""PLY(Python""")
		self.pylToHtmlResult+=str(""" Lex-Yacc)""")
		self.pylToHtmlResult+=str("""</h2>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""It""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" required""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" execute""")
		self.pylToHtmlResult+=str(""" pylatte.""")
		self.pylToHtmlResult+=str(""" It""")
		self.pylToHtmlResult+=str(""" makes""")
		self.pylToHtmlResult+=str(""" converting""")
		self.pylToHtmlResult+=str(""" PYL""")
		self.pylToHtmlResult+=str(""" Code""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" Python""")
		self.pylToHtmlResult+=str(""" code""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""you""")
		self.pylToHtmlResult+=str(""" can""")
		self.pylToHtmlResult+=str(""" download""")
		self.pylToHtmlResult+=str(""" install""")
		self.pylToHtmlResult+=str(""" file""")
		self.pylToHtmlResult+=str(""" at""")
		self.pylToHtmlResult+=str(""" <a href="http://www.dabeaz.com/ply/index.html">""")
		self.pylToHtmlResult+=str("""http://www.dabeaz.com/ply/index.html""")
		self.pylToHtmlResult+=str("""</a>""")
		self.pylToHtmlResult+=str(""" and""")
		self.pylToHtmlResult+=str(""" unzip""")
		self.pylToHtmlResult+=str(""" the""")
		self.pylToHtmlResult+=str(""" file""")
		self.pylToHtmlResult+=str(""" and""")
		self.pylToHtmlResult+=str(""" install.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				<h3>""")
		self.pylToHtmlResult+=str("""Install""")
		self.pylToHtmlResult+=str(""" PYL""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""
				<pre class="brush: bash">""")
		self.pylToHtmlResult+=str("""
					$sudo""")
		self.pylToHtmlResult+=str(""" python3""")
		self.pylToHtmlResult+=str(""" setup.py""")
		self.pylToHtmlResult+=str(""" install""")
		self.pylToHtmlResult+=str("""
				</pre>""")
		self.pylToHtmlResult+=str("""
			<h2>""")
		self.pylToHtmlResult+=str("""MySQL""")
		self.pylToHtmlResult+=str(""" modules""")
		self.pylToHtmlResult+=str(""" for""")
		self.pylToHtmlResult+=str(""" python3""")
		self.pylToHtmlResult+=str("""</h2>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""It""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" required""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" install""")
		self.pylToHtmlResult+=str(""" MySQL""")
		self.pylToHtmlResult+=str(""" module""")
		self.pylToHtmlResult+=str(""" for""")
		self.pylToHtmlResult+=str(""" python3.""")
		self.pylToHtmlResult+=str(""" It""")
		self.pylToHtmlResult+=str(""" makes""")
		self.pylToHtmlResult+=str(""" using""")
		self.pylToHtmlResult+=str(""" database""")
		self.pylToHtmlResult+=str(""" with""")
		self.pylToHtmlResult+=str(""" MySQL""")
		self.pylToHtmlResult+=str(""" on""")
		self.pylToHtmlResult+=str(""" python3.x""")
		self.pylToHtmlResult+=str(""" possible.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				
				<h3>""")
		self.pylToHtmlResult+=str("""Install""")
		self.pylToHtmlResult+=str(""" MySQL""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""
				<pre class="brush: bash">""")
		self.pylToHtmlResult+=str("""
					$sudo""")
		self.pylToHtmlResult+=str(""" apt-get""")
		self.pylToHtmlResult+=str(""" install""")
		self.pylToHtmlResult+=str(""" mysql-server""")
		self.pylToHtmlResult+=str(""" mysql-client""")
		self.pylToHtmlResult+=str("""
				</pre>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""During""")
		self.pylToHtmlResult+=str(""" the""")
		self.pylToHtmlResult+=str(""" installation,""")
		self.pylToHtmlResult+=str(""" it""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" asked""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" enter""")
		self.pylToHtmlResult+=str(""" root""")
		self.pylToHtmlResult+=str(""" password.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				
				<h3>""")
		self.pylToHtmlResult+=str("""Install""")
		self.pylToHtmlResult+=str(""" Distribute""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""
				<pre class="brush: bash">""")
		self.pylToHtmlResult+=str("""
					$sudo""")
		self.pylToHtmlResult+=str(""" apt-get""")
		self.pylToHtmlResult+=str(""" install""")
		self.pylToHtmlResult+=str(""" curl""")
		self.pylToHtmlResult+=str("""
					$curl""")
		self.pylToHtmlResult+=str(""" -0""")
		self.pylToHtmlResult+=str(""" http://python-distribute.org/distribute_setup.py""")
		self.pylToHtmlResult+=str("""
					$sudo""")
		self.pylToHtmlResult+=str(""" python3""")
		self.pylToHtmlResult+=str(""" distribute_setup.py""")
		self.pylToHtmlResult+=str(""" 
				</pre>""")
		self.pylToHtmlResult+=str("""
				
				<h3>""")
		self.pylToHtmlResult+=str("""Install""")
		self.pylToHtmlResult+=str(""" MySQLdb""")
		self.pylToHtmlResult+=str(""" for""")
		self.pylToHtmlResult+=str(""" Python3""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""Some""")
		self.pylToHtmlResult+=str(""" kind""")
		self.pylToHtmlResult+=str(""" people""")
		self.pylToHtmlResult+=str(""" contribute""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" development""")
		self.pylToHtmlResult+=str(""" of""")
		self.pylToHtmlResult+=str(""" python3""")
		self.pylToHtmlResult+=str(""" based""")
		self.pylToHtmlResult+=str(""" MySQL""")
		self.pylToHtmlResult+=str(""" module""")
		self.pylToHtmlResult+=str(""" as""")
		self.pylToHtmlResult+=str(""" open""")
		self.pylToHtmlResult+=str(""" source.""")
		self.pylToHtmlResult+=str(""" It""")
		self.pylToHtmlResult+=str(""" helps""")
		self.pylToHtmlResult+=str(""" developers""")
		self.pylToHtmlResult+=str(""" connect""")
		self.pylToHtmlResult+=str(""" between""")
		self.pylToHtmlResult+=str(""" python3""")
		self.pylToHtmlResult+=str(""" and""")
		self.pylToHtmlResult+=str(""" MySQL.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""Download""")
		self.pylToHtmlResult+=str(""" here""")
		self.pylToHtmlResult+=str(""" :""")
		self.pylToHtmlResult+=str(""" <a href="https://github.com/davispuh/MySQL-for-Python-3">""")
		self.pylToHtmlResult+=str("""https://github.com/davispuh/MySQL-for-Python-3""")
		self.pylToHtmlResult+=str("""</a>""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				<pre class="brush: bash">""")
		self.pylToHtmlResult+=str("""
					$tar""")
		self.pylToHtmlResult+=str(""" -xzvf""")
		self.pylToHtmlResult+=str(""" MySQL-python-1.2.3.tar.gz""")
		self.pylToHtmlResult+=str("""
					$cd""")
		self.pylToHtmlResult+=str(""" MySQL-python-1.2.3""")
		self.pylToHtmlResult+=str("""
					
					$vim""")
		self.pylToHtmlResult+=str(""" site.cfg""")
		self.pylToHtmlResult+=str(""" 
				</pre>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""Open""")
		self.pylToHtmlResult+=str(""" <i>""")
		self.pylToHtmlResult+=str("""site.cfg""")
		self.pylToHtmlResult+=str("""</i>""")
		self.pylToHtmlResult+=str(""" file""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" configure.""")
		self.pylToHtmlResult+=str(""" Next,""")
		self.pylToHtmlResult+=str(""" find""")
		self.pylToHtmlResult+=str(""" <b>""")
		self.pylToHtmlResult+=str("""//mysql_config""")
		self.pylToHtmlResult+=str("""</b>""")
		self.pylToHtmlResult+=str(""" and""")
		self.pylToHtmlResult+=str(""" remove""")
		self.pylToHtmlResult+=str(""" '//'""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" make""")
		self.pylToHtmlResult+=str(""" it""")
		self.pylToHtmlResult+=str(""" not""")
		self.pylToHtmlResult+=str(""" a""")
		self.pylToHtmlResult+=str(""" commnet.""")
		self.pylToHtmlResult+=str(""" Then,""")
		self.pylToHtmlResult+=str(""" input""")
		self.pylToHtmlResult+=str(""" the""")
		self.pylToHtmlResult+=str(""" path""")
		self.pylToHtmlResult+=str(""" which""")
		self.pylToHtmlResult+=str(""" mysql""")
		self.pylToHtmlResult+=str(""" installed""")
		self.pylToHtmlResult+=str(""" like""")
		self.pylToHtmlResult+=str(""" <b>""")
		self.pylToHtmlResult+=str("""mysql_config""")
		self.pylToHtmlResult+=str(""" =""")
		self.pylToHtmlResult+=str(""" /home/pylatte/mysql""")
		self.pylToHtmlResult+=str("""</b>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""After""")
		self.pylToHtmlResult+=str(""" configuration,""")
		self.pylToHtmlResult+=str(""" execute""")
		self.pylToHtmlResult+=str(""" following""")
		self.pylToHtmlResult+=str(""" command""")
		self.pylToHtmlResult+=str(""" at""")
		self.pylToHtmlResult+=str(""" path""")
		self.pylToHtmlResult+=str(""" MySQL-python-1.2.3""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" installed.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				<pre class="brush: bash">""")
		self.pylToHtmlResult+=str("""
					$sudo""")
		self.pylToHtmlResult+=str(""" python3""")
		self.pylToHtmlResult+=str(""" setup.py""")
		self.pylToHtmlResult+=str(""" build""")
		self.pylToHtmlResult+=str("""
					$sudo""")
		self.pylToHtmlResult+=str(""" python3""")
		self.pylToHtmlResult+=str(""" setup.py""")
		self.pylToHtmlResult+=str(""" install""")
		self.pylToHtmlResult+=str("""
				</pre>""")
		self.pylToHtmlResult+=str("""
				
				<p>""")
		self.pylToHtmlResult+=str("""If""")
		self.pylToHtmlResult+=str(""" EnvironmentError""")
		self.pylToHtmlResult+=str(""" occured,""")
		self.pylToHtmlResult+=str(""" check""")
		self.pylToHtmlResult+=str(""" mysql_config""")
		self.pylToHtmlResult+=str(""" configuration""")
		self.pylToHtmlResult+=str(""" again,""")
		self.pylToHtmlResult+=str(""" and""")
		self.pylToHtmlResult+=str(""" execute""")
		self.pylToHtmlResult+=str(""" following""")
		self.pylToHtmlResult+=str(""" command.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str(""" 
				<pre class="brush: bash">""")
		self.pylToHtmlResult+=str("""
					$sudo""")
		self.pylToHtmlResult+=str(""" apt-get""")
		self.pylToHtmlResult+=str(""" install""")
		self.pylToHtmlResult+=str(""" python-setuptools""")
		self.pylToHtmlResult+=str(""" python-dev""")
		self.pylToHtmlResult+=str(""" libmysqlclient15-dev""")
		self.pylToHtmlResult+=str(""" 
				</pre>""")
		self.pylToHtmlResult+=str("""
				
				<h3>""")
		self.pylToHtmlResult+=str("""Check""")
		self.pylToHtmlResult+=str(""" if""")
		self.pylToHtmlResult+=str(""" the""")
		self.pylToHtmlResult+=str(""" installation""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" complete""")
		self.pylToHtmlResult+=str(""" or""")
		self.pylToHtmlResult+=str(""" not""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""Execute""")
		self.pylToHtmlResult+=str(""" python3.x""")
		self.pylToHtmlResult+=str(""" interpreter""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				<pre class="brush: bash">""")
		self.pylToHtmlResult+=str("""
					$python3""")
		self.pylToHtmlResult+=str("""
				</pre>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""Then,""")
		self.pylToHtmlResult+=str(""" import""")
		self.pylToHtmlResult+=str(""" MySQLdb""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				<pre class="brush: bash">""")
		self.pylToHtmlResult+=str("""
					>""")
		self.pylToHtmlResult+=str(""">""")
		self.pylToHtmlResult+=str("""import""")
		self.pylToHtmlResult+=str(""" MySQLdb""")
		self.pylToHtmlResult+=str(""" 
				</pre>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""If""")
		self.pylToHtmlResult+=str(""" import""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" successful""")
		self.pylToHtmlResult+=str(""" without""")
		self.pylToHtmlResult+=str(""" any""")
		self.pylToHtmlResult+=str(""" error""")
		self.pylToHtmlResult+=str(""" message,""")
		self.pylToHtmlResult+=str(""" congratulation!""")
		self.pylToHtmlResult+=str(""" it""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" complete.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				
				
			<h2>""")
		self.pylToHtmlResult+=str("""MongoDB""")
		self.pylToHtmlResult+=str(""" modules""")
		self.pylToHtmlResult+=str(""" for""")
		self.pylToHtmlResult+=str(""" python3""")
		self.pylToHtmlResult+=str("""</h2>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""It""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" required""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" install""")
		self.pylToHtmlResult+=str(""" MongoDB""")
		self.pylToHtmlResult+=str(""" module""")
		self.pylToHtmlResult+=str(""" for""")
		self.pylToHtmlResult+=str(""" python3.""")
		self.pylToHtmlResult+=str(""" It""")
		self.pylToHtmlResult+=str(""" makes""")
		self.pylToHtmlResult+=str(""" using""")
		self.pylToHtmlResult+=str(""" database""")
		self.pylToHtmlResult+=str(""" with""")
		self.pylToHtmlResult+=str(""" MongoDB""")
		self.pylToHtmlResult+=str(""" on""")
		self.pylToHtmlResult+=str(""" python3.x""")
		self.pylToHtmlResult+=str(""" possible.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				
				<h3>""")
		self.pylToHtmlResult+=str("""Install""")
		self.pylToHtmlResult+=str(""" MongoDB""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""
				<pre class="brush: bash">""")
		self.pylToHtmlResult+=str("""
					$sudo""")
		self.pylToHtmlResult+=str(""" apt-get""")
		self.pylToHtmlResult+=str(""" install""")
		self.pylToHtmlResult+=str(""" mongodb""")
		self.pylToHtmlResult+=str("""
				</pre>""")
		self.pylToHtmlResult+=str("""
				
				<h3>""")
		self.pylToHtmlResult+=str("""Install""")
		self.pylToHtmlResult+=str(""" Mongodb""")
		self.pylToHtmlResult+=str(""" for""")
		self.pylToHtmlResult+=str(""" Python3""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""Download""")
		self.pylToHtmlResult+=str(""" here""")
		self.pylToHtmlResult+=str(""" :""")
		self.pylToHtmlResult+=str(""" <a href="https://github.com/mongodb/mongo-python-driver">""")
		self.pylToHtmlResult+=str("""https://github.com/mongodb/mongo-python-driver""")
		self.pylToHtmlResult+=str("""</a>""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				<pre class="brush: bash">""")
		self.pylToHtmlResult+=str("""
					$tar""")
		self.pylToHtmlResult+=str(""" -xzvf""")
		self.pylToHtmlResult+=str(""" mongo-python-driver-py3k.tar.gz""")
		self.pylToHtmlResult+=str("""
					$cd""")
		self.pylToHtmlResult+=str(""" mongo-python-driver-py3k""")
		self.pylToHtmlResult+=str("""
				</pre>""")
		self.pylToHtmlResult+=str("""
			
				<p>""")
		self.pylToHtmlResult+=str("""After""")
		self.pylToHtmlResult+=str(""" configuration,""")
		self.pylToHtmlResult+=str(""" execute""")
		self.pylToHtmlResult+=str(""" following""")
		self.pylToHtmlResult+=str(""" command""")
		self.pylToHtmlResult+=str(""" at""")
		self.pylToHtmlResult+=str(""" path""")
		self.pylToHtmlResult+=str(""" mongo-python-driver-py3k""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" installed.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				<pre class="brush: bash">""")
		self.pylToHtmlResult+=str("""
					$sudo""")
		self.pylToHtmlResult+=str(""" python3""")
		self.pylToHtmlResult+=str(""" setup.py""")
		self.pylToHtmlResult+=str(""" build""")
		self.pylToHtmlResult+=str("""
					$sudo""")
		self.pylToHtmlResult+=str(""" python3""")
		self.pylToHtmlResult+=str(""" setup.py""")
		self.pylToHtmlResult+=str(""" install""")
		self.pylToHtmlResult+=str("""
				</pre>""")
		self.pylToHtmlResult+=str("""
				
				<h3>""")
		self.pylToHtmlResult+=str("""Check""")
		self.pylToHtmlResult+=str(""" if""")
		self.pylToHtmlResult+=str(""" the""")
		self.pylToHtmlResult+=str(""" installation""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" complete""")
		self.pylToHtmlResult+=str(""" or""")
		self.pylToHtmlResult+=str(""" not""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""Execute""")
		self.pylToHtmlResult+=str(""" python3.x""")
		self.pylToHtmlResult+=str(""" interpreter""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				<pre class="brush: bash">""")
		self.pylToHtmlResult+=str("""
					$python3""")
		self.pylToHtmlResult+=str("""
				</pre>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""Then,""")
		self.pylToHtmlResult+=str(""" import""")
		self.pylToHtmlResult+=str(""" pymongo""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				<pre class="brush: bash">""")
		self.pylToHtmlResult+=str("""
					>""")
		self.pylToHtmlResult+=str(""">""")
		self.pylToHtmlResult+=str("""import""")
		self.pylToHtmlResult+=str(""" pymongo""")
		self.pylToHtmlResult+=str("""
				</pre>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""If""")
		self.pylToHtmlResult+=str(""" import""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" successful""")
		self.pylToHtmlResult+=str(""" without""")
		self.pylToHtmlResult+=str(""" any""")
		self.pylToHtmlResult+=str(""" error""")
		self.pylToHtmlResult+=str(""" message,""")
		self.pylToHtmlResult+=str(""" congratulation!""")
		self.pylToHtmlResult+=str(""" it""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" complete.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
			</div>""")
		self.pylToHtmlResult+=str("""<!--/content-primary -->""")
		self.pylToHtmlResult+=str("""

			<div class="content-secondary">""")
		self.pylToHtmlResult+=str("""

				<div data-role="collapsible" data-collapsed="true" data-theme="b" data-content-theme="d">""")
		self.pylToHtmlResult+=str("""

						<h3>""")
		self.pylToHtmlResult+=str("""More""")
		self.pylToHtmlResult+=str(""" in""")
		self.pylToHtmlResult+=str(""" this""")
		self.pylToHtmlResult+=str(""" section""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""

						<ul data-role="listview" data-theme="c" data-dividertheme="d">""")
		self.pylToHtmlResult+=str("""
							<li data-role="list-divider">""")
		self.pylToHtmlResult+=str("""Menu""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""<a target="_self" href="../index">""")
		self.pylToHtmlResult+=str("""About""")
		self.pylToHtmlResult+=str("""</a>""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""<a target="_self" href="../download">""")
		self.pylToHtmlResult+=str("""Download""")
		self.pylToHtmlResult+=str("""</a>""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<li data-theme="b">""")
		self.pylToHtmlResult+=str("""<a target="_self" href="../install">""")
		self.pylToHtmlResult+=str("""Install""")
		self.pylToHtmlResult+=str("""</a>""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""<a target="_self" href="../tutorial">""")
		self.pylToHtmlResult+=str("""Tutorial""")
		self.pylToHtmlResult+=str("""</a>""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""<a target="_self" href="../documentation">""")
		self.pylToHtmlResult+=str("""Documentation""")
		self.pylToHtmlResult+=str("""</a>""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""<a target="_self" href="../comment">""")
		self.pylToHtmlResult+=str("""Comment""")
		self.pylToHtmlResult+=str("""</a>""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""<a target="_self" href="../faq">""")
		self.pylToHtmlResult+=str("""F""")
		self.pylToHtmlResult+=str(""" A""")
		self.pylToHtmlResult+=str(""" Q""")
		self.pylToHtmlResult+=str("""</a>""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""<a target="_self" href="../contactus">""")
		self.pylToHtmlResult+=str("""Contact""")
		self.pylToHtmlResult+=str(""" us""")
		self.pylToHtmlResult+=str("""</a>""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<img src="../pyl/image/pylatte.png">""")
		self.pylToHtmlResult+=str("""</img>""")
		self.pylToHtmlResult+=str("""
						</ul>""")
		self.pylToHtmlResult+=str("""
				</div>""")
		self.pylToHtmlResult+=str("""
			</div>""")
		self.pylToHtmlResult+=str("""

		</div>""")
		self.pylToHtmlResult+=str("""<!-- /content -->""")
		self.pylToHtmlResult+=str("""

		<div data-role="footer" class="footer-docs" data-theme="b">""")
		self.pylToHtmlResult+=str("""
				<h4>""")
		self.pylToHtmlResult+=str("""&copy;""")
		self.pylToHtmlResult+=str(""" 2011""")
		self.pylToHtmlResult+=str(""" The""")
		self.pylToHtmlResult+=str(""" Pylatte""")
		self.pylToHtmlResult+=str(""" Project""")
		self.pylToHtmlResult+=str("""</h4>""")
		self.pylToHtmlResult+=str("""
		</div>""")
		self.pylToHtmlResult+=str("""

		</div>""")
		self.pylToHtmlResult+=str("""<!-- /page -->""")
		self.pylToHtmlResult+=str("""
		<!-- Finally, to actually run the highlighter, you need to include this JS on your page -->""")
		self.pylToHtmlResult+=str("""
	</body>""")
		self.pylToHtmlResult+=str("""
	<script type="text/javascript">""")
		self.pylToHtmlResult+=str("""
	     SyntaxHighlighter.all()""")
		self.pylToHtmlResult+=str("""
	</script>""")
		self.pylToHtmlResult+=str("""
</html>""")
		self.sessionDic=session
		pass
	def getHtml(self):
		return self.pylToHtmlResult
		pass
	def getSession(self):
		return self.sessionDic
		pass
