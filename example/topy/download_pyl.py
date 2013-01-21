# -*- coding: utf-8 -*- 
import Pylatte.WebServer.formFile as formFile
class download:
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
		self.pylToHtmlResult+=str("""Download""")
		self.pylToHtmlResult+=str("""</h1>""")
		self.pylToHtmlResult+=str("""
			<h2>""")
		self.pylToHtmlResult+=str("""Downloading""")
		self.pylToHtmlResult+=str(""" Pylatte""")
		self.pylToHtmlResult+=str("""</h2>""")
		self.pylToHtmlResult+=str("""
				<ul>""")
		self.pylToHtmlResult+=str("""
					<li>""")
		self.pylToHtmlResult+=str("""<h3>""")
		self.pylToHtmlResult+=str("""Released""")
		self.pylToHtmlResult+=str(""" Code""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
					<p>""")
		self.pylToHtmlResult+=str("""Latest""")
		self.pylToHtmlResult+=str(""" stable""")
		self.pylToHtmlResult+=str(""" release""")
		self.pylToHtmlResult+=str(""" :""")
		self.pylToHtmlResult+=str(""" <a href = "http://code.google.com/p/pylatte/downloads/list" target="_blank">""")
		self.pylToHtmlResult+=str("""here""")
		self.pylToHtmlResult+=str("""</a>""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
					<p>""")
		self.pylToHtmlResult+=str("""This""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" a""")
		self.pylToHtmlResult+=str(""" released""")
		self.pylToHtmlResult+=str(""" version""")
		self.pylToHtmlResult+=str(""" for""")
		self.pylToHtmlResult+=str(""" people""")
		self.pylToHtmlResult+=str(""" who""")
		self.pylToHtmlResult+=str(""" would""")
		self.pylToHtmlResult+=str(""" like""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" develop""")
		self.pylToHtmlResult+=str(""" website""")
		self.pylToHtmlResult+=str(""" using""")
		self.pylToHtmlResult+=str(""" pylatte.""")
		self.pylToHtmlResult+=str(""" This""")
		self.pylToHtmlResult+=str(""" includes""")
		self.pylToHtmlResult+=str(""" sample""")
		self.pylToHtmlResult+=str(""" sample""")
		self.pylToHtmlResult+=str(""" pages""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" help""")
		self.pylToHtmlResult+=str(""" people""")
		self.pylToHtmlResult+=str(""" develop""")
		self.pylToHtmlResult+=str(""" website.""")
		self.pylToHtmlResult+=str("""
			
					<li>""")
		self.pylToHtmlResult+=str("""<h3>""")
		self.pylToHtmlResult+=str("""Development""")
		self.pylToHtmlResult+=str(""" code""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
					<p>""")
		self.pylToHtmlResult+=str("""Latest""")
		self.pylToHtmlResult+=str(""" development""")
		self.pylToHtmlResult+=str(""" code""")
		self.pylToHtmlResult+=str(""" :""")
		self.pylToHtmlResult+=str(""" <a href = "http://code.google.com/p/pylatte/" target="_blank">""")
		self.pylToHtmlResult+=str("""here""")
		self.pylToHtmlResult+=str("""</a>""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
					<o>""")
		self.pylToHtmlResult+=str("""This""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" Development""")
		self.pylToHtmlResult+=str(""" code""")
		self.pylToHtmlResult+=str(""" for""")
		self.pylToHtmlResult+=str(""" developer""")
		self.pylToHtmlResult+=str(""" who""")
		self.pylToHtmlResult+=str(""" would""")
		self.pylToHtmlResult+=str(""" like""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" join""")
		self.pylToHtmlResult+=str(""" Pylatte""")
		self.pylToHtmlResult+=str(""" development""")
		self.pylToHtmlResult+=str(""" with""")
		self.pylToHtmlResult+=str(""" us.""")
		self.pylToHtmlResult+=str(""" Anyone""")
		self.pylToHtmlResult+=str(""" who""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" interested""")
		self.pylToHtmlResult+=str(""" in""")
		self.pylToHtmlResult+=str(""" development""")
		self.pylToHtmlResult+=str(""" of""")
		self.pylToHtmlResult+=str(""" Pylatte""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" welcome.""")
		self.pylToHtmlResult+=str(""" Join""")
		self.pylToHtmlResult+=str(""" us""")
		self.pylToHtmlResult+=str(""" now.""")
		self.pylToHtmlResult+=str("""
				</ul>""")
		self.pylToHtmlResult+=str("""
			<h2>""")
		self.pylToHtmlResult+=str("""Essential""")
		self.pylToHtmlResult+=str(""" Modules""")
		self.pylToHtmlResult+=str("""</h2>""")
		self.pylToHtmlResult+=str("""
				<ul>""")
		self.pylToHtmlResult+=str("""
					<li>""")
		self.pylToHtmlResult+=str("""<h3>""")
		self.pylToHtmlResult+=str("""PLY""")
		self.pylToHtmlResult+=str(""" (Python""")
		self.pylToHtmlResult+=str(""" Lex-Yacc)""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
					<p>""")
		self.pylToHtmlResult+=str("""Latest""")
		self.pylToHtmlResult+=str(""" stable""")
		self.pylToHtmlResult+=str(""" release""")
		self.pylToHtmlResult+=str(""" :""")
		self.pylToHtmlResult+=str(""" <a href = "http://www.dabeaz.com/ply" target="_blank">""")
		self.pylToHtmlResult+=str("""ver""")
		self.pylToHtmlResult+=str(""" 3.4""")
		self.pylToHtmlResult+=str("""</a>""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
					<p>""")
		self.pylToHtmlResult+=str("""This""")
		self.pylToHtmlResult+=str(""" module""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" essential""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" execute""")
		self.pylToHtmlResult+=str(""" Pylatte.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				</ul>""")
		self.pylToHtmlResult+=str("""
				
			<h2>""")
		self.pylToHtmlResult+=str("""Extra""")
		self.pylToHtmlResult+=str(""" Modules""")
		self.pylToHtmlResult+=str("""</h2>""")
		self.pylToHtmlResult+=str("""
				<ul>""")
		self.pylToHtmlResult+=str("""
					<li>""")
		self.pylToHtmlResult+=str("""<h3>""")
		self.pylToHtmlResult+=str("""Mysqldb""")
		self.pylToHtmlResult+=str(""" for""")
		self.pylToHtmlResult+=str(""" python3""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
					<p>""")
		self.pylToHtmlResult+=str("""Latest""")
		self.pylToHtmlResult+=str(""" stable""")
		self.pylToHtmlResult+=str(""" release""")
		self.pylToHtmlResult+=str(""" :""")
		self.pylToHtmlResult+=str(""" <a href = "https://github.com/davispuh/MySQL-for-Python-3" target="_blank">""")
		self.pylToHtmlResult+=str("""ver""")
		self.pylToHtmlResult+=str(""" 3.6.2""")
		self.pylToHtmlResult+=str("""</a>""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
					<p>""")
		self.pylToHtmlResult+=str("""Some""")
		self.pylToHtmlResult+=str(""" people""")
		self.pylToHtmlResult+=str(""" who""")
		self.pylToHtmlResult+=str(""" are""")
		self.pylToHtmlResult+=str(""" very""")
		self.pylToHtmlResult+=str(""" kind""")
		self.pylToHtmlResult+=str(""" alreay""")
		self.pylToHtmlResult+=str(""" made""")
		self.pylToHtmlResult+=str(""" mysqldb""")
		self.pylToHtmlResult+=str(""" module""")
		self.pylToHtmlResult+=str(""" for""")
		self.pylToHtmlResult+=str(""" python3.""")
		self.pylToHtmlResult+=str(""" This""")
		self.pylToHtmlResult+=str(""" module""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" absoluately""")
		self.pylToHtmlResult+=str(""" essential""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" use""")
		self.pylToHtmlResult+=str(""" Pylatte""")
		self.pylToHtmlResult+=str(""" with""")
		self.pylToHtmlResult+=str(""" Mysql.""")
		self.pylToHtmlResult+=str(""" If""")
		self.pylToHtmlResult+=str(""" you""")
		self.pylToHtmlResult+=str(""" need""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" use""")
		self.pylToHtmlResult+=str(""" mysql""")
		self.pylToHtmlResult+=str(""" on""")
		self.pylToHtmlResult+=str(""" your""")
		self.pylToHtmlResult+=str(""" website""")
		self.pylToHtmlResult+=str(""" based""")
		self.pylToHtmlResult+=str(""" on""")
		self.pylToHtmlResult+=str(""" Pylatte,""")
		self.pylToHtmlResult+=str(""" you""")
		self.pylToHtmlResult+=str(""" must""")
		self.pylToHtmlResult+=str(""" download.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
				</ul>""")
		self.pylToHtmlResult+=str("""
				<ul>""")
		self.pylToHtmlResult+=str("""
					<li>""")
		self.pylToHtmlResult+=str("""<h3>""")
		self.pylToHtmlResult+=str("""pyMongo""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
					<p>""")
		self.pylToHtmlResult+=str("""Latest""")
		self.pylToHtmlResult+=str(""" stable""")
		self.pylToHtmlResult+=str(""" release""")
		self.pylToHtmlResult+=str(""" :""")
		self.pylToHtmlResult+=str(""" <a href = "https://github.com/mongodb/mongo-python-driver" target="_blank">""")
		self.pylToHtmlResult+=str("""here""")
		self.pylToHtmlResult+=str("""</a>""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
					<p>""")
		self.pylToHtmlResult+=str("""The""")
		self.pylToHtmlResult+=str(""" PyMongo""")
		self.pylToHtmlResult+=str(""" distribution""")
		self.pylToHtmlResult+=str(""" contains""")
		self.pylToHtmlResult+=str(""" tools""")
		self.pylToHtmlResult+=str(""" for""")
		self.pylToHtmlResult+=str(""" interacting""")
		self.pylToHtmlResult+=str(""" with""")
		self.pylToHtmlResult+=str(""" MongoDB""")
		self.pylToHtmlResult+=str(""" database""")
		self.pylToHtmlResult+=str(""" from""")
		self.pylToHtmlResult+=str(""" Python.""")
		self.pylToHtmlResult+=str(""" This""")
		self.pylToHtmlResult+=str(""" module""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" absoluately""")
		self.pylToHtmlResult+=str(""" essential""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" use""")
		self.pylToHtmlResult+=str(""" Pylatte""")
		self.pylToHtmlResult+=str(""" with""")
		self.pylToHtmlResult+=str(""" MongoDB.""")
		self.pylToHtmlResult+=str(""" If""")
		self.pylToHtmlResult+=str(""" you""")
		self.pylToHtmlResult+=str(""" need""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" use""")
		self.pylToHtmlResult+=str(""" MongoDB""")
		self.pylToHtmlResult+=str(""" on""")
		self.pylToHtmlResult+=str(""" your""")
		self.pylToHtmlResult+=str(""" website""")
		self.pylToHtmlResult+=str(""" based""")
		self.pylToHtmlResult+=str(""" on""")
		self.pylToHtmlResult+=str(""" Pylatte,""")
		self.pylToHtmlResult+=str(""" you""")
		self.pylToHtmlResult+=str(""" must""")
		self.pylToHtmlResult+=str(""" download.""")
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
							<li>""")
		self.pylToHtmlResult+=str("""<a target="_self" href="../index">""")
		self.pylToHtmlResult+=str("""About""")
		self.pylToHtmlResult+=str("""</a>""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<li data-theme="b">""")
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
							<li>""")
		self.pylToHtmlResult+=str("""<a target="_self" href="../demo1">""")
		self.pylToHtmlResult+=str("""Demo1""")
		self.pylToHtmlResult+=str("""</a>""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""<a target="_self" href="../demo2">""")
		self.pylToHtmlResult+=str("""Demo2""")
		self.pylToHtmlResult+=str("""</a>""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""<a target="_self" href="../demo3">""")
		self.pylToHtmlResult+=str("""Demo3""")
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
</html>""")
		self.sessionDic=session
		pass
	def getHtml(self):
		return self.pylToHtmlResult
		pass
	def getSession(self):
		return self.sessionDic
		pass
