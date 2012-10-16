# -*- coding: utf-8 -*- 
import Pylatte.WebServer.formFile as formFile
class faq:
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

	<script type="text/javascript">""")
		self.pylToHtmlResult+=str("""
		function""")
		self.pylToHtmlResult+=str(""" submitForm()""")
		self.pylToHtmlResult+=str(""" {""")
		self.pylToHtmlResult+=str("""
			alert(&quot;232&quot;);""")
		self.pylToHtmlResult+=str("""
		 	$(&quot;#fileForm&quot;).submit();""")
		self.pylToHtmlResult+=str("""
		}""")
		self.pylToHtmlResult+=str("""
	</script>""")
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
		self.pylToHtmlResult+=str("""Frequently""")
		self.pylToHtmlResult+=str(""" Asked""")
		self.pylToHtmlResult+=str(""" Questions""")
		self.pylToHtmlResult+=str("""</h1>""")
		self.pylToHtmlResult+=str("""
				<h2>""")
		self.pylToHtmlResult+=str("""General""")
		self.pylToHtmlResult+=str("""</h2>""")
		self.pylToHtmlResult+=str("""
				<ul>""")
		self.pylToHtmlResult+=str("""
					<li>""")
		self.pylToHtmlResult+=str("""Why""")
		self.pylToHtmlResult+=str(""" did""")
		self.pylToHtmlResult+=str(""" you""")
		self.pylToHtmlResult+=str(""" guys""")
		self.pylToHtmlResult+=str(""" decied""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" make""")
		self.pylToHtmlResult+=str(""" python3-based""")
		self.pylToHtmlResult+=str(""" web""")
		self.pylToHtmlResult+=str(""" framework?""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
					<p>""")
		self.pylToHtmlResult+=str("""One""")
		self.pylToHtmlResult+=str(""" day""")
		self.pylToHtmlResult+=str(""" we""")
		self.pylToHtmlResult+=str(""" read""")
		self.pylToHtmlResult+=str(""" Linux""")
		self.pylToHtmlResult+=str(""" Journal""")
		self.pylToHtmlResult+=str(""" Dec.""")
		self.pylToHtmlResult+=str(""" 2010""")
		self.pylToHtmlResult+=str(""" issue.""")
		self.pylToHtmlResult+=str(""" Then""")
		self.pylToHtmlResult+=str(""" we""")
		self.pylToHtmlResult+=str(""" found""")
		self.pylToHtmlResult+=str(""" out""")
		self.pylToHtmlResult+=str(""" there""")
		self.pylToHtmlResult+=str(""" are""")
		self.pylToHtmlResult+=str(""" an""")
		self.pylToHtmlResult+=str(""" interesting""")
		self.pylToHtmlResult+=str(""" article.""")
		self.pylToHtmlResult+=str(""" The""")
		self.pylToHtmlResult+=str(""" article""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" about""")
		self.pylToHtmlResult+=str(""" programming""")
		self.pylToHtmlResult+=str(""" languages""")
		self.pylToHtmlResult+=str(""" on""")
		self.pylToHtmlResult+=str(""" top""")
		self.pylToHtmlResult+=str(""" 10.""")
		self.pylToHtmlResult+=str(""" Actually,""")
		self.pylToHtmlResult+=str(""" python""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" not""")
		self.pylToHtmlResult+=str(""" a""")
		self.pylToHtmlResult+=str(""" popular""")
		self.pylToHtmlResult+=str(""" language""")
		self.pylToHtmlResult+=str(""" in""")
		self.pylToHtmlResult+=str(""" Korea,""")
		self.pylToHtmlResult+=str(""" but""")
		self.pylToHtmlResult+=str(""" python""")
		self.pylToHtmlResult+=str(""" was""")
		self.pylToHtmlResult+=str(""" best""")
		self.pylToHtmlResult+=str(""" on""")
		self.pylToHtmlResult+=str(""" the""")
		self.pylToHtmlResult+=str(""" rank.""")
		self.pylToHtmlResult+=str(""" so""")
		self.pylToHtmlResult+=str(""" we""")
		self.pylToHtmlResult+=str(""" wander""")
		self.pylToHtmlResult+=str(""" why""")
		self.pylToHtmlResult+=str(""" python""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" popular""")
		self.pylToHtmlResult+=str(""" in""")
		self.pylToHtmlResult+=str(""" the""")
		self.pylToHtmlResult+=str(""" world.""")
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
					<p>""")
		self.pylToHtmlResult+=str("""In""")
		self.pylToHtmlResult+=str(""" this""")
		self.pylToHtmlResult+=str(""" reason,""")
		self.pylToHtmlResult+=str(""" we""")
		self.pylToHtmlResult+=str(""" decieded""")
		self.pylToHtmlResult+=str(""" to""")
		self.pylToHtmlResult+=str(""" study""")
		self.pylToHtmlResult+=str(""" the""")
		self.pylToHtmlResult+=str(""" newest""")
		self.pylToHtmlResult+=str(""" python,""")
		self.pylToHtmlResult+=str(""" python3.""")
		self.pylToHtmlResult+=str(""" whild""")
		self.pylToHtmlResult+=str(""" we're""")
		self.pylToHtmlResult+=str(""" studying""")
		self.pylToHtmlResult+=str(""" it,""")
		self.pylToHtmlResult+=str(""" we""")
		self.pylToHtmlResult+=str(""" realized""")
		self.pylToHtmlResult+=str(""" there""")
		self.pylToHtmlResult+=str(""" is""")
		self.pylToHtmlResult+=str(""" no""")
		self.pylToHtmlResult+=str(""" web""")
		self.pylToHtmlResult+=str(""" framework""")
		self.pylToHtmlResult+=str(""" based""")
		self.pylToHtmlResult+=str(""" on""")
		self.pylToHtmlResult+=str(""" only""")
		self.pylToHtmlResult+=str(""" python3""")
		self.pylToHtmlResult+=str(""" (without""")
		self.pylToHtmlResult+=str(""" 2to3).""")
		self.pylToHtmlResult+=str(""" Finally,""")
		self.pylToHtmlResult+=str(""" we""")
		self.pylToHtmlResult+=str(""" are""")
		self.pylToHtmlResult+=str(""" developing""")
		self.pylToHtmlResult+=str(""" Pylatte""")
		self.pylToHtmlResult+=str(""" as""")
		self.pylToHtmlResult+=str(""" a""")
		self.pylToHtmlResult+=str(""" open""")
		self.pylToHtmlResult+=str(""" source""")
		self.pylToHtmlResult+=str(""" project.""")
		self.pylToHtmlResult+=str(""" 
				</ul>""")
		self.pylToHtmlResult+=str("""
	
				<h2>""")
		self.pylToHtmlResult+=str("""Using""")
		self.pylToHtmlResult+=str(""" Pylatte""")
		self.pylToHtmlResult+=str("""</h2>""")
		self.pylToHtmlResult+=str("""
				<ul>""")
		self.pylToHtmlResult+=str("""
					<li>""")
		self.pylToHtmlResult+=str("""Not""")
		self.pylToHtmlResult+=str(""" frequently""")
		self.pylToHtmlResult+=str(""" asked""")
		self.pylToHtmlResult+=str(""" yet.""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
				</ul>""")
		self.pylToHtmlResult+=str("""
				
				<h2>""")
		self.pylToHtmlResult+=str("""Developing""")
		self.pylToHtmlResult+=str(""" Pylatte""")
		self.pylToHtmlResult+=str("""</h2>""")
		self.pylToHtmlResult+=str("""
				<ul>""")
		self.pylToHtmlResult+=str("""
					<li>""")
		self.pylToHtmlResult+=str("""Not""")
		self.pylToHtmlResult+=str(""" frequently""")
		self.pylToHtmlResult+=str(""" asked""")
		self.pylToHtmlResult+=str(""" yet.""")
		self.pylToHtmlResult+=str("""</li>""")
		self.pylToHtmlResult+=str("""
				</ul>""")
		self.pylToHtmlResult+=str("""
				
				<h2>""")
		self.pylToHtmlResult+=str("""GET/POST""")
		self.pylToHtmlResult+=str(""" Test""")
		self.pylToHtmlResult+=str("""</h2>""")
		self.pylToHtmlResult+=str("""
				<form name="form" method="post" action="../faq">""")
		self.pylToHtmlResult+=str("""
					<p>""")
		self.pylToHtmlResult+=str("""
						<input type="text" name="name">""")
		self.pylToHtmlResult+=str("""
						<input type="submit" value="CLICK">""")
		self.pylToHtmlResult+=str("""
					</p>""")
		self.pylToHtmlResult+=str("""
				</form>""")

		if param=={}:
			pass	
		else:
			session['name']=param['name']
			self.pylToHtmlResult+=str("""
	<p>""")
			self.pylToHtmlResult+=str("""Get""")
			self.pylToHtmlResult+=str(""" or""")
			self.pylToHtmlResult+=str(""" Post""")
			self.pylToHtmlResult+=str(""" :""")
			self.pylToHtmlResult+=str( param['name'])
			self.pylToHtmlResult+=str("""</p>""")

		

		if session=={}:
			pass	
		else:
			self.pylToHtmlResult+=str("""
	<p>""")
			self.pylToHtmlResult+=str("""Session""")
			self.pylToHtmlResult+=str(""" :""")
			self.pylToHtmlResult+=str( session['name'])
			self.pylToHtmlResult+=str("""</p>""")

			pass
		self.pylToHtmlResult+=str("""
	<h3>""")
		self.pylToHtmlResult+=str("""HeaderInfo['path']""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""
	<p>""")
		self.pylToHtmlResult+=str(headerInfo['path'])
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
	<h3>""")
		self.pylToHtmlResult+=str("""HeaderInfo['Accept']""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""
	<p>""")
		self.pylToHtmlResult+=str(headerInfo['Accept'])
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
	<h3>""")
		self.pylToHtmlResult+=str("""HeaderInfo['Accept-Charset']""")
		self.pylToHtmlResult+=str("""</h3>""")
		self.pylToHtmlResult+=str("""
	<p>""")
		self.pylToHtmlResult+=str(headerInfo['Accept-Charset'])
		self.pylToHtmlResult+=str("""</p>""")
		self.pylToHtmlResult+=str("""
	<div>""")
		self.pylToHtmlResult+=str("""
		<form id="fileForm" data-ajax="false" class="ui-body ui-body-a ui-corner-all" method="post" enctype="multipart/form-data" action="http://127.0.0.1:8000/faviconUpload">""")
		self.pylToHtmlResult+=str("""
			<input type="file" name="file1"/>""")
		self.pylToHtmlResult+=str("""
			<button type="submit" data-theme="b" name="submit" value="submit-value">""")
		self.pylToHtmlResult+=str("""Submit""")
		self.pylToHtmlResult+=str("""</button>""")
		self.pylToHtmlResult+=str("""
		</form>""")
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
								<li data-theme="b">""")
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
</html>""")
		self.sessionDic=session
		pass
	def getHtml(self):
		return self.pylToHtmlResult
		pass
	def getSession(self):
		return self.sessionDic
		pass
