'''
Created on 2011. 7. 24.

@author: Hwanseung Lee(rucifer1217@gmail.com)


this Class is not used in pylatte any more.
'''
import logging

class methodGetGetParam:
    dic = dict()

    def __init__(self,path):
        self.dic=dict()
        from urllib.parse import unquote
        path=path.replace("+", " ")
        path=unquote(path, 'utf-8', 'replace')
        try:
            params=path.split('?')[1].split('&')
            
            for param in params:
                item = param.split('=')
                self.dic[item[0]]=item[1]
            
            logging.debug(self.dic)
        
        except IndexError:
            #logging.debug("parameter is none")
            pass
        
        self.getParam()
        pass
    
    def getParam(self):
        return self.dic

if __name__ == '__main__':
    p=methodGetGetParam("urlTest.pyl1?method=1&to=1");
    logging.debug(p.getParam())