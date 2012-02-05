import ply.lex as lex
import math

# List of token names.   This is always required
tokens = (
   'PYL_OUTPUT',
   'PYL',
   'HTML',
   'HTML_L',
   'HTML_R',
   'NOHTML',
) 

def t_PYL_OUTPUT(t):
    r'\s*\<\$\=(.*?)\$\>' 
    t.value = (t.value)
    return t

def t_PYL(t):
    r'\s*\<\$[^<>]*?\$\>' 
    t.value = (t.value)
    print("#"+t.value+"#")
    return t

def t_HTML(t):
    r'\s*\<[\/\!]*?[^<>]*?\>' 
    t.value = (t.value)  
    return t

def t_HTML_L(t):
    r'\s*\<[\!]*[.|\w]*?[^<]' 
    t.value = (t.value)  
    return t

def t_HTML_R(t):
    r'\s*[\/\!]*[^<>]*\>' 
    t.value = (t.value)  
    return t

def t_NOHTML(t):
    r'\s*[^<>\s]+' 
    t.value = (t.value)     
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = '\t'

# Error handling rule
def t_error(t):
    print ("Illegal character '%s'" % t.value[0:40])
    t.lexer.skip(1)

class pylToPy:
    pystring=""
    page=""
    pyl_path=""
    def __init__(self,pyl_path,filterStr):
        # 파일 읽기
        self.pyl_path=pyl_path
        if filterStr == "":
            self.page = open('pyl/'+pyl_path, encoding='utf-8').read()
        else:
            self.page += filterStr
            self.page += open('pyl/'+pyl_path, encoding='utf-8').read()
            
            
        self.translationPy()
        pass
    
        
    def translationPy(self):
        pypage = ["# -*- coding: utf-8 -*- \n"]
        pypage.append('import formFile\n')
        
        pypage.append('class ' +self.pyl_path.split('.')[0]+':\n')
        pypage.append('\t'+'pylToHtmlResult=""\n')
        pypage.append('\t'+'sessionDic=dict()\n')
        pypage.append('\t'+'def __init__(self,param,pyFile,session,headerInfo,lattedb):\n')
        pypage.append('\t\t'+'self.generate(param,pyFile,session,headerInfo,lattedb)\n\n')
        
        pypage.append('\t'+'def generate(self,param,pyFile,session,headerInfo,lattedb):\n')
        
        # 파이썬 코드 처리
        # Build the lexer
        lexer = lex.lex(debug=1)
        
        # Give the lexer some input
        lexer.input(self.page)
        
        while True:
            tok = lexer.token()
            processResult=""
            if not tok: 
                break      # No more input
            else:
                if tok.type=="PYL":
                    processResult=self.processPyl(tok.type, tok.value, tok.lineno, tok.lexpos)
                elif tok.type=="PYL_OUTPUT":
                    processResult=self.processPylOut(tok.type, tok.value, tok.lineno, tok.lexpos)
                elif tok.type=="HTML":
                    processResult=self.processHTML(tok.type, tok.value, tok.lineno, tok.lexpos)
                elif tok.type=="HTML" or tok.type=="HTML_L" or tok.type=="HTML_R" or tok.type=="NOHTML":
                    processResult=self.processNotPyl(tok.type, tok.value, tok.lineno, tok.lexpos)
            pypage.append(processResult)
             
        #print("end!!")   
        pypage.append('\t\t'+'self.sessionDic=session\n')
        pypage.append('\t\t'+'pass\n')
        pypage.append('\t'+'def getHtml(self):\n')
        pypage.append('\t\t'+'return self.pylToHtmlResult\n')
        pypage.append('\t\t'+'pass\n')
        pypage.append('\t'+'def getSession(self):\n')
        pypage.append('\t\t'+'return self.sessionDic\n')
        pypage.append('\t\t'+'pass\n') 
        # 파이썬 코드 만들어보기
        
        print(type(pypage))
        print(type(self.pystring))
        pystring = ""
        for p in pypage:
            if p=='\n':
                pystring += "\n\t\t"
            else:
                pystring += p
                
        self.pystring=pystring
        pass
        
    def processPyl(self, type,value,lineno,lexpos):
        
        #print("***\n"+t.value[3:-3]+"\n***")
        content=value[3:-3];
        
        #print("+++"+t.value[-2:]+"##")
        if value[0:3]=="<$\n" and value[-2:]=="$>":
            #print("$$"+content+"$$")
            try:
                firstNPos=content.index("\n")
                #print("Value", firstNPos, secondNPos)
                firstLineCotent=content[:firstNPos]
            except ValueError:
                #print("ValueError")
                firstLineCotent=content
            finally:
                print("&&"+firstLineCotent+"&&")
                localTapCount=0
                localSpaceCount=0
                for i in firstLineCotent:
                    if i == '\n':
                        localTapCount=0
                        localSpaceCount=0
                    elif i == '\t':
                        localTapCount+=1;
                    elif i == ' ':
                        localSpaceCount+=1;
                    else:
                        print("end" + i)
                        print("count", localTapCount, localSpaceCount)
                        count=localTapCount+(math.ceil(localSpaceCount/4))
                        space="\n"
                        space+="\t"
                        content=str(content).replace("\n",space)
                        print("%%%\n"+content+"\n%%%")
                        break
        else:
            print("this is not pylcode")
        
        return '\t\tself.pylToHtmlResult+=str("pylatte")\n'
        pass
    
    def processPylOut(self, type,value,lineno,lexpos):
        value=value.replace('<$=', "")
        value=value.replace('$>', "")
        return '\t\tself.pylToHtmlResult+=str("""'+value+'""")\n'
        pass
    
    def processHTML(self, type,value,lineno,lexpos):
        return '\t\tself.pylToHtmlResult+=str("""'+value+'""")\n'
        pass
    
    def processNotPyl(self, type,value,lineno,lexpos):
        value=value.replace('\"', "&quot;")
        return '\t\tself.pylToHtmlResult+=str("""'+value+'""")\n'
        pass
    
    
    def outPy(self):
        # .py 로 저장하는데 저장할 때 원본 .pyl 파일명을 따름
        with open("topy/"+self.pyl_path.split('.')[0]+"_pyl.py", mode='w', encoding='utf-8') as result_file:
            result_file.write(self.pystring)

