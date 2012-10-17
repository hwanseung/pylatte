'''
Created on 2011. 7. 16.

@author: Hwanseung Lee(rucifer1217@gmail.com)
'''
import sys;
sys.path.append('./topy')    #Path to save uploaded files.
import os
import http.server
import Pylatte.WebServer.methodGetGetParam as methodGetGetParam      #To use GET parameter
import Pylatte.WebServer.methodGetPostParam as methodGetPostParam   #To use POST parameter
import Pylatte.WebServer.requestHeaderInfo as requestHeaderInfo   #To use request Header information in pyl files.
import Pylatte.WebServer.sessionUtil as sessionUtil
import imp

class latteServer(http.server.CGIHTTPRequestHandler):
    
    excuteDic=tuple()
    urlMappingDic=tuple()
    databaseInfo=tuple()
    server_version="pylatte Server v0.9.8.1"
    
    isPyl=False
    dynamicHtml=""
    pyFile=None;
    
    def __init__(self, request, client_address, server):

        #URL Mapping
        self.urlMap=server.urlMap

        #Database information
        self.databaseInfo=server.databaseInfo
        
        http.server.CGIHTTPRequestHandler.__init__(self, request, client_address, server)
            
        pass
    
    def log_message(self, format, *args):
        #로그 남기는게 외부에서 접속시 response Time을 잡아먹음.
        pass
    
    def do_GET(self):
        latteSession=""
        headerInfo=requestHeaderInfo.requestHeaderInfo(self)
        
        print("request url :" +self.path)

        #get GET parameters value.
        param=methodGetGetParam.methodGetGetParam(self.path)

        self.pyFile=None; #no file uploaded
        
        
        
        url = self.path.split('?')[0]
        try:
            self.path=self.urlMap[url]
            moduleName=self.path.split('.')[0]
            print("moduleName : "+moduleName)
            urlTest_pyl=moduleName+'_pyl'
            
            #Checking a cookie value to know whether session exists or not.
            print("Cookie : "+headerInfo.getHeaderInfo()["Cookie"])
            
            sessionutil =sessionUtil.session
            
            cookies=headerInfo.getHeaderInfo()["Cookie"].split(";");

            
            for item in cookies:
                cookie = item.split("=")
                if cookie[0]=="PYLATTESESSIONID":
                    #print (cookie[1])
                    latteSession=cookie[1]
            
            #if there is no cookie value, make a new cookie value.
            if latteSession=="":
                sessionKey = sessionutil.genSessionKey(sessionutil)
                
            #If there is a cookie value, get the value from head information and put into sessionKey variable.
            else: 
                sessionKey = latteSession
                
            print("session ID : "+sessionKey);
            
            try:
                sessionData = sessionutil.getSessionData(sessionutil,sessionKey)
            except IOError:
                sessionData =""
                
            sessionDic = sessionutil.sessionDataTodict(sessionutil,sessionData)
            
            #print(urlTest_pyl)
            folders = ['./topy']
            pyl = __import__(urlTest_pyl,fromlist=[folders])
            imp.reload(pyl)
            print("Got started to process dynamic Page")
            module=getattr(pyl, moduleName)(param.getParam(),self.pyFile,sessionDic,headerInfo.getHeaderInfo(),self.databaseInfo)
            #print("processing DynamicPage End")
            htmlcode = module.getHtml()    # completely generaged HTML
            #print(htmlcode)
            finalSessionDic=module.getSession()
            sessionData = sessionutil.dictToSessionData(sessionutil,finalSessionDic)
            
            sessionutil.setSessionData(sessionutil,sessionKey, sessionData)
            ##wf = open("temp.html","w")
            ##wf.write(htmlcode)
            ##wf.close()
            self.dynamicHtml = htmlcode;
            self.isPyl=True

        except KeyError:# If there is nothing to process dynamically, look for static thing
            print('Not Found pyl')
            self.isPyl=False
            sessionKey=None
            pass
        except TypeError:
            print('Error - Result of processing SQL is None. NoneType object is not subscriptable.')
            pass
        
        
        if(self.isPyl == True):
            #if session value is same
            try:
                if latteSession=="" and sessionKey!=None:
                    try:
                        self.send_head("PYLATTESESSIONID="+sessionKey+"; "+headerInfo.getHeaderInfo()["Cookie"])
                    except TypeError:
                        self.send_head("PYLATTESESSIONID="+sessionKey)
                else:
                    self.send_head(None)#send sessionid to header
            except IndexError:
                self.send_head(None)
                
            self.wfile.write(bytes(self.dynamicHtml, 'UTF-8'))
        else:
            f = self.send_head(None)
            
            if f:
                self.copyfile(f, self.wfile)
                f.close()
        print("\n")
        pass
       
    def do_POST(self):
        latteSession=""
        
        headerInfo=requestHeaderInfo.requestHeaderInfo(self)
        
        print(self.path)
        
        #print("Start of getting POST parameter")
        post_payload = self.rfile.read(int(headerInfo.getHeaderInfo()["Content-Length"]));
        print(post_payload)
        if post_payload.find(b'Content-Disposition: form-data')!=-1:
            print("multy-part upload");
            import Pylatte.WebServer.postMultipartForm as postMultipartForm
            param=postMultipartForm.postMultipartForm(post_payload)
            self.pyFile=param.getFileInfo()
            
        else:
            param=methodGetPostParam.methodGetPostParam(str(post_payload))
            self.pyFile=None;
        #print("End of getting POST parameter")
        
        
        
        url = self.path
        try:
            self.path=self.urlMap[url]
            moduleName=self.path.split('.')[0]
            print("moduleName : "+moduleName)
            urlTest_pyl=moduleName+'_pyl'
            
            
            #print(urlTest_pyl)
            folders = ['./topy']
            pyl = __import__(urlTest_pyl,fromlist=[folders])#import py files which is generated from pyl files.
            imp.reload(pyl)
            #Checking a cookie value to know whether session exists or not.
            print("Cookie:"+headerInfo.getHeaderInfo()["Cookie"])
            
            sessionutil =sessionUtil.session
            
            cookies=headerInfo.getHeaderInfo()["Cookie"].split(";");
    
            for item in cookies:
                cookie = item.split("=")
                if cookie[0]=="PYLATTESESSIONID":
                    #print (cookie[1])
                    latteSession=cookie[1]
            
            #if there is no cookie value, make a new cookie value.
            if latteSession=="":
                sessionKey = sessionutil.genSessionKey(sessionutil)
                
            #If there is a cookie value, get the value from head information and put into sessionKey variable.
            else: 
                sessionKey = latteSession
                
            print("session ID : "+sessionKey);
            
            try:
                sessionData = sessionutil.getSessionData(sessionutil, sessionKey)
            except IOError:
                sessionData =""
                
            sessionDic = sessionutil.sessionDataTodict(sessionutil,sessionData)
            
            print("processing Dynamic Page")
            module=getattr(pyl, moduleName)(param.getParam(),self.pyFile,sessionDic,headerInfo.getHeaderInfo(),self.databaseInfo)
            #print("processing Dynamic Page End")
            
            #세션유지시킬 값도 가져와야됨.
            
            htmlcode = module.getHtml()
            #print(htmlcode)
            finalSessionDic=module.getSession()
            sessionData = sessionutil.dictToSessionData(sessionutil,finalSessionDic)
            
            sessionutil.setSessionData(sessionutil,sessionKey, sessionData)
            ##wf = open("temp.html","w")
            ##wf.write(htmlcode)
            ##wf.close()
            self.dynamicHtml = htmlcode;
            self.isPyl=True

        except KeyError:# If there is nothing to process dynamically, look for static thing
            print('Not Found pyl')
            self.isPyl=False
            sessionKey=None
            pass
        except TypeError:
            print('Error - Result of processing SQL is None. NoneType object is not subscriptable.')
            pass
        
        
        if(self.isPyl == True):
            #if session value is same
            try:
                if latteSession=="" and sessionKey!=None:
                    try:
                        self.send_head("PYLATTESESSIONID="+sessionKey+"; "+headerInfo.getHeaderInfo()["Cookie"])
                    except TypeError:
                        self.send_head("PYLATTESESSIONID="+sessionKey)
                else:
                    self.send_head(None)#send sessionid to header
            except IndexError:
                self.send_head(None)
                
            self.wfile.write(bytes(self.dynamicHtml, 'UTF-8'))
        else:
            f = self.send_head(None)
            
            if f:
                self.copyfile(f, self.wfile)
                f.close()
                
        print("\n")
        pass
        
            
    def do_HEAD(self):
        http.server.CGIHTTPRequestHandler.do_HEAD(self)
        pass
    
    def send_head(self,sessionData=None):
        """Common code for GET and HEAD commands.

        This sends the response code and MIME headers.

        Return value is either a file object (which has to be copied
        to the outputfile by the caller unless the command was HEAD,
        and must be closed by the caller under all circumstances), or
        None, in which case the caller has nothing further to do.
        """
        
        
        if self.isPyl==True:
            self.send_response(200)
            self.send_header("Content-Length", len(self.dynamicHtml) )
            self.send_header("Last-Modified", self.date_time_string(200000))
            self.send_header("Content-type", "text/html" + "; charset=utf-8")
            if sessionData!=None:#if sessionKey exist, the key are used
                self.send_header("Set-Cookie", sessionData)
            self.end_headers()
            return
        else:
            path = self.translate_path(self.path)
            print("static file response: "+path)
            
            f = None
            if os.path.isdir(path):
                if not self.path.endswith('/'):
                    # redirect browser - doing basically what apache does
                    self.send_response(301)
                    self.send_header("Location", self.path + "/")
                    self.end_headers()
                    return None
                for index in "index.html", "index.htm":
                    index = os.path.join(path, index)
                    if os.path.exists(index):
                        path = index
                        break
                else:
                    return self.list_directory(path)
            ctype = self.guess_type(path)
            try:
                f = open(path, 'rb')
            except IOError:
                self.send_error(404, "File not found")
                return None
            self.send_response(200)
            if self.isPyl==True:
                self.send_header("Content-type", ctype + "; charset=utf-8")
            else:
                self.send_header("Content-type", ctype)
            fs = os.fstat(f.fileno())
            self.send_header("Content-Length", str(fs[6]))
            self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
            self.end_headers()
        return f
    
    
            
if __name__ == '__main__':
    str1 = "PYLATTESESSIONID=pylsession_2894c5183c66a4e92b21e3c6720fcf02; __utma=96992031.1636130766.1320671238.1320671238.1320671238.1; __utmb=96992031.4.10.1320671238; __utmc=96992031; __utmz=96992031.1320671238.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)"
    #str1 = "__utma=96992031.1901537661.1320667483.1320667483.1320667483.1; __utmb=96992031.7.10.1320667483; __utmc=96992031; __utmz=96992031.1320667483.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)"
    cookies=str1.split(";");
    
    latteSession=""
    for item in cookies:
        cookie = item.split("=")
        if cookie[0]=="PYLATTESESSIONID":
            print (cookie[1])
            latteSession=cookie[1]
    
    if latteSession=="":
        print("no")
    
  
    