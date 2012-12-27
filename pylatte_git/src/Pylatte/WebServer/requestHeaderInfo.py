'''
Created on 2011. 7. 29.

@author: HwanSeung Lee(rucifer1217@gmail.com)

request Header information.
this information is wsgi environ value.
'''
class requestHeaderInfo:
    
    h_info=dict()
    def __init__(self,environ):
        
        print("REQUEST_METHOD :"+environ.get('REQUEST_METHOD'))
        print("SCRIPT_NAME :"+environ.get('SCRIPT_NAME'))
        print("PATH_INFO :"+environ.get('PATH_INFO'))
        print("QUERY_STRING :"+environ.get('QUERY_STRING'))
        print("CONTENT_TYPE :"+environ.get('CONTENT_TYPE'))
        print("CONTENT_LENGTH :"+environ.get('CONTENT_LENGTH'))
        print("SERVER_NAME :"+environ.get('SERVER_NAME'))
        print("SERVER_PORT :"+environ.get('SERVER_PORT'))
        print("SERVER_PROTOCOL :"+environ.get('SERVER_PROTOCOL'))
        print("SERVER_SOFTWARE :"+environ.get('SERVER_SOFTWARE'))
              
        print("HTTP_ACCEPT :"+environ.get('HTTP_ACCEPT'))
        print("HTTP_ACCEPT_ENCODING :"+environ.get('HTTP_ACCEPT_ENCODING'))
        print("HTTP_ACCEPT_LANGUAGE :"+environ.get('HTTP_ACCEPT_LANGUAGE'))
        print("HTTP_HOST :"+environ.get('HTTP_HOST'))
        print("HTTP_USER_AGENT :"+environ.get('HTTP_USER_AGENT'))
        print("HTTP_CONNECTION :"+environ.get('HTTP_CONNECTION'))
        
        print("REMOTE_ADDR :"+environ.get('REMOTE_ADDR'))
        print("REMOTE_HOST :"+environ.get('REMOTE_HOST'))
        
        #keys = environ.keys()
        #print(keys)
        
        self.h_info["REQUEST_METHOD"]=environ.get('REQUEST_METHOD', "")
        self.h_info["SCRIPT_NAME"]=environ.get('SCRIPT_NAME', "")
        self.h_info["PATH_INFO"]=environ.get('PATH_INFO', "")
        self.h_info["QUERY_STRING"]=environ.get('QUERY_STRING', "")
        self.h_info["CONTENT_TYPE"]=environ.get('CONTENT_TYPE', "")
        self.h_info["CONTENT_LENGTH"]=environ.get('CONTENT_LENGTH', "")
        
        self.h_info["SERVER_NAME"]=environ.get('SERVER_NAME', "")
        self.h_info["SERVER_PORT"]=environ.get('SERVER_PORT', "")
        self.h_info["SERVER_PROTOCOL"]=environ.get('SERVER_PROTOCOL', "")
        self.h_info["SERVER_SOFTWARE"]=environ.get('SERVER_SOFTWARE', "")
        
        self.h_info["HTTP_ACCEPT"]=environ.get('HTTP_ACCEPT', "")
        self.h_info["HTTP_ACCEPT_ENCODING"]=environ.get('HTTP_ACCEPT_ENCODING', "")
        self.h_info["HTTP_ACCEPT_LANGUAGE"]=environ.get('HTTP_ACCEPT_LANGUAGE', "")
        self.h_info["HTTP_HOST"]=environ.get('HTTP_HOST', "")
        self.h_info["HTTP_USER_AGENT"]=environ.get('HTTP_USER_AGENT', "")
        self.h_info["HTTP_CONNECTION"]=environ.get('HTTP_CONNECTION', "")

        self.h_info["REMOTE_ADDR"]=environ.get('REMOTE_ADDR', "")
        self.h_info["REMOTE_HOST"]=environ.get('REMOTE_HOST', "")
           
        pass
    def getHeaderInfo(self):
        return self.h_info
        
        pass
