'''
Created on 2011. 10. 7.

@author: HwanSeung Lee(rucifer1217@gmail.com)
'''

import shutil

class formFile:
    
    error=""
    formFile=dict()
    def __init__(self,formFile):
        self.formFile=formFile
        pass
        
    def moveUploadFile(self,name,dir,fileName):
        """
        name : name of input tag in HTML
        dir : path to save a file. it must exist. if not, an error occurs
        fileName : file name to save
        
        return 0 when sucessed
        return -1 when failed
        
        """
        print(name)
        print(self.formFile)
        print(self.formFile[name])
        print("/tmp/pylatte_tmp/"+self.formFile[name]["tmpFileName"])
        shutil.move("/tmp/pylatte_tmp/"+self.formFile[name]["tmpFileName"],dir+"/"+fileName)
        
        
        self.error="success"
        return 0
        pass
    
    def getError(self):
        return self.error
        pass
    
    pass

