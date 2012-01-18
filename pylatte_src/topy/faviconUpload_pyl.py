# -*- coding: utf-8 -*- 
import formFile
class faviconUpload:
	result=""
	sessionDic=dict()
	def __init__(self,param,pyFile,session,headerInfo,lattedb):
		self.generate(param,pyFile,session,headerInfo,lattedb)

	def generate(self,param,pyFile,session,headerInfo,lattedb):

		pyformFile=formFile.formFile(pyFile)
		pyformFile.moveUploadFile("file1","pyl","favicon.ico")
		
		self.result+=str("""
		
		 """)
		self.result+=str("""<script type="text/javascript">
			alert("upload success!!");
			history.back();
		 """)
		self.result+=str("""</script> """)
		self.sessionDic=session
		pass
	def getHtml(self):
		return self.result
		pass
	def getSession(self):
		return self.sessionDic
		pass
