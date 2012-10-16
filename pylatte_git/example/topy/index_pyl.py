# -*- coding: utf-8 -*- 
import Pylatte.WebServer.formFile as formFile
class index:
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
		<a href="../../" data-icon="home" data-iconpos="notext" data-direction="reverse" class="ui-btn-right jqm-home">""")
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
		self.pylToHtmlResult+=str("""Welcome""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" Pylatte""")
		self.pylToHtmlResult+=str("""</h1>""")
		self.pylToHtmlResult+=str("""
			<h2>""")
		self.pylToHtmlResult+=str("""Pylatte""")
		self.pylToHtmlResult+=str(""" :""")
		self.pylToHtmlResult+=str("""  A""")
		self.pylToHtmlResult+=str(""" Web""")
		self.pylToHtmlResult+=str(""" Framework""")
		self.pylToHtmlResult+=str(""" Based""")
		self.pylToHtmlResult+=str(""" on""")
		self.pylToHtmlResult+=str(""" Python""")
		self.pylToHtmlResult+=str(""" 3""")
		self.pylToHtmlResult+=str("""</h2>""")
		self.pylToHtmlResult+=str("""
			<p>""")
		self.pylToHtmlResult+=str("""Pylatte""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" a""")
		self.pylToHtmlResult+=str(""" web""")
		self.pylToHtmlResult+=str(""" framework""")
		self.pylToHtmlResult+=str(""" created""")
		self.pylToHtmlResult+=str(""" specifically""")
		self.pylToHtmlResult+=str(""" for""")
		self.pylToHtmlResult+=str(""" Python""")
		self.pylToHtmlResult+=str(""" 3.""")
		self.pylToHtmlResult+=str(""" Developers""")
		self.pylToHtmlResult+=str(""" can""")
		self.pylToHtmlResult+=str(""" now""")
		self.pylToHtmlResult+=str(""" generate""")
		self.pylToHtmlResult+=str(""" websites""")
		self.pylToHtmlResult+=str(""" with""")
		self.pylToHtmlResult+=str(""" Pylatte""")
		self.pylToHtmlResult+=str(""" in""")
		self.pylToHtmlResult+=str(""" Python""")
		self.pylToHtmlResult+=str(""" 3.""")
		self.pylToHtmlResult+=str(""" just""")
		self.pylToHtmlResult+=str(""" as""")
		self.pylToHtmlResult+=str(""" they""")
		self.pylToHtmlResult+=str(""" might""")
		self.pylToHtmlResult+=str(""" for""")
		self.pylToHtmlResult+=str(""" Python""")
		self.pylToHtmlResult+=str(""" 2x-based""")
		self.pylToHtmlResult+=str(""" frameworks""")
		self.pylToHtmlResult+=str(""" such""")
		self.pylToHtmlResult+=str(""" as""")
		self.pylToHtmlResult+=str(""" Django,""")
		self.pylToHtmlResult+=str(""" Flask,""")
		self.pylToHtmlResult+=str(""" or""")
		self.pylToHtmlResult+=str(""" Bottle.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
			
			<h2>""")
		self.pylToHtmlResult+=str("""Sample""")
		self.pylToHtmlResult+=str(""" code""")
		self.pylToHtmlResult+=str("""</h2>""")
		self.pylToHtmlResult+=str("""
			<p>""")
		self.pylToHtmlResult+=str("""The""")
		self.pylToHtmlResult+=str(""" following""")
		self.pylToHtmlResult+=str(""" code""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" a""")
		self.pylToHtmlResult+=str(""" example""")
		self.pylToHtmlResult+=str(""" <i>""")
		self.pylToHtmlResult+=str("""pyl""")
		self.pylToHtmlResult+=str("""</i>""")
		self.pylToHtmlResult+=str(""" file.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str(""" 
			<pre class="brush: xml">""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""Pylatte""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				&lt;$""")
		self.pylToHtmlResult+=str("""
				pyl""")
		self.pylToHtmlResult+=str(""" =""")
		self.pylToHtmlResult+=str(""" &quot;HTML&quot;""")
		self.pylToHtmlResult+=str(""" +""")
		self.pylToHtmlResult+=str(""" &quot;""")
		self.pylToHtmlResult+=str(""" +""")
		self.pylToHtmlResult+=str(""" &quot;""")
		self.pylToHtmlResult+=str(""" +""")
		self.pylToHtmlResult+=str(""" &quot;python&quot;""")
		self.pylToHtmlResult+=str("""
				$&gt;""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""
				&lt;$=pyl$&gt;""")
		self.pylToHtmlResult+=str("""
				</p>""")
		self.pylToHtmlResult+=str("""
			</pre>""")
		self.pylToHtmlResult+=str("""
			<p>""")
		self.pylToHtmlResult+=str("""The""")
		self.pylToHtmlResult+=str(""" pyl""")
		self.pylToHtmlResult+=str(""" code""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" translated""")
		self.pylToHtmlResult+=str(""" by""")
		self.pylToHtmlResult+=str(""" Pylatte""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" HTML""")
		self.pylToHtmlResult+=str(""" in""")
		self.pylToHtmlResult+=str(""" the""")
		self.pylToHtmlResult+=str(""" browser.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
			<pre class="brush: xml">""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""Pylatte""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""
				HTML""")
		self.pylToHtmlResult+=str(""" +""")
		self.pylToHtmlResult+=str(""" python""")
		self.pylToHtmlResult+=str("""
				</p>""")
		self.pylToHtmlResult+=str("""
			</pre>""")
		self.pylToHtmlResult+=str("""
			
			<h2>""")
		self.pylToHtmlResult+=str("""Functions""")
		self.pylToHtmlResult+=str("""</h2>""")
		self.pylToHtmlResult+=str("""
			<ul>""")
		self.pylToHtmlResult+=str("""
				<li>""")
		self.pylToHtmlResult+=str("""<h3>""")
		self.pylToHtmlResult+=str("""Translation""")
		self.pylToHtmlResult+=str(""" Engine""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""Pylatte""")
		self.pylToHtmlResult+=str(""" uses""")
		self.pylToHtmlResult+=str(""" pyl""")
		self.pylToHtmlResult+=str(""" file""")
		self.pylToHtmlResult+=str(""" format.""")
		self.pylToHtmlResult+=str(""" pyl""")
		self.pylToHtmlResult+=str(""" consists""")
		self.pylToHtmlResult+=str(""" of""")
		self.pylToHtmlResult+=str(""" HTML""")
		self.pylToHtmlResult+=str(""" and""")
		self.pylToHtmlResult+=str(""" Python.""")
		self.pylToHtmlResult+=str(""" pyl""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" fully""")
		self.pylToHtmlResult+=str(""" translated""")
		self.pylToHtmlResult+=str(""" by""")
		self.pylToHtmlResult+=str(""" the""")
		self.pylToHtmlResult+=str(""" Pylatte""")
		self.pylToHtmlResult+=str(""" engine""")
		self.pylToHtmlResult+=str(""" into""")
		self.pylToHtmlResult+=str(""" HTML.""")
		self.pylToHtmlResult+=str(""" It""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" unique""")
		self.pylToHtmlResult+=str(""" feature""")
		self.pylToHtmlResult+=str(""" of""")
		self.pylToHtmlResult+=str(""" Pylatte.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				<li>""")
		self.pylToHtmlResult+=str("""<h3>""")
		self.pylToHtmlResult+=str("""Database""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""To""")
		self.pylToHtmlResult+=str(""" use""")
		self.pylToHtmlResult+=str(""" the""")
		self.pylToHtmlResult+=str(""" database,""")
		self.pylToHtmlResult+=str(""" a""")
		self.pylToHtmlResult+=str(""" single""")
		self.pylToHtmlResult+=str(""" external""")
		self.pylToHtmlResult+=str(""" library""")
		self.pylToHtmlResult+=str(""" must""")
		self.pylToHtmlResult+=str(""" be""")
		self.pylToHtmlResult+=str(""" installed:""")
		self.pylToHtmlResult+=str(""" the""")
		self.pylToHtmlResult+=str(""" MySQLdb""")
		self.pylToHtmlResult+=str(""" module""")
		self.pylToHtmlResult+=str(""" for""")
		self.pylToHtmlResult+=str(""" Python""")
		self.pylToHtmlResult+=str(""" 3.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""Simple""")
		self.pylToHtmlResult+=str(""" and""")
		self.pylToHtmlResult+=str(""" advanced""")
		self.pylToHtmlResult+=str(""" SQL""")
		self.pylToHtmlResult+=str(""" via""")
		self.pylToHtmlResult+=str(""" specific""")
		self.pylToHtmlResult+=str(""" functions""")
		self.pylToHtmlResult+=str(""" that""")
		self.pylToHtmlResult+=str(""" are""")
		self.pylToHtmlResult+=str(""" similar""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" iBATIS""")
		self.pylToHtmlResult+=str(""" are""")
		self.pylToHtmlResult+=str(""" provided.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				<li>""")
		self.pylToHtmlResult+=str("""<h3>""")
		self.pylToHtmlResult+=str("""Session""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""A""")
		self.pylToHtmlResult+=str(""" session""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" needed""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" distinguish""")
		self.pylToHtmlResult+=str(""" each""")
		self.pylToHtmlResult+=str(""" client.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				<li>""")
		self.pylToHtmlResult+=str("""<h3>""")
		self.pylToHtmlResult+=str("""Filter""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""If""")
		self.pylToHtmlResult+=str(""" a""")
		self.pylToHtmlResult+=str(""" filter""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" set,""")
		self.pylToHtmlResult+=str(""" select""")
		self.pylToHtmlResult+=str(""" pages""")
		self.pylToHtmlResult+=str(""" pass""")
		self.pylToHtmlResult+=str(""" through""")
		self.pylToHtmlResult+=str(""" the""")
		self.pylToHtmlResult+=str(""" filter.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				<li>""")
		self.pylToHtmlResult+=str("""<h3>""")
		self.pylToHtmlResult+=str("""Form""")
		self.pylToHtmlResult+=str(""" File""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""It""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" possible""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" upload""")
		self.pylToHtmlResult+=str(""" a""")
		self.pylToHtmlResult+=str(""" file""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" server""")
		self.pylToHtmlResult+=str(""" via""")
		self.pylToHtmlResult+=str(""" POST.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				<li>""")
		self.pylToHtmlResult+=str("""<h3>""")
		self.pylToHtmlResult+=str("""URL""")
		self.pylToHtmlResult+=str(""" Mapping""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""For""")
		self.pylToHtmlResult+=str(""" security""")
		self.pylToHtmlResult+=str(""" purposes,""")
		self.pylToHtmlResult+=str(""" URL""")
		self.pylToHtmlResult+=str(""" mapping""")
		self.pylToHtmlResult+=str(""" transfers""")
		self.pylToHtmlResult+=str(""" virtual""")
		self.pylToHtmlResult+=str(""" URLs""")
		self.pylToHtmlResult+=str(""" accessed""")
		self.pylToHtmlResult+=str(""" by""")
		self.pylToHtmlResult+=str(""" clients""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" web""")
		self.pylToHtmlResult+=str(""" pages.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
			</ul>""")
		self.pylToHtmlResult+=str("""
			
			<h2>""")
		self.pylToHtmlResult+=str("""History""")
		self.pylToHtmlResult+=str("""</h2>""")
		self.pylToHtmlResult+=str("""
			<ul>""")
		self.pylToHtmlResult+=str("""
				<li>""")
		self.pylToHtmlResult+=str("""<h3>""")
		self.pylToHtmlResult+=str("""2011.""")
		self.pylToHtmlResult+=str(""" 05.""")
		self.pylToHtmlResult+=str(""" 13""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""The""")
		self.pylToHtmlResult+=str(""" Pylatte""")
		self.pylToHtmlResult+=str(""" project""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" created""")
		self.pylToHtmlResult+=str(""" in""")
		self.pylToHtmlResult+=str(""" Busan,""")
		self.pylToHtmlResult+=str(""" South""")
		self.pylToHtmlResult+=str(""" Korea.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				<li>""")
		self.pylToHtmlResult+=str("""<h3>""")
		self.pylToHtmlResult+=str("""2011.""")
		self.pylToHtmlResult+=str(""" 09.""")
		self.pylToHtmlResult+=str(""" 02""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""Initial""")
		self.pylToHtmlResult+=str(""" design""")
		self.pylToHtmlResult+=str(""" and""")
		self.pylToHtmlResult+=str(""" development""")
		self.pylToHtmlResult+=str(""" of""")
		self.pylToHtmlResult+=str(""" the""")
		self.pylToHtmlResult+=str(""" Pylatte""")
		self.pylToHtmlResult+=str(""" project.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				<li>""")
		self.pylToHtmlResult+=str("""<h3>""")
		self.pylToHtmlResult+=str("""2011.""")
		self.pylToHtmlResult+=str(""" 10.""")
		self.pylToHtmlResult+=str(""" 31""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
				<p>""")
		self.pylToHtmlResult+=str("""Pylatte""")
		self.pylToHtmlResult+=str(""" 0.9v""")
		self.pylToHtmlResult+=str(""" released.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
			</ul>""")
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
							<li data-theme="b">""")
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
							<li>""")
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

		</body>""")
		self.pylToHtmlResult+=str("""
	<!-- Finally, to actually run the highlighter, you need to include this JS on your page -->""")
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
