'''
Created on 2011. 6. 4.

@author: HwanSeung Lee(rucifer1217@gmail.com)
'''
import threading
import Pylatte.WebServer.latteSocketServer as latteSocketServer
import Pylatte.WebServer.latteServer as latteServer
import Pylatte.WebServer.configParser as configParser


print("**start latteServer**\n")
PORT = configParser.parseServerPort()
Handler = latteServer.latteServer
httpd = latteSocketServer.latteSockeServer(("", PORT), Handler)
    
def worker():
    """
    Start a server
    """
    print ("serving at port", PORT)
    httpd.serve_forever()
    
    pass;


def start():
    h = threading.Thread(name='httpd', target=worker())
    h.start()
    
    

    pass;
