# -*- coding: utf-8 -*- 
import Pylatte.WebServer.formFile as formFile
class documentation:
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
		self.pylToHtmlResult+=str("""Documentation""")
		self.pylToHtmlResult+=str("""</h1>""")
		self.pylToHtmlResult+=str("""
				<div data-role="collapsible-set" data-theme="c" data-content-theme="d">""")
		self.pylToHtmlResult+=str("""
				<div data-role="listview" data-inset="true" data-filter="true" data-filter-theme="c">""")
		self.pylToHtmlResult+=str("""
					<div data-role="collapsible" data-collapsed="true">""")
		self.pylToHtmlResult+=str("""
						<h3>""")
		self.pylToHtmlResult+=str("""pylatte_config.xml""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""
						<p>""")
		self.pylToHtmlResult+=str("""Configuration""")
		self.pylToHtmlResult+=str(""" about""")
		self.pylToHtmlResult+=str(""" Server""")
		self.pylToHtmlResult+=str(""" port""")
		self.pylToHtmlResult+=str(""" number,""")
		self.pylToHtmlResult+=str(""" URL""")
		self.pylToHtmlResult+=str(""" Mapping,""")
		self.pylToHtmlResult+=str(""" and""")
		self.pylToHtmlResult+=str(""" Filter""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
						<pre class="brush: xml">""")
		self.pylToHtmlResult+=str("""
							<config>""")
		self.pylToHtmlResult+=str("""
								<pylatte-server>""")
		self.pylToHtmlResult+=str("""
									<port>""")
		self.pylToHtmlResult+=str("""80""")
		self.pylToHtmlResult+=str("""</port>""")
		self.pylToHtmlResult+=str("""<!-- Pylatte web server port number. 80 set by default -->""")
		self.pylToHtmlResult+=str("""
								</pylatte-server>""")
		self.pylToHtmlResult+=str("""
							
								<latteUrl>""")
		self.pylToHtmlResult+=str("""<!-- URL Mapping pairs -->""")
		self.pylToHtmlResult+=str("""
									<!-- From hostname/pylatte to hostname/sample.pyl -->""")
		self.pylToHtmlResult+=str("""
									<!-- pylatte-name is a just name of each pair. -->""")
		self.pylToHtmlResult+=str("""
									<pylatte>""")
		self.pylToHtmlResult+=str("""
										<pylatte-name>""")
		self.pylToHtmlResult+=str("""mapping_test""")
		self.pylToHtmlResult+=str("""</pylatte-name>""")
		self.pylToHtmlResult+=str("""
										<pylatte-pyl>""")
		self.pylToHtmlResult+=str("""sample.pyl""")
		self.pylToHtmlResult+=str("""</pylatte-pyl>""")
		self.pylToHtmlResult+=str("""
									</pylatte>""")
		self.pylToHtmlResult+=str("""
									<pylatte-mapping>""")
		self.pylToHtmlResult+=str("""
										<pylatte-name>""")
		self.pylToHtmlResult+=str("""mapping_test""")
		self.pylToHtmlResult+=str("""</pylatte-name>""")
		self.pylToHtmlResult+=str("""
										<url-mapping>""")
		self.pylToHtmlResult+=str("""/pylatte""")
		self.pylToHtmlResult+=str("""</url-mapping>""")
		self.pylToHtmlResult+=str("""
									</pylatte-mapping>""")
		self.pylToHtmlResult+=str("""
								</latteUrl>""")
		self.pylToHtmlResult+=str("""
								
								<latteFilter>""")
		self.pylToHtmlResult+=str("""<!-- Filter pairs -->""")
		self.pylToHtmlResult+=str("""
									<!-- filter-pyl code are executed first before filter-url pages are accessed -->""")
		self.pylToHtmlResult+=str("""
									<!-- filter-name is a just name of each pair. -->""")
		self.pylToHtmlResult+=str("""
									<filter>""")
		self.pylToHtmlResult+=str("""
										<filter-name>""")
		self.pylToHtmlResult+=str("""filter_test""")
		self.pylToHtmlResult+=str("""</filter-name>""")
		self.pylToHtmlResult+=str("""
										<filter-pyl>""")
		self.pylToHtmlResult+=str("""filter/sample_filter.pyl""")
		self.pylToHtmlResult+=str("""</filter-pyl>""")
		self.pylToHtmlResult+=str("""
									</filter>""")
		self.pylToHtmlResult+=str("""
									<filter-mapping>""")
		self.pylToHtmlResult+=str("""
										<filter-name>""")
		self.pylToHtmlResult+=str("""filter_test""")
		self.pylToHtmlResult+=str("""</filter-name>""")
		self.pylToHtmlResult+=str("""
										<filter-url>""")
		self.pylToHtmlResult+=str("""documenation.pyl""")
		self.pylToHtmlResult+=str("""</filter-url>""")
		self.pylToHtmlResult+=str("""
										<filter-url>""")
		self.pylToHtmlResult+=str("""tutorial.pyl""")
		self.pylToHtmlResult+=str("""</filter-url>""")
		self.pylToHtmlResult+=str("""
										<filter-url>""")
		self.pylToHtmlResult+=str("""contact.pyl""")
		self.pylToHtmlResult+=str("""</filter-url>""")
		self.pylToHtmlResult+=str("""
									</filter-mapping>""")
		self.pylToHtmlResult+=str("""
								</latteFilter>""")
		self.pylToHtmlResult+=str("""
							</config>""")
		self.pylToHtmlResult+=str("""
						</pre>""")
		self.pylToHtmlResult+=str("""
					</div>""")
		self.pylToHtmlResult+=str("""
					<div data-role="collapsible"  data-collapsed="true">""")
		self.pylToHtmlResult+=str("""
						<h3>""")
		self.pylToHtmlResult+=str("""db_mapping.xml""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""
						<p>""")
		self.pylToHtmlResult+=str("""Configuration""")
		self.pylToHtmlResult+=str(""" about""")
		self.pylToHtmlResult+=str(""" database""")
		self.pylToHtmlResult+=str(""" information""")
		self.pylToHtmlResult+=str(""" and""")
		self.pylToHtmlResult+=str(""" using""")
		self.pylToHtmlResult+=str(""" advanced""")
		self.pylToHtmlResult+=str(""" SQL""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
						<pre class="brush: xml">""")
		self.pylToHtmlResult+=str("""
							<database>""")
		self.pylToHtmlResult+=str("""
								<sql db="mysql">""")
		self.pylToHtmlResult+=str("""<!-- information about MySQL to connect database -->""")
		self.pylToHtmlResult+=str("""
									<host>""")
		self.pylToHtmlResult+=str("""localhost""")
		self.pylToHtmlResult+=str("""</host>""")
		self.pylToHtmlResult+=str("""
									<user>""")
		self.pylToHtmlResult+=str("""root""")
		self.pylToHtmlResult+=str("""</user>""")
		self.pylToHtmlResult+=str("""
									<password>""")
		self.pylToHtmlResult+=str("""pylatte""")
		self.pylToHtmlResult+=str("""</password>""")
		self.pylToHtmlResult+=str("""
									<dbName>""")
		self.pylToHtmlResult+=str("""pylatte""")
		self.pylToHtmlResult+=str("""</dbName>""")
		self.pylToHtmlResult+=str("""
								</sql>""")
		self.pylToHtmlResult+=str("""
								
								<sqlmap id="user">""")
		self.pylToHtmlResult+=str("""<!-- SQL set-->""")
		self.pylToHtmlResult+=str("""
									<!-- SQL list to use -->""")
		self.pylToHtmlResult+=str("""
									<!-- $variable$ is replaced with python variable -->""")
		self.pylToHtmlResult+=str("""
								    <seIect id="select1">""")
		self.pylToHtmlResult+=str("""SELECT""")
		self.pylToHtmlResult+=str(""" *""")
		self.pylToHtmlResult+=str(""" FROM""")
		self.pylToHtmlResult+=str(""" table""")
		self.pylToHtmlResult+=str("""</select>""")
		self.pylToHtmlResult+=str("""
								    <seIect id="select2">""")
		self.pylToHtmlResult+=str("""SELECT""")
		self.pylToHtmlResult+=str(""" *""")
		self.pylToHtmlResult+=str(""" FROM""")
		self.pylToHtmlResult+=str(""" table""")
		self.pylToHtmlResult+=str(""" WHERE""")
		self.pylToHtmlResult+=str(""" age""")
		self.pylToHtmlResult+=str(""" =""")
		self.pylToHtmlResult+=str(""" $age$""")
		self.pylToHtmlResult+=str("""</select>""")
		self.pylToHtmlResult+=str("""
								    <insert id="insert1">""")
		self.pylToHtmlResult+=str("""INSERT""")
		self.pylToHtmlResult+=str(""" INTO""")
		self.pylToHtmlResult+=str(""" table""")
		self.pylToHtmlResult+=str(""" VALUES""")
		self.pylToHtmlResult+=str(""" ($name$,""")
		self.pylToHtmlResult+=str(""" $age$)""")
		self.pylToHtmlResult+=str("""</insert>""")
		self.pylToHtmlResult+=str("""
								    <update id="update1">""")
		self.pylToHtmlResult+=str("""UPDATE""")
		self.pylToHtmlResult+=str(""" table""")
		self.pylToHtmlResult+=str(""" SET""")
		self.pylToHtmlResult+=str(""" age""")
		self.pylToHtmlResult+=str(""" =""")
		self.pylToHtmlResult+=str(""" $age$""")
		self.pylToHtmlResult+=str(""" WHERE""")
		self.pylToHtmlResult+=str(""" name""")
		self.pylToHtmlResult+=str(""" =""")
		self.pylToHtmlResult+=str(""" $name$""")
		self.pylToHtmlResult+=str("""</update>""")
		self.pylToHtmlResult+=str("""
								    <delete id="delete1">""")
		self.pylToHtmlResult+=str("""DELETE""")
		self.pylToHtmlResult+=str(""" FROM""")
		self.pylToHtmlResult+=str(""" table""")
		self.pylToHtmlResult+=str(""" WHERE""")
		self.pylToHtmlResult+=str(""" age""")
		self.pylToHtmlResult+=str(""" =""")
		self.pylToHtmlResult+=str(""" $age$""")
		self.pylToHtmlResult+=str("""</delete>""")
		self.pylToHtmlResult+=str("""
								</sqlmap>""")
		self.pylToHtmlResult+=str("""
							</database>""")
		self.pylToHtmlResult+=str("""
						</pre>""")
		self.pylToHtmlResult+=str("""
					</div>""")
		self.pylToHtmlResult+=str("""
					<div data-role="collapsible"  data-collapsed="true">""")
		self.pylToHtmlResult+=str("""
						<h3>""")
		self.pylToHtmlResult+=str("""latteServerStart.py""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""
						<p>""")
		self.pylToHtmlResult+=str("""Turn""")
		self.pylToHtmlResult+=str(""" on""")
		self.pylToHtmlResult+=str(""" Pylatte""")
		self.pylToHtmlResult+=str(""" web""")
		self.pylToHtmlResult+=str(""" server""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
						<ul>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""parseServerPort()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Set""")
		self.pylToHtmlResult+=str(""" a""")
		self.pylToHtmlResult+=str(""" server""")
		self.pylToHtmlResult+=str(""" port""")
		self.pylToHtmlResult+=str(""" number""")
		self.pylToHtmlResult+=str(""" by""")
		self.pylToHtmlResult+=str(""" reading""")
		self.pylToHtmlResult+=str(""" pylatte_config.xml""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""worker()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Work""")
		self.pylToHtmlResult+=str(""" a""")
		self.pylToHtmlResult+=str(""" server""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""my_service()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""checking""")
		self.pylToHtmlResult+=str(""" a""")
		self.pylToHtmlResult+=str(""" command""")
		self.pylToHtmlResult+=str(""" from""")
		self.pylToHtmlResult+=str(""" interective""")
		self.pylToHtmlResult+=str(""" prompt.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
						</ul>""")
		self.pylToHtmlResult+=str("""
					</div>""")
		self.pylToHtmlResult+=str("""
					<div data-role="collapsible"  data-collapsed="true">""")
		self.pylToHtmlResult+=str("""
						<h3>""")
		self.pylToHtmlResult+=str("""pyLatteConfigParser""")
		self.pylToHtmlResult+=str(""" Class""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""
						<p>""")
		self.pylToHtmlResult+=str("""This""")
		self.pylToHtmlResult+=str(""" class""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" just""")
		self.pylToHtmlResult+=str(""" for""")
		self.pylToHtmlResult+=str(""" a""")
		self.pylToHtmlResult+=str(""" test.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
						<ul>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""__init__()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Set""")
		self.pylToHtmlResult+=str(""" a""")
		self.pylToHtmlResult+=str(""" Mapping""")
		self.pylToHtmlResult+=str(""" information""")
		self.pylToHtmlResult+=str(""" and""")
		self.pylToHtmlResult+=str(""" Filter""")
		self.pylToHtmlResult+=str(""" information""")
		self.pylToHtmlResult+=str(""" by""")
		self.pylToHtmlResult+=str(""" reading""")
		self.pylToHtmlResult+=str(""" pylatte_config.xml""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""parserUrlMappingExcute()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Bring""")
		self.pylToHtmlResult+=str(""" the""")
		self.pylToHtmlResult+=str(""" path""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" access(execute)""")
		self.pylToHtmlResult+=str(""" pyl""")
		self.pylToHtmlResult+=str(""" file""")
		self.pylToHtmlResult+=str(""" actually""")
		self.pylToHtmlResult+=str(""" from""")
		self.pylToHtmlResult+=str(""" a""")
		self.pylToHtmlResult+=str(""" xml""")
		self.pylToHtmlResult+=str(""" file""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""parseUrlMappingUrl()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Bring""")
		self.pylToHtmlResult+=str(""" the""")
		self.pylToHtmlResult+=str(""" virtual""")
		self.pylToHtmlResult+=str(""" URL""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" link""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" one""")
		self.pylToHtmlResult+=str(""" pyl""")
		self.pylToHtmlResult+=str(""" file""")
		self.pylToHtmlResult+=str(""" from""")
		self.pylToHtmlResult+=str(""" a""")
		self.pylToHtmlResult+=str(""" xml""")
		self.pylToHtmlResult+=str(""" file""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""makeUrlMap()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Make""")
		self.pylToHtmlResult+=str(""" dictionay""")
		self.pylToHtmlResult+=str(""" mapping""")
		self.pylToHtmlResult+=str(""" data""")
		self.pylToHtmlResult+=str(""" pairs""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""parseFilterPyl()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Bring""")
		self.pylToHtmlResult+=str(""" the""")
		self.pylToHtmlResult+=str(""" path""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" filter""")
		self.pylToHtmlResult+=str(""" pyl""")
		self.pylToHtmlResult+=str(""" file""")
		self.pylToHtmlResult+=str(""" actually""")
		self.pylToHtmlResult+=str(""" from""")
		self.pylToHtmlResult+=str(""" a""")
		self.pylToHtmlResult+=str(""" xml""")
		self.pylToHtmlResult+=str(""" file""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""parseFilterUrl()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Bring""")
		self.pylToHtmlResult+=str(""" the""")
		self.pylToHtmlResult+=str(""" path""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" be""")
		self.pylToHtmlResult+=str(""" filtered""")
		self.pylToHtmlResult+=str(""" pyl""")
		self.pylToHtmlResult+=str(""" files""")
		self.pylToHtmlResult+=str(""" from""")
		self.pylToHtmlResult+=str(""" a""")
		self.pylToHtmlResult+=str(""" xml""")
		self.pylToHtmlResult+=str(""" file""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""makeFilterMap()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Make""")
		self.pylToHtmlResult+=str(""" dictionay""")
		self.pylToHtmlResult+=str(""" filter""")
		self.pylToHtmlResult+=str(""" data""")
		self.pylToHtmlResult+=str(""" pairs""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""getUrlMap()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""getDataBaseInfo()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""getFilterMap()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
						</ul>""")
		self.pylToHtmlResult+=str("""
					</div>""")
		self.pylToHtmlResult+=str("""
					<div data-role="collapsible"  data-collapsed="true">""")
		self.pylToHtmlResult+=str("""
						<h3>""")
		self.pylToHtmlResult+=str("""pyLatteDBMappingParser""")
		self.pylToHtmlResult+=str(""" Class""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""
						<p>""")
		self.pylToHtmlResult+=str("""To""")
		self.pylToHtmlResult+=str(""" deal""")
		self.pylToHtmlResult+=str(""" with""")
		self.pylToHtmlResult+=str(""" database""")
		self.pylToHtmlResult+=str(""" based""")
		self.pylToHtmlResult+=str(""" on""")
		self.pylToHtmlResult+=str(""" MySQL""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
						<ul>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""__init__()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Ready""")
		self.pylToHtmlResult+=str(""" for""")
		self.pylToHtmlResult+=str(""" reading""")
		self.pylToHtmlResult+=str(""" database""")
		self.pylToHtmlResult+=str(""" information""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""loadXmlFromFile()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Load""")
		self.pylToHtmlResult+=str(""" XML""")
		self.pylToHtmlResult+=str(""" document""")
		self.pylToHtmlResult+=str(""" about""")
		self.pylToHtmlResult+=str(""" database""")
		self.pylToHtmlResult+=str(""" information""")
		self.pylToHtmlResult+=str(""" and""")
		self.pylToHtmlResult+=str(""" SQL""")
		self.pylToHtmlResult+=str(""" Mapping""")
		self.pylToHtmlResult+=str(""" information""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""parseDataBaseInfo()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Get""")
		self.pylToHtmlResult+=str(""" database""")
		self.pylToHtmlResult+=str(""" information(host,""")
		self.pylToHtmlResult+=str(""" user,""")
		self.pylToHtmlResult+=str(""" password,""")
		self.pylToHtmlResult+=str(""" database""")
		self.pylToHtmlResult+=str(""" name)""")
		self.pylToHtmlResult+=str(""" from""")
		self.pylToHtmlResult+=str(""" XML""")
		self.pylToHtmlResult+=str(""" document""")
		self.pylToHtmlResult+=str("""
        And""")
		self.pylToHtmlResult+=str(""" Connect""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" MySQL""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" use""")
		self.pylToHtmlResult+=str(""" the""")
		self.pylToHtmlResult+=str(""" database""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
        					<li>""")
		self.pylToHtmlResult+=str("""queryProcessing""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
        					<p>""")
		self.pylToHtmlResult+=str("""Execute""")
		self.pylToHtmlResult+=str(""" SQL""")
		self.pylToHtmlResult+=str(""" with""")
		self.pylToHtmlResult+=str(""" replacing""")
		self.pylToHtmlResult+=str(""" variables""")
		self.pylToHtmlResult+=str(""" in""")
		self.pylToHtmlResult+=str(""" SQL.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
        					<li>""")
		self.pylToHtmlResult+=str("""queryForList()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
        					<p>""")
		self.pylToHtmlResult+=str("""Looking""")
		self.pylToHtmlResult+=str(""" for""")
		self.pylToHtmlResult+=str(""" matched""")
		self.pylToHtmlResult+=str(""" SQL""")
		self.pylToHtmlResult+=str(""" with""")
		self.pylToHtmlResult+=str(""" specified""")
		self.pylToHtmlResult+=str(""" id""")
		self.pylToHtmlResult+=str(""" from""")
		self.pylToHtmlResult+=str(""" XML""")
		self.pylToHtmlResult+=str(""" document""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
						</ul>""")
		self.pylToHtmlResult+=str("""
					</div>""")
		self.pylToHtmlResult+=str("""
					<div data-role="collapsible"  data-collapsed="true">""")
		self.pylToHtmlResult+=str("""
						<h3>""")
		self.pylToHtmlResult+=str("""formFile""")
		self.pylToHtmlResult+=str(""" Class""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""
						<p>""")
		self.pylToHtmlResult+=str("""This""")
		self.pylToHtmlResult+=str(""" class""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" just""")
		self.pylToHtmlResult+=str(""" for""")
		self.pylToHtmlResult+=str(""" a""")
		self.pylToHtmlResult+=str(""" test.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
						<ul>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""__init__()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Initializing""")
		self.pylToHtmlResult+=str(""" variables.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""moveUploadFile()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Upload""")
		self.pylToHtmlResult+=str(""" files""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" indicated""")
		self.pylToHtmlResult+=str(""" path.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""getError""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Return""")
		self.pylToHtmlResult+=str(""" an""")
		self.pylToHtmlResult+=str(""" error""")
		self.pylToHtmlResult+=str(""" message.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
						</ul>""")
		self.pylToHtmlResult+=str("""
					</div>""")
		self.pylToHtmlResult+=str("""
					<div data-role="collapsible" data-collapsed="true">""")
		self.pylToHtmlResult+=str("""
						<h3>""")
		self.pylToHtmlResult+=str("""latteServer""")
		self.pylToHtmlResult+=str(""" Class""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""
						<p>""")
		self.pylToHtmlResult+=str("""This""")
		self.pylToHtmlResult+=str(""" class""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" just""")
		self.pylToHtmlResult+=str(""" for""")
		self.pylToHtmlResult+=str(""" a""")
		self.pylToHtmlResult+=str(""" test.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
						<ul>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""__init__()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Read""")
		self.pylToHtmlResult+=str(""" URL""")
		self.pylToHtmlResult+=str(""" mapping""")
		self.pylToHtmlResult+=str(""" and""")
		self.pylToHtmlResult+=str(""" database""")
		self.pylToHtmlResult+=str(""" information""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""do_GET()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""GET""")
		self.pylToHtmlResult+=str(""" parameter""")
		self.pylToHtmlResult+=str(""" processing""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""do_POST()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""POST""")
		self.pylToHtmlResult+=str(""" parameter""")
		self.pylToHtmlResult+=str(""" processing""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""do_HEAD()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Head""")
		self.pylToHtmlResult+=str(""" in""")
		self.pylToHtmlResult+=str(""" formation""")
		self.pylToHtmlResult+=str(""" processing""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""send_head()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""This""")
		self.pylToHtmlResult+=str(""" sends""")
		self.pylToHtmlResult+=str(""" the""")
		self.pylToHtmlResult+=str(""" response""")
		self.pylToHtmlResult+=str(""" code""")
		self.pylToHtmlResult+=str(""" and""")
		self.pylToHtmlResult+=str(""" MIME""")
		self.pylToHtmlResult+=str(""" headers.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
						</ul>""")
		self.pylToHtmlResult+=str("""
					</div>""")
		self.pylToHtmlResult+=str("""
					<div data-role="collapsible" data-collapsed="true">""")
		self.pylToHtmlResult+=str("""
						<h3>""")
		self.pylToHtmlResult+=str("""latteSocketServer""")
		self.pylToHtmlResult+=str(""" Class""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""
						<p>""")
		self.pylToHtmlResult+=str("""This""")
		self.pylToHtmlResult+=str(""" class""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" just""")
		self.pylToHtmlResult+=str(""" for""")
		self.pylToHtmlResult+=str(""" a""")
		self.pylToHtmlResult+=str(""" test.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
						<ul>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""__init__()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Server""")
		self.pylToHtmlResult+=str(""" started""")
		self.pylToHtmlResult+=str(""" entierly.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""server_bind()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Binding""")
		self.pylToHtmlResult+=str(""" a""")
		self.pylToHtmlResult+=str(""" server""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""shutdown()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Shut""")
		self.pylToHtmlResult+=str(""" down""")
		self.pylToHtmlResult+=str(""" a""")
		self.pylToHtmlResult+=str(""" server""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""sessionFileRemove()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Remove""")
		self.pylToHtmlResult+=str(""" session""")
		self.pylToHtmlResult+=str(""" files""")
		self.pylToHtmlResult+=str(""" generated""")
		self.pylToHtmlResult+=str(""" before""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
						</ul>""")
		self.pylToHtmlResult+=str("""
					</div>""")
		self.pylToHtmlResult+=str("""
					<div data-role="collapsible" data-collapsed="true">""")
		self.pylToHtmlResult+=str("""
						<h3>""")
		self.pylToHtmlResult+=str("""methodGetGetParam""")
		self.pylToHtmlResult+=str(""" Class""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""
						<p>""")
		self.pylToHtmlResult+=str("""Reading""")
		self.pylToHtmlResult+=str(""" GET""")
		self.pylToHtmlResult+=str(""" parameters""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
						<ul>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""__init__()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Parsing""")
		self.pylToHtmlResult+=str(""" GET""")
		self.pylToHtmlResult+=str(""" parameters""")
		self.pylToHtmlResult+=str(""" from""")
		self.pylToHtmlResult+=str(""" accessed""")
		self.pylToHtmlResult+=str(""" URL.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""getParam()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Return""")
		self.pylToHtmlResult+=str(""" GET""")
		self.pylToHtmlResult+=str(""" parameters""")
		self.pylToHtmlResult+=str(""" as""")
		self.pylToHtmlResult+=str(""" dictionary""")
		self.pylToHtmlResult+=str(""" type.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
						</ul>""")
		self.pylToHtmlResult+=str("""
					</div>""")
		self.pylToHtmlResult+=str("""
					<div data-role="collapsible" data-collapsed="true">""")
		self.pylToHtmlResult+=str("""
						<h3>""")
		self.pylToHtmlResult+=str("""methodGetPostParam""")
		self.pylToHtmlResult+=str(""" Class""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""
						<p>""")
		self.pylToHtmlResult+=str("""Reading""")
		self.pylToHtmlResult+=str(""" POST""")
		self.pylToHtmlResult+=str(""" parameters""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
						<ul>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""__init__()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Get""")
		self.pylToHtmlResult+=str(""" POST""")
		self.pylToHtmlResult+=str(""" parameters""")
		self.pylToHtmlResult+=str(""" from""")
		self.pylToHtmlResult+=str(""" a""")
		self.pylToHtmlResult+=str(""" loaded""")
		self.pylToHtmlResult+=str(""" page""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""getParam""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Return""")
		self.pylToHtmlResult+=str(""" POST""")
		self.pylToHtmlResult+=str(""" parameters""")
		self.pylToHtmlResult+=str(""" as""")
		self.pylToHtmlResult+=str(""" dictionary""")
		self.pylToHtmlResult+=str(""" type""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
						</ul>""")
		self.pylToHtmlResult+=str("""
					</div>""")
		self.pylToHtmlResult+=str("""
					<div data-role="collapsible" data-collapsed="true">""")
		self.pylToHtmlResult+=str("""
						<h3>""")
		self.pylToHtmlResult+=str("""postMultipartForm""")
		self.pylToHtmlResult+=str(""" Class""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""
						<p>""")
		self.pylToHtmlResult+=str("""This""")
		self.pylToHtmlResult+=str(""" class""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" used""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" send""")
		self.pylToHtmlResult+=str(""" multipart/form""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
						<ul>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""__init__()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Save""")
		self.pylToHtmlResult+=str(""" payload""")
		self.pylToHtmlResult+=str(""" datas""")
		self.pylToHtmlResult+=str(""" in""")
		self.pylToHtmlResult+=str(""" the""")
		self.pylToHtmlResult+=str(""" start""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""__splitPayload()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Split""")
		self.pylToHtmlResult+=str(""" received""")
		self.pylToHtmlResult+=str(""" datas""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""__analysisData()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Analysis""")
		self.pylToHtmlResult+=str(""" splited""")
		self.pylToHtmlResult+=str(""" datas""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""__getTmpHashKey()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Make""")
		self.pylToHtmlResult+=str(""" a""")
		self.pylToHtmlResult+=str(""" temporary""")
		self.pylToHtmlResult+=str(""" file""")
		self.pylToHtmlResult+=str(""" name.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""getFileInfo()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Return""")
		self.pylToHtmlResult+=str(""" file""")
		self.pylToHtmlResult+=str(""" information.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""getParam()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Retrun""")
		self.pylToHtmlResult+=str(""" input""")
		self.pylToHtmlResult+=str(""" data""")
		self.pylToHtmlResult+=str(""" except""")
		self.pylToHtmlResult+=str(""" for""")
		self.pylToHtmlResult+=str(""" file""")
		self.pylToHtmlResult+=str(""" information""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
						</ul>""")
		self.pylToHtmlResult+=str("""
					</div>""")
		self.pylToHtmlResult+=str("""
					<div data-role="collapsible" data-collapsed="true">""")
		self.pylToHtmlResult+=str("""
						<h3>""")
		self.pylToHtmlResult+=str("""pylToPy""")
		self.pylToHtmlResult+=str(""" Class""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""
						<p>""")
		self.pylToHtmlResult+=str("""Translation""")
		self.pylToHtmlResult+=str(""" module""")
		self.pylToHtmlResult+=str(""" from""")
		self.pylToHtmlResult+=str(""" pyl""")
		self.pylToHtmlResult+=str(""" file""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" py(python)""")
		self.pylToHtmlResult+=str(""" file""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
						<ul>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""__init__()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Read""")
		self.pylToHtmlResult+=str(""" a""")
		self.pylToHtmlResult+=str(""" pyl""")
		self.pylToHtmlResult+=str(""" file""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""translationPy()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Translate""")
		self.pylToHtmlResult+=str(""" code""")
		self.pylToHtmlResult+=str(""" from""")
		self.pylToHtmlResult+=str(""" .pyl""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" .py""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""outPy()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Get""")
		self.pylToHtmlResult+=str(""" original""")
		self.pylToHtmlResult+=str(""" pyl""")
		self.pylToHtmlResult+=str(""" name""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" save""")
		self.pylToHtmlResult+=str(""" py""")
		self.pylToHtmlResult+=str(""" file.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
						</ul>""")
		self.pylToHtmlResult+=str("""
					</div>""")
		self.pylToHtmlResult+=str("""
					<div data-role="collapsible" data-collapsed="true">""")
		self.pylToHtmlResult+=str("""
						<h3>""")
		self.pylToHtmlResult+=str("""requestHeaderInfo""")
		self.pylToHtmlResult+=str(""" Class""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""
						<p>""")
		self.pylToHtmlResult+=str("""Information""")
		self.pylToHtmlResult+=str(""" of""")
		self.pylToHtmlResult+=str(""" request""")
		self.pylToHtmlResult+=str(""" header""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
						<ul>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""__init__()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Generate""")
		self.pylToHtmlResult+=str(""" head""")
		self.pylToHtmlResult+=str(""" information""")
		self.pylToHtmlResult+=str(""" from""")
		self.pylToHtmlResult+=str(""" header""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""getHeaderInfo()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Return""")
		self.pylToHtmlResult+=str(""" header""")
		self.pylToHtmlResult+=str(""" information""")
		self.pylToHtmlResult+=str(""" as""")
		self.pylToHtmlResult+=str(""" dictionary""")
		self.pylToHtmlResult+=str(""" type""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
						</ul>""")
		self.pylToHtmlResult+=str("""
					</div>""")
		self.pylToHtmlResult+=str("""
					<div data-role="collapsible" data-collapsed="true">""")
		self.pylToHtmlResult+=str("""
						<h3>""")
		self.pylToHtmlResult+=str("""session""")
		self.pylToHtmlResult+=str(""" Class""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""
						<p>""")
		self.pylToHtmlResult+=str("""Dealing""")
		self.pylToHtmlResult+=str(""" with""")
		self.pylToHtmlResult+=str(""" session""")
		self.pylToHtmlResult+=str(""" information""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
						<ul>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""checkAvailableSession()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Check""")
		self.pylToHtmlResult+=str(""" whether""")
		self.pylToHtmlResult+=str(""" the""")
		self.pylToHtmlResult+=str(""" session""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" valid""")
		self.pylToHtmlResult+=str(""" or""")
		self.pylToHtmlResult+=str(""" not.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""genSessionKey()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Generate""")
		self.pylToHtmlResult+=str(""" session""")
		self.pylToHtmlResult+=str(""" file.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""setSessionData()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Save""")
		self.pylToHtmlResult+=str(""" file""")
		self.pylToHtmlResult+=str(""" using""")
		self.pylToHtmlResult+=str(""" generated""")
		self.pylToHtmlResult+=str(""" key""")
		self.pylToHtmlResult+=str(""" string""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""getSessionData()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Get""")
		self.pylToHtmlResult+=str(""" session""")
		self.pylToHtmlResult+=str(""" data""")
		self.pylToHtmlResult+=str(""" using""")
		self.pylToHtmlResult+=str(""" the""")
		self.pylToHtmlResult+=str(""" session""")
		self.pylToHtmlResult+=str(""" key.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""dictToSessionData()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Change""")
		self.pylToHtmlResult+=str(""" form""")
		self.pylToHtmlResult+=str(""" from""")
		self.pylToHtmlResult+=str(""" dictionary""")
		self.pylToHtmlResult+=str(""" type""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" session""")
		self.pylToHtmlResult+=str(""" data""")
		self.pylToHtmlResult+=str(""" type""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
							<li>""")
		self.pylToHtmlResult+=str("""sessionDataTodict()""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
							<p>""")
		self.pylToHtmlResult+=str("""Change""")
		self.pylToHtmlResult+=str(""" form""")
		self.pylToHtmlResult+=str(""" from""")
		self.pylToHtmlResult+=str(""" session""")
		self.pylToHtmlResult+=str(""" data""")
		self.pylToHtmlResult+=str(""" type""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" dictionary""")
		self.pylToHtmlResult+=str(""" type""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
						</ul>""")
		self.pylToHtmlResult+=str("""
					</div>""")
		self.pylToHtmlResult+=str("""
				</div>""")
		self.pylToHtmlResult+=str("""
				</div>""")
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
						<li data-theme="b">""")
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
		<!-- Finally, to actually run the highlighter, you need to include this JS on your page -->""")
		self.pylToHtmlResult+=str("""
		<script type="text/javascript">""")
		self.pylToHtmlResult+=str("""
		     SyntaxHighlighter.all()""")
		self.pylToHtmlResult+=str("""
		</script>""")
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
