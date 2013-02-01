'''
Created on 2012. 12. 27.

@author: pylatte
'''
# import the helper functions we need to get and render tracebacks

import pylatte.web.configParser as configParser

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

class configSetMiddleware(object):
    
    parser = None
    
    def __init__(self, app):
        self.app = app
        self.parser = configParser.pyLatteConfigPaser()
        print(pylatte_AsciiArt)
    def __call__(self, environ, start_response):
       
        ##print(self.parser.getLastConfigFileModifyTime())
        ##print(self.parser.getConfigFileModifyTime())
        
        
        if self.parser.getLastConfigFileModifyTime() != self.parser.getConfigFileModifyTime():
            """설정파일을 읽어왔을때의 그 파일의 수정시간이 다른다면 다시 읽어오기."""
            self.parser = configParser.pyLatteConfigPaser()
            pass
        
        environ["urlMap"] = self.parser.getUrlMap()
        environ["filterMap"] = self.parser.getFilterMap()
        
        appiter = self.app(environ, start_response)
        for item in appiter:
            #print(str(item))
            yield item