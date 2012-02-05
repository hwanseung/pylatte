# -*- coding: utf-8 -*- 
import formFile
class faviconUpload:
	pylToHtmlResult=""
	sessionDic=dict()
	def __init__(self,param,pyFile,session,headerInfo,lattedb):
		self.generate(param,pyFile,session,headerInfo,lattedb)

	def generate(self,param,pyFile,session,headerInfo,lattedb):
		self.pylToHtmlResult+=str("pylatte")
		self.pylToHtmlResult+=str("""

<script type="text/javascript">""")
		self.pylToHtmlResult+=str("""
	alert(&quot;upload""")
		self.pylToHtmlResult+=str(""" success!!&quot;);""")
		self.pylToHtmlResult+=str("""
	history.back();""")
		self.pylToHtmlResult+=str("""
</script>""")
		self.sessionDic=session
		pass
	def getHtml(self):
		return self.pylToHtmlResult
		pass
	def getSession(self):
		return self.sessionDic
		pass
