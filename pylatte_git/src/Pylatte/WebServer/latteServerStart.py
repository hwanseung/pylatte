'''
Created on 2011. 6. 4.

@author: HwanSeung Lee(rucifer1217@gmail.com)
'''
import Pylatte.WebServer.latteServer_wsgi as latteServer_wsgi
import Pylatte.WebServer.configParser as configParser
from wsgiref.simple_server import make_server

PORT = configParser.parseServerPort()

def start():
    application = latteServer_wsgi.ExceptionMiddleware(latteServer_wsgi.application)
    srv = make_server('localhost', PORT, application)
    srv.serve_forever()
    
    pass;
