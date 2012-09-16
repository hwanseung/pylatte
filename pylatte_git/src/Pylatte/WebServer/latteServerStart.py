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

def latte_service():
    """
    Checking a command from interective prompt.
    """
    while True:
        commend_input = input("if you want to Shutdown Server, You have to type 'quit'")
        if commend_input == "quit":
            print ("server going down")
            
            httpd.shutdown()
            
            break
    pass;

def start():
    h = threading.Thread(name='httpd', target=worker())
    t = threading.Thread(name='timer', target=latte_service())
    h.start()
    t.start()    
    pass;
