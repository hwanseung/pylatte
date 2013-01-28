'''
Created on 2011. 10. 7.

@author: HwanSeung Lee(rucifer1217@gmail.com)
'''
import os
import logging
class formFile:
    error=""
    def moveUploadFile(self,fieldStorage,dir,fileName):
        """
        fieldStorage : fieldStorage
        dir : path to save a file. it must exist. if not, an error occurs
        fileName : file name to save
        
        return 0 when sucessed
        return -1 when failed
        
        """
        
        #pyFile.filename
        logging.info(fieldStorage)
        logging.info(fieldStorage.name)
        logging.info(fieldStorage.filename)
        logging.info(fieldStorage.bytes_read)
        #logging.info(fieldStorage.file)
        #logging.info(fieldStorage.file.read())
        f = open(dir+"/"+fileName, 'wb')
        f.write(fieldStorage.file.read())
        f.close()
        
        self.error="success"
        return 0
        pass
    
    def getError(self):
        return self.error
        pass
    
    pass

