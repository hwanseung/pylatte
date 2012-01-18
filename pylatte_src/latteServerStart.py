import latteSocketServer
import latteServer

import threading

def parseServerPort():
    """
    Bring a server port number from pylatte_config.xml
    """
    from xml.dom.minidom import parse
    doc=parse("pylatte_config.xml")
    tags = doc.getElementsByTagName("pylatte-server")
    for item in tags:
        for item1 in item.childNodes:
            if(item1.nodeName=="port"):
                return int(item1.firstChild.nodeValue)
                
    pass 

print("**start latteServer**\n")
PORT = parseServerPort()
Handler = latteServer.latteServer
httpd = latteSocketServer.latteSockeServer(("", PORT), Handler)

def worker():
    """
    Start a server
    """
    print ("serving at port", PORT)
    httpd.serve_forever()
    pass;

def my_service():
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
        
h = threading.Thread(name='httpd', target=worker)
t = threading.Thread(name='timer', target=my_service)

h.start()
t.start()



