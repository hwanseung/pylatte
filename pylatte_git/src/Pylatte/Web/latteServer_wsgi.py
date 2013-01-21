'''
Created on 2011. 7. 16.

@author: Hwanseung Lee(rucifer1217@gmail.com)
'''
import re
import imp
import os
import sys,os.path
from cgi import parse_qs, escape

import Pylatte.Web.requestHeaderInfo as requestHeaderInfo   #To use request Header information in pyl files.
import Pylatte.Web.sessionUtil as sessionUtil
import Pylatte.Web.pylToPy as pylToPy

def not_found(environ, start_response):
    """Called if no URL matches."""
    start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
    return ['Not Found']

def application(environ, start_response):
    
    headerInfo = requestHeaderInfo.requestHeaderInfo(environ).getHeaderInfo()
    param = parse_qs(environ.get('QUERY_STRING', ''))
    path = environ.get('PATH_INFO', '')
    print("GET method Parameters "+str(param))
    print("path : "+path)
    
    print("urlMap : "+str(environ["urlMap"]))
    print("filterMap : "+str(environ["filterMap"]))
    print("Cookie : "+headerInfo["HTTP_COOKIE"])
    
    try:
        pylPath=environ["urlMap"][path]
    except KeyError:
        """미리 xml로 명시한 동적 요청이 아닐 경우 여기로 들어오기 되어 있음.
        여기서 정적파일을 찾은 후 없으면  404 not found.
        """
        try:
            path = path.replace("..","")
            in_file = open(os.getcwd()+path,"rb")
            staticFile = in_file.read()
            in_file.close()
        except IOError:
            return not_found(environ, start_response)
        start_response('200 OK', [])
        return [staticFile]
        pass
        
    moduleName=pylPath.split('.')[0]
    print("moduleName : "+moduleName)
    urlTest_pyl=moduleName+'_pyl'
    print(urlTest_pyl)
    
    sessionutil =sessionUtil.session
    cookies=headerInfo["HTTP_COOKIE"].split(";");

    latteSession=""
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

    #---------------------make pyl to py
    
    print("make PYLtoPY-----------------------")
    print("path : "+path)
    
    a = environ["urlMap"]
    item = None
    if a.get(path)!=None:
        print(a.get(path))
        item = a.get(path)
    print(environ["urlMap"])
    
    print("urlMap : "+str(environ["urlMap"]))
    print("filterMap : "+str(environ["filterMap"]))
    

    print("make end PYLtoPY-----------------------")
    print("start to pylToPy")

    #Looking for filter to execute before pyl files executed.
    filterMap=environ["filterMap"]
    filterStr = ""
    for item1 in filterMap.keys():
        if item in filterMap[item1]:
            filterStr += open('pyl/'+item1, encoding='utf-8').read()+"\n"
    p=pylToPy.pylToPy(item,filterStr)
    p.outPy()
    print("end to pylToPy\n")

    #---------------------
    sys.path.append(os.path.join(os.getcwd(), 'topy'))
    print(sys.path)
    
    pyl = __import__(urlTest_pyl)
    imp.reload(pyl)
    print("Got started to process dynamic Page")
    pyFile=None;
    databaseInfo=tuple()
    
    module=getattr(pyl, moduleName)(param,pyFile,sessionDic,headerInfo,databaseInfo)
    print("processing DynamicPage End")
    htmlcode = module.getHtml()    # completely generaged HTML
    print(htmlcode)


    start_response('200 OK', [('Content-Type', 'text/html')])
    return [bytes(htmlcode,'utf-8')]
    
    
if __name__ == '__main__':
        
    from wsgiref.simple_server import make_server
    application = application
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()
