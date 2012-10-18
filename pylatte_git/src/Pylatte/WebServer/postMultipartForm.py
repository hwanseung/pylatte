'''
Created on 2011. 7. 24.

@author: HwanSeung Lee(rucifer1217@gmail.com)
'''
class postMultipartForm:
    """
    This class is used to send multipart/form
    """
    
    pyload=b''
    delimiter= b''
    splited=b''
    param=dict()
    formFile=dict()
    def __init__(self,pyload):
        """
        Save payload datas in the start
        """
        self.pyload=pyload
        self.__splitPayload()
        self.__analysisData()
        pass
    
    def __splitPayload(self):
        """
        Split received datas
        """
        print(self.pyload)
        self.delimiter=self.pyload.split(b'\r\n')
        
        print(self.delimiter)
        
        self.splited= self.pyload.split(self.delimiter[0])
        self.splited.pop(0)# 스플릿하고 남는거 제거
        pass
    
    def __analysisData(self):
        """
        Analysis splited datas and the others become 'param'.
        """
        for item in self.splited:
            print("------------------")
            splited_item = item.split(b"\r\n");
            #for item1 in splited_item:
                #print("######")
                #print(item1)
            
            if splited_item[0]==b'--':
                #데이터의 종료를 의미한다.
                break;
            else:
                #파일이 아니라 일반적인 type="text"이거나 type="hidden" 일경우
               
                if splited_item[1].find(b'filename=')==-1:
                    namePosition=splited_item[1].find(b'; name="')
                    #print(namePosition)
                    nameValueStartP = splited_item[1].find(b'\"',namePosition)+1; #name attribute 값의 시작위치
                    nameValueEndP = splited_item[1].find(b'\"',namePosition+8); #name attribute 값의 종료위치
                    nameValue= splited_item[1][nameValueStartP:nameValueEndP] #name attribute Value
                    #print(b'name='+nameValue)
                    #print(splited_item[3])
                    self.param[str(nameValue,'UTF-8')]=str(splited_item[3],'UTF-8')
                    print(self.param)
                    print("This is not a file")
                    pass
                #form에 파일이 올라왔을 경우
                else:
                    fileInfo=dict()
                    namePosition=splited_item[1].find(b'; name=')
                    #print(namePosition)
                    nameValueStartP = splited_item[1].find(b'\"',namePosition)+1; #name attribute 값의 시작위치
                    nameValueEndP = splited_item[1].find(b'\"',namePosition+8); #name attribute 값의 종료위치
                    nameValue= splited_item[1][nameValueStartP:nameValueEndP] #name attribute Value
                    print(b'name='+nameValue)
                    
                    filenamePosition=splited_item[1].find(b'; filename=')
                    #print(filenamePosition)
                    filenameValueStartP = splited_item[1].find(b'\"',filenamePosition)+1; #name attribute 값의 시작위치
                    filenameValueEndP = splited_item[1].find(b'\"',filenamePosition+12); #name attribute 값의 종료위치
                    filenameValue= splited_item[1][filenameValueStartP:filenameValueEndP] #name attribute Value
                    
                    print(b'filename='+filenameValue)
                   
                    print(splited_item[4])
                    
                    import os
                    if os.path.exists("/tmp/pylatte_tmp/"):
                        print("Already exist")
                    else:
                        print("Not exist")
                        os.mkdir("/tmp/pylatte_tmp/")
                    
                    #Temporary file name.
                    tmpFileName=self.__getTmpHashKey(str(filenameValue))+".pylTemp"
                    with open("/tmp/pylatte_tmp/"+tmpFileName, mode='wb') as tmp_file:
                        tmp_file.write(splited_item[4]);
                    
                    fileInfo["realFileName"]=str(filenameValue,'UTF-8')
                    fileInfo["tmpFileName"]=tmpFileName
                    fileInfo["size"]= splited_item[4].__len__()
                    self.formFile[str(nameValue,'UTF-8')]=fileInfo
                    
                    print(self.formFile)
                    pass
                
                pass
                    
        pass
    
    def __getTmpHashKey(self,fileName):
        """
        Make a temporary file name.
        """
        import hashlib
        import time
        
        timestamp = int(time.time())
        timestr = str(timestamp)
        
        return 'pyltmp_' + hashlib.md5(b'pyl'+str.encode(fileName)+ str.encode(timestr) ).hexdigest()
        pass
    
    def getFileInfo(self):
        """
        Return file information.
        """
        return self.formFile
        pass
    
    def getParam(self):
        """
        Retrun input data except for file information
        """
        return self.param
        pass
    pass

if __name__ == '__main__':
    input1 = b'-----------------------------765669583386782207550639134\r\nContent-Disposition: form-data; name="file1"; filename="secmem.main.logo.gif"\r\nContent-Type: image/gif\r\n\r\nGIF89a\xac\x00\x12\x00\xc4\x00\x00\xca\xca\xc9\xe4\xe4\xe2\xb1\xb1\xb1opq\x98\x99\x99\xd2\xd2\xd1wxyfgi\x90\x91\x91\xdb\xdb\xd9\xb9\xba\xb9\xa9\xa9\xa9\xe6\xe6\xe4\x88\x88\x89\xe7\xe7\xe5\xc2\xc2\xc1\xa1\xa1\xa1\x7f\x80\x81\xe5\xe5\xe3\x92\x94\x97\xbb\xbd\xbf\xed\x1c$^_a\xe3\xe3\xe1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00!\xf9\x04\x00\x00\x00\x00\x00,\x00\x00\x00\x00\xac\x00\x12\x00\x00\x05\xff\xe0%\x8edi\x9eh\xaa\xael\xeb\xbep,\x8b\x81d\xdf8\x1e\xd4yo\xef\xba\xe0-0+\x1a\x8f\xc8\x99d\xc2l:\x9d\xb6\x8atJ\xa5\xda(X\n#\xab\xe5JR\x02HA$\x88\x00F\x05\xc8cD\x88\x94\x1ej\x13\xe0A\xaf?\x12\xa3\xb9\xfd1\x1e)\x04cp\n\x11\x02yg"\x00\x84\tv\x00i\x0fm\x17\x05w\x91\x93\x90#\x10\x85df$KO\x9eLQU\xa2RWY\x0e\\\xa7Y_(\x11\x16k\x17\x10\xae#\x0f\x16\x10#\xad%\xb1\xb6%\xad\x16\xbe\xbf\xaf\x17\xbd\xbf\xb5"\t\x06\xbe\x07p\xb5\xc5\x00\x03\xbe\x03g\xb4j\xc4\x11\xd3\xb8\xb1k\xd9\xc2\x16$\x16\x03\x97\xb2#\x9d\x9fO\xa1\xa3U\xa5X\xa9\xeb^)\xc8\xaf\xdb"\x0b\x16\x08i\x10\xcf%\x04\x16\x06r\xf4\x08\x0f\xe0\xe1\x11\xd1jO\x9f}\x0b\x14\x1c\x18\xa0\xab\xd83\x02\xfb\xc0M\xa3\x05\xd0\x82\xb5Z\xd8dm\xc3\x85\xc8W\xb8`\x17\xc8\x95kr\x0e\xdd\x14u\x14\xd8\xff\xa5tw\xa2\x80/\x04"by\xbc\x80\xe0\x1b\xad_$\x00\x1c\xf0\x05R\xc44n\xbc,F\x18\xba\t(\xb7\x86\xd4`^\xd8g\x00\x195[\xc4 d\x8c\x8a\xaf[L_\n\xae\x82\x0c\xc0\xc0\x81\xd7\xaf`\xbd2\xd8\xd15\xac\xd9\xb1\x12P\xa9U\xc5*\xd9\x99X\x08l\x01\xf8\xb5\x80\xa0\xd5\x0b\x02vB8p`\xc1@\x9f\xc58\xde\x12J\xf4\x10\xbd\x06\xfb" \xfd\t\x8b\x9f\xd3\x9f\xdfjJ\xed\x06w\xf2\xb0\x8e;\x0f\xbc\x15\'B\xe4\xc8\t%MV@\xa9R\xe5*\x12\tZ!\xd0y \x8c,\x9d\x16\x14\x06\xb6\xdaj@\xd6D\xdf\x06\x0e\x8b:8\xc5>\x8bi\x98AH\xf0\xad@\x81g\x92j\xd1\x1a\xd0\xea\xe2\xe4\xc6\xda,\x08\x08\xd8\x8d\x9ef\x01\x16\x94\xc9\xeb\xfc\x19\x8a\x04\xd1V\xd2\x9aZ\x8b\xe5\xf4\x08\xec\x04\x10\xd9\xce\xe6\xf2@\xd6\x02MS[\x05P\xe8\xa7\x82\xacd \xe8\xdf\x1f\xc7.1\x8b\x17$2\x94\x01\x11\x10(\x1c^\xc4\xd4\xa7\\\xff5\xd7Pf\xc1\x02\x0f\xd4\xb4\x06.\x0b\x18p\x08\x000m\x17Rw$}\x07\x1e)\xe2\xb53\x1e[r\x98P\xc6\x19\n\xf4\x11\xe0\x02\xb8\xbdQL\x0ca\xf0\x87I\x80C\xed\x14\x01\x01\x92\xbd\x08G\x7f\x8c\xe5D\x08$2\x01c\x94O\x87\\\xa0\xc0p\x9cp\x08\x8a\x87\x1f\x92F\x1e\x05\xe6\xe9CTa%\xd4\xe4\x8b\x1b\xb0\xecW\x93b\xfb\r2\xe5\x97\x04\xc4(\xe3~\xaf\xb4R\xc63\xba\xa0\xd0\xa3\x80S\xa6\'\x89\x1dx\x08v\x01?u S\x02Wf\x9dEV\x9ea\xa1\xf5\xa4i)47\xd43 a\x07PMu\xfd\xa7\xe8\x02_\x82\xb9\x9b\xa2\xbb\x144Y\x9a\'\xf4\xb8\x1cQ\x00\xb6\xe5\x8d\xa2%x6Rh&99by\x81\xde\xa5\xe1>k\xd0\xd2@\x12.X\x82\x94\x9a/^\xd0c\xa6\'\xc8I\'\x1dv&\xa9$\xa8\xe8\x88*"\xa9m\x11E(\t\xff\xd0\xf4 \xab3,\xa2b\t\xca\xce\xf2\r\xa6X\x9e0\x877\x07\x10\xb5SN\xa7J\x82\xc6$x\xbe\xaeD\xe2\tm|Y\xe4\x05\xc7\xfcb\xc0_\xc8\xa6[\x02\x9bD\xa5\xe7B\xa3\xd1r\xb7\xeb\xb6\xa2\xa1\xb4E\x16\xf7\x02k\xc4\x91\xf8\xa9\xeb\xef\xbf)\xf0\xe0C\x0e@\x0cL\xb0\xc0\x12 \xac0\xc0\x0c7\xec\xf0\xc3\x10G,\xf1\x0c!\x00\x00;\r\n-----------------------------765669583386782207550639134\r\nContent-Disposition: form-data; name="file2"; filename="text 1.txt"\r\nContent-Type: text/plain\r\n\r\nhello1\n\r\n-----------------------------765669583386782207550639134\r\nContent-Disposition: form-data; name="file3"; filename="text 3.txt"\r\nContent-Type: text/plain\r\n\r\nhello3\n\r\n-----------------------------765669583386782207550639134\r\nContent-Disposition: form-data; name="text1"\r\n\r\nttt\r\n-----------------------------765669583386782207550639134\r\nContent-Disposition: form-data; name="hidden1"\r\n\r\n\r\n-----------------------------765669583386782207550639134--\r\n'
                        
    p=postMultipartForm(input1)
   
   
