'''
Created on 2011. 7. 29.

@author: HwanSeung Lee(rucifer1217@gmail.com)

request Header information.
this information is wsgi environ value.
'''

import logging

class requestHeaderInfo:
    
    h_info=dict()
    def __init__(self,environ):
        
        logging.debug("REQUEST_METHOD :"+environ.get('REQUEST_METHOD'))
        logging.debug("SCRIPT_NAME :"+environ.get('SCRIPT_NAME'))
        logging.debug("PATH_INFO :"+environ.get('PATH_INFO'))
        logging.debug("QUERY_STRING :"+environ.get('QUERY_STRING'))
        logging.debug("CONTENT_TYPE :"+environ.get('CONTENT_TYPE'))
        logging.debug("CONTENT_LENGTH :"+environ.get('CONTENT_LENGTH'))
        logging.debug("SERVER_NAME :"+environ.get('SERVER_NAME'))
        logging.debug("SERVER_PORT :"+environ.get('SERVER_PORT'))
        logging.debug("SERVER_PROTOCOL :"+environ.get('SERVER_PROTOCOL'))
        logging.debug("SERVER_SOFTWARE :"+environ.get('SERVER_SOFTWARE'))
              
        logging.debug("HTTP_ACCEPT :"+environ.get('HTTP_ACCEPT'))
        logging.debug("HTTP_ACCEPT_ENCODING :"+environ.get('HTTP_ACCEPT_ENCODING'))
        logging.debug("HTTP_ACCEPT_LANGUAGE :"+environ.get('HTTP_ACCEPT_LANGUAGE'))
        logging.debug("HTTP_HOST :"+environ.get('HTTP_HOST'))
        logging.debug("HTTP_USER_AGENT :"+environ.get('HTTP_USER_AGENT'))
        logging.debug("HTTP_CONNECTION :"+environ.get('HTTP_CONNECTION'))
        
        logging.debug("REMOTE_ADDR :"+environ.get('REMOTE_ADDR'))
        logging.debug("REMOTE_HOST :"+environ.get('REMOTE_HOST'))
        
        #keys = environ.keys()
        #logging.debug(keys)
        
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
        
        if environ.__contains__("HTTP_COOKIE"):
            self.h_info["HTTP_COOKIE"] = environ.get('HTTP_COOKIE',"")
        else:
            self.h_info["HTTP_COOKIE"] = ""
           
        pass
    def getHeaderInfo(self):
        return self.h_info
        
        pass
