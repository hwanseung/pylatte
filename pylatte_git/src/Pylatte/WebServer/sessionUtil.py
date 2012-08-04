'''
Created on 2011. 6. 4.

@author: Heegeun Park(sirini@gmail.com)
@modifier : HwanSeung Lee(rucifer1217@gmail.com)
'''

class session:
    # After limit (default = 900 sec), the session becomes unvalid.
    def checkAvailableSession(self, key, limit=900):
        
        import os.path
        import time
        
        if os.path.isfile('session/' + key) != True:
            return False
        
        if int(os.path.getmtime('session/' + key)) + limit < int(time.time()):
            os.remove('session/' + key)
            return False
        else:
            return True 
    
    
    # Generate session file @Heegeun Park
    # To put cookie in client, set the value like Set-Cookie: PYLSESSION=pylsession_rjdidkoawe3il2q39njklszdfjoi ... in HTTP header
    def genSessionKey(self):
        
        import hashlib
        import time
        
        timestamp = int(time.time())
        timestr = str(timestamp)
        
        return 'pylsession_' + hashlib.md5(b'pylatte' + str.encode(timestr) ).hexdigest()
    
    # Save file using generated key string @Heegeun Park
    # It is possible to write in a selected file.
    def setSessionData(self, key, content=None):
        
        import os
        if os.path.isdir("session") == False:
            os.mkdir("session")
        
        f = open('session/' + key, mode='w', encoding='utf-8')
        if content != None:
            f.write(content)
        f.close()
        pass
    
    # Get session data using the session key.  @Hwanseung Lee
    def getSessionData(self,key):
        import os
        if os.path.isdir("session") == False:
            os.mkdir("session")
            
        f = open('session/' + key, mode='r', encoding='utf-8')
        content=f.read();
        print (content)
        
        return content    
        
    # Change form from dictionary type to session data type @Hwanseung Lee
    def dictToSessionData(self,dicData):
        dataStr = "";
        for item in dicData.keys():
            dataStr+=item+":"+dicData[item]+"/"
        
        return dataStr
        pass
    
        # Change form from session data type to dictionary type @Hwanseung Lee
    def sessionDataTodict(self,data):
        splitedData=data.split('/')
        resultDic = dict();
        
        try:
            for item in splitedData:
                resultDic[item.split(':')[0]]=item.split(':')[1]
        
        except IndexError:#indexError를 받으면 그냥 넘기도록 설정
            pass
            
        return resultDic
        pass
            
if __name__ == '__main__':
    str1 = "key:value/key1:value1/key2:value2/"
    result = session.sessionDataTodict(session,str1)
    print (result)
    
    resultStr = session.dictToSessionData(session, result)
    print (resultStr)
    
    
