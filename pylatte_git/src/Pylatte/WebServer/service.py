'''
Created on 2012. 10. 17.

@author: pylatte
'''
import threading

class service(threading.Thread):
    httpd = ""
    def init(self,httpd):
        self.httpd=httpd
        pass
    def run(self):
        """
        Checking a command from interective prompt.
        """
        while True:
            commend_input = input("if you want to Shutdown Server, You have to type 'quit'")
            if commend_input == "quit":
                print ("server going down")
                
                self.httpd.shutdown()
                
                break
            
        pass;