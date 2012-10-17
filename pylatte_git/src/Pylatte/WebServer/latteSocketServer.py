'''
Created on 2011. 7. 19.

@author: Hwanseung Lee(rucifer1217@gmail.com)
'''
import socket
import socketserver
import Pylatte.WebServer.configParser as configParser
import Pylatte.WebServer.pylToPy as pylToPy
import Pylatte.WebServer.service as service

pylatte_AsciiArt="""
=============================================================                            
                     ,,                               
                   `7MM           mm     mm           
                     MM           MM     MM           
`7MMpdMAo.`7M'   `MF'MM   ,6"Yb.mmMMmm mmMMmm .gP"Ya  
  MM   `Wb  VA   ,V  MM  8)   MM  MM     MM  ,M'   Yb 
  MM    M8   VA ,V   MM   ,pm9MM  MM     MM  8M\"\"\"\"\"\" 
  MM   ,AP    VVV    MM  8M   MM  MM     MM  YM.    , 
  MMbmmd'     ,V   .JMML.`Moo9^Yo.`Mbmo  `Mbmo`Mbmmd' 
  MM         ,V                                       
.JMML.    OOb"                                        
============================================================="""


class latteSockeServer(socketserver.TCPServer):
    def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True):
        socketserver.TCPServer.__init__(self, server_address, RequestHandlerClass, bind_and_activate=bind_and_activate)
        
        self.restart_server()
        
        th = service.service()
        th.init(self,RequestHandlerClass.server_version)
        th.start()
        
        pass
    
    def restart_server(self):
        self.sessionFileRemove()
        self.topyFileRemove()
        print("start to parser Config")
        parser=configParser.pyLatteConfigPaser()
        
        self.urlMap=parser.getUrlMap()
        self.databaseInfo = parser.getDataBaseInfo()
        self.filterMap=parser.getFilterMap()
        print("end to parser Config\n")
        
        print("start to pylToPy")
        for item in self.urlMap.values():
            print("processing pylTopy : "+item)
        
            
            #Looking for filter to execute before pyl files executed.
            filterStr = ""
            for item1 in self.filterMap.keys():
                if item in self.filterMap[item1]:
                    filterStr += open('pyl/'+item1, encoding='utf-8').read()+"\n"
                    #print(str)
                    
            #print(filterStr); 
            #if item in self.filterMap
            
            p=pylToPy.pylToPy(item,filterStr)
            p.outPy()
        print("end to pylToPy\n")
        print(pylatte_AsciiArt)
        pass
    
    def server_bind(self):
        
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)
        self.server_address = self.socket.getsockname()
    
    def shutdown(self):
        socketserver.TCPServer.shutdown(self)
        self.sessionFileRemove()
        self.topyFileRemove()
        self.socket.close()
        del self.socket        
        pass
    
    def sessionFileRemove(self):
        import os
        
        # Delete the files first.
        
        for dirpath, dirnames, filenames in os.walk(os.getcwd()+"/session"):
            for each_file in filenames:
                if os.path.exists(os.path.join(dirpath, each_file)):
                    os.remove(os.path.join(dirpath, each_file))
        
        print("session File Remove\n")
        pass
    
    def topyFileRemove(self):
        import os
        
        # Delete the files first.
        
        for dirpath, dirnames, filenames in os.walk(os.getcwd()+"/topy"):
            for each_file in filenames:
                if os.path.exists(os.path.join(dirpath, each_file)):
                    os.remove(os.path.join(dirpath, each_file))
                    
        for dirpath, dirnames, filenames in os.walk(os.getcwd()+"/topy/__pycache__"):
            for each_file in filenames:
                if os.path.exists(os.path.join(dirpath, each_file)):
                    os.remove(os.path.join(dirpath, each_file))
        
        print("topy File Remove\n")
        pass
    
            
if __name__ == '__main__':
    import os
        
    # Delete the files first.
    print(os.getcwd())
    
    for dirpath, dirnames, filenames in os.walk(os.getcwd()+"/session"):
        for each_file in filenames:
            if os.path.exists(os.path.join(dirpath, each_file)):
                print('- ' + dirpath + '/' + each_file)
                os.remove(os.path.join(dirpath, each_file))

                

    
