'''
Created on 2011. 6. 4.

@author: HwanSeung Lee(rucifer1217@gmail.com)
'''
import Pylatte.Web.latteServer_wsgi as latteServer_wsgi
import Pylatte.Web.Middleware.ExceptionMiddleware as ExceptionMiddleware
import Pylatte.Web.Middleware.ConfigSetMiddleware as ConfigSetMiddleware
import Pylatte.Web.configParser as configParser
from wsgiref.simple_server import make_server

PORT = configParser.parseServerPort()

def start():
    application = latteServer_wsgi.application
    #application = ExceptionMiddleware.ExceptionMiddleware(application)
    application = ConfigSetMiddleware.ConfigSetMiddleware(application)
    srv = make_server('localhost', PORT, application)
    srv.serve_forever()
    
    pass;
