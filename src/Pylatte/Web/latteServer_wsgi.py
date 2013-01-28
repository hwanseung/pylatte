'''
Created on 2011. 7. 16.

@author: Hwanseung Lee(rucifer1217@gmail.com)
'''
import re
import imp
import os
import sys,os.path
import logging
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
    if headerInfo["REQUEST_METHOD"] == "GET":
        param = dict( (k, v if len(v)>1 else v[0] ) for k, v in parse_qs(environ.get('QUERY_STRING', '')).items() )
    elif headerInfo["REQUEST_METHOD"] == "POST":
        try:
            length= int(environ.get('CONTENT_LENGTH', '0'))
        except ValueError:
            length= 0
        if length!=0:
            param = dict( (k, v if len(v)>1 else v[0] ) for k, v in parse_qs(environ['wsgi.input'].read(length).decode(),True).items() )
        else:
                param = dict()
    else:
        param = dict()
    path = environ.get('PATH_INFO', '')
    
    logging.debug("GET method Parameters "+str(param))
    logging.debug("path : "+path)
    
    logging.debug("urlMap : "+str(environ["urlMap"]))
    logging.debug("filterMap : "+str(environ["filterMap"]))
    logging.debug("Cookie : "+headerInfo["HTTP_COOKIE"])
    
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
    logging.debug("moduleName : "+moduleName)
    urlTest_pyl=moduleName+'_pyl'
    logging.debug(urlTest_pyl)
    
    sessionutil =sessionUtil.session
    cookies=headerInfo["HTTP_COOKIE"].split(";");

    latteSession=""
    for item in cookies:
        cookie = item.split("=")
        if cookie[0]=="PYLATTESESSIONID":
            #logging.debug (cookie[1])
            latteSession=cookie[1]
    
    #if there is no cookie value, make a new cookie value.
    if latteSession=="":
        sessionKey = sessionutil.genSessionKey(sessionutil)
    #If there is a cookie value, get the value from head information and put into sessionKey variable.
    else: 
        sessionKey = latteSession
    logging.debug("session ID : "+sessionKey);
    
    try:
        sessionData = sessionutil.getSessionData(sessionutil,sessionKey)
    except IOError:
        sessionData =""
        
    sessionDic = sessionutil.sessionDataTodict(sessionutil,sessionData)

    #---------------------make pyl to py
    
    logging.debug("make PYLtoPY-----------------------")
    logging.debug("path : "+path)
    
    a = environ["urlMap"]
    item = None
    if a.get(path)!=None:
        logging.debug(a.get(path))
        item = a.get(path)
    
    logging.debug(environ["urlMap"])
    
    logging.debug("urlMap : "+str(environ["urlMap"]))
    logging.debug("filterMap : "+str(environ["filterMap"]))
    

    logging.debug("make end PYLtoPY-----------------------")
    logging.debug("start to pylToPy")
    
    #Looking for filter to execute before pyl files executed.
    filterMap=environ["filterMap"]
    filterStr = ""
    for item1 in filterMap.keys():
        if item in filterMap[item1]:
            filterStr += open('pyl/'+item1, encoding='utf-8').read()+"\n"
    p=pylToPy.pylToPy(item,filterStr)
    p.outPy()
    logging.debug("end to pylToPy\n")

    #---------------------
    sys.path.append(os.path.join(os.getcwd(), 'topy'))
    logging.debug(sys.path)
    
    pyl = __import__(urlTest_pyl)
    imp.reload(pyl)
    logging.debug("Got started to process dynamic Page")
    pyFile=dict()
    databaseInfo=tuple()
    logging.info("param : "+str(param))
    module=getattr(pyl, moduleName)(param,pyFile,sessionDic,headerInfo,databaseInfo)
    logging.debug("processing DynamicPage End")
    htmlcode = module.getHtml()    # completely generaged HTML
    #logging.debug(htmlcode)


    start_response('200 OK', [('Content-Type', 'text/html')])
    return [bytes(htmlcode,'utf-8')]
    
    
if __name__ == '__main__':
        
    from wsgiref.simple_server import make_server
    application = application
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()
