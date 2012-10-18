'''
Created on 2011. 9. 24.

@author: Hwanseung Lee(rucifer1217@gmail.com)
'''
class methodGetPostParam:
    dic = dict()

    def __init__(self, post):
        self.dic=dict()
        from urllib.parse import unquote
        post=post.replace("+", " ")
        post=unquote(post, 'utf-8', 'replace')
        post = str(post).split("b'", 1)[1].rsplit("'", 1)[0]
        try:
            params=post.split('&')
            
            for param in params:
                item = param.split('=')
                self.dic[item[0]]=item[1]
            print("param:")
            print(self.dic)
        
        except IndexError:
            print("파라미터 없음.")
        
        self.getParam()
        pass
    
    def getParam(self):
        return self.dic

if __name__ == '__main__':
    from urllib.parse import unquote
    str= "What%20is%20the+name+of+python3-based+web+framework%3F";
    str=str.replace("+", " ")
    
    print(unquote(str, 'utf-8', 'replace'))
    
    #p=methodGetPostParam("urlTest.pyl1?method=1&to=1");
    #print(p.getParam())