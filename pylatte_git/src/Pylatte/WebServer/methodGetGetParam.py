'''
Created on 2011. 7. 24.

@author: Hwanseung Lee(rucifer1217@gmail.com)
'''

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
            
            print(self.dic)
        
        except IndexError:
            #print("parameter is none")
            pass
        
        self.getParam()
        pass
    
    def getParam(self):
        return self.dic

if __name__ == '__main__':
    p=methodGetGetParam("urlTest.pyl1?method=1&to=1");
    print(p.getParam())