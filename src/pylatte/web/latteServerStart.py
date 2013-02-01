'''
Created on 2011. 6. 4.

@author: HwanSeung Lee(rucifer1217@gmail.com)
'''
import pylatte.web.latteServer as latteServer
import pylatte.web.middleware.configSetMiddleware as configSetMiddleware
import pylatte.web.configParser as configParser
from wsgiref.simple_server import make_server

PORT = configParser.parseServerPort()

def start():
    application = latteServer.application
    application = configSetMiddleware.configSetMiddleware(application)
    srv = make_server('localhost', PORT, application)
    srv.serve_forever()
    
    pass;
