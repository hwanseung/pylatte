'''
Created on 2012. 10. 17.

@author: pylatte
'''
import threading
import logging

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
                logging.debug ("pylatte server going down~!")
                
                self.httpd.shutdown()
                
                break
                pass
            elif commend_input == "version":
                logging.debug ("version : "+self.version)
                pass
    
            elif commend_input == "help":
                logging.debug ("help       : view command list")
                logging.debug ("version    : view server version")
                logging.debug ("restart    : pylatte server restart")
                logging.debug ("quit       : pylatte server shutdown")
                pass
            elif commend_input == "info":
                logging.debug ("pylatte is python Web Framework - Insert Python code in HTML(called PYL)")
                logging.debug ("website : http://www.pylatte.org/")
                logging.debug ("mail : pylatte@pylatte.org")
                logging.debug ("License: GPL")
                pass
            elif commend_input == "restart":
                self.httpd.restart_server()
            else:
                logging.debug ("'"+commend_input +"'command is not found. ")
                pass
            
        pass;