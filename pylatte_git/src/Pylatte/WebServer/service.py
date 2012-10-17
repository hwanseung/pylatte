'''
Created on 2012. 10. 17.

@author: pylatte
'''
import threading

class service(threading.Thread):
    httpd = ""
    version = ""
    def init(self,httpd,version):
        self.httpd=httpd
        self.version = version
        pass
    def run(self):
        """
        Checking a command from interective prompt.
        """
        while True:
            commend_input = input(">>")
            if commend_input == "quit":
                print ("pylatte server going down~!")
                
                self.httpd.shutdown()
                
                break
                pass
            elif commend_input == "version":
                print ("version : "+self.version)
                pass
    
            elif commend_input == "help":
                print ("help       : view command list")
                print ("version    : view server version")
                print ("restart    : pylatte server restart")
                print ("quit       : pylatte server shutdown")
                pass
            elif commend_input == "info":
                print ("pylatte is python Web Framework - Insert Python code in HTML(called PYL) and execute webserver")
                print ("website : http://www.pylatte.org/")
                print ("mail : pylatte@pylatte.org")
                print ("License: GPL")
                pass
            elif commend_input == "restart":
                self.httpd.restart_server()
            else:
                print ("'"+commend_input +"'command is not found. ")
                pass
            
        pass;