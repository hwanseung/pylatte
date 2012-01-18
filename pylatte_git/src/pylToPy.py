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
        import re#정규표현식 모듈
        import math
        
        pypage = ["# -*- coding: utf-8 -*- \n"]
        pypage.append('import formFile\n')
        ex_i = 0
        
        loop_count=0
        
        pypage.append('class ' +self.pyl_path.split('.')[0]+':\n')
        pypage.append('\t'+'result=""\n')
        pypage.append('\t'+'sessionDic=dict()\n')
        pypage.append('\t'+'def __init__(self,param,pyFile,session,headerInfo,lattedb):\n')
        pypage.append('\t\t'+'self.generate(param,pyFile,session,headerInfo,lattedb)\n\n')
        
        pypage.append('\t'+'def generate(self,param,pyFile,session,headerInfo,lattedb):\n')
        
        # 파이썬 코드 처리
        for i in range(0, len(self.page)):
            try:
                i = ex_i         
                
                # 단순 변수 출력문이면 처리
                #print("char= "+self.page[i]+self.page[i+1]+" i="+str(i))
                
                if self.page[i] == '<' and self.page[i+1] == '\\' and self.page[i+2] == '$':
                    loop = 3;
                    pypage.append("\n")
                    for j in range(loop_count):
                        pypage.append('\t')    
                    pypage.append("self.result+='<$'")
                    ex_i = i+loop
                    pass
                
                elif self.page[i] == '\\' and self.page[i+1] == '$' and self.page[i+2] == '>':
                    loop = 3;
                    pypage.append("\n")
                    for j in range(loop_count):
                        pypage.append('\t')    
                    pypage.append("self.result+='$>'")
                    ex_i = i+loop
                    pass
                
                elif self.page[i] == '<' and self.page[i+1] == '$' and self.page[i+2] == '=':
                    #print("<$=")
                    
                    pypage.append("\n")
                    for j in range(loop_count):
                        pypage.append('\t')       
                    
                    pypage.append("self.result+=str(")
                    
                    loop = 3
                    while True:
                        pypage.append( self.page[ i+loop ] )
                        loop += 1
                        
                        if self.page[ i+loop ] == '$' and self.page[ i+loop+1 ] == '>':
                               
                            pypage.append(")")
                            ex_i = i + loop + 2
                            break
                
                        
                # 파이썬 코드 블럭이면 그대로 입력        
                elif self.page[i] == '<' and self.page[i+1] == '$' and self.page[i+2] != '=':
                    #print("<$")
                    loop = 2
                    
                    while True:
                        
                        pypage.append( self.page[ i+loop ] )
                        loop += 1
                        
                        if self.page[ i+loop ] == '$' and self.page[ i+loop+1 ] == '>':
                            
                            #print(self.page[i:i + loop + 2])
                            
                            content=self.page[i:i + loop + 2]
                            forList =re.findall(r"for.+:",content);
                            whileList =re.findall(r"while.+:",content);
                            ifList =re.findall(r"if.+:",content);
                            elifList =re.findall(r"elif.+:",content);
                            elseList =re.findall(r"else:",content);
                            passList =re.findall(r"pass",content);

                            localLoopCount=(len(forList)+len(whileList)+len(ifList)+len(elifList)+len(elseList)-len(passList));
                            loop_count+=localLoopCount#들여쓰기 카운트늘이기
                            
                            if localLoopCount<=0:
                                #spaceList =re.DOTALL(r".",content);
                                
                                spaceList = content;
                                
                                #print(spaceList)
                                localBackCount=0
                                localTapCount=0
                                localSpaceCount=0
                                spaceList=spaceList[0:-1]
                                #print(spaceList)
                                
                                try:
                                    while True:
                                        #print(spaceList)
                                        n_Count=spaceList.index("\n")
                                        #print(n_Count)
                                        #print(spaceList)
                                        spaceList=spaceList[n_Count+1:len(spaceList)]
                                        #print(spaceList)
                                except:
                                    #print("except")
                                    pass
                                finally:
                                    for z in spaceList:
                                        if z == '\n':
                                            localTapCount=0
                                            localSpaceCount=0
                                        elif z == '\t':
                                            localTapCount+=1;
                                        elif z == ' ':
                                            localSpaceCount+=1;
                                            
                                    pass
                                
                                
                                    
                                
                                localBackCount=localTapCount+(math.ceil(localSpaceCount/4))
                                #print(localBackCount)
                                loop_count=localBackCount#들여쓰기 카운트늘이기
                            
                            ex_i = i + loop + 2
                            break
                
               
                        
                #데이터베이스 정보 include 해주기!!
                elif self.page[i] == '<' and self.page[i+1:i+16] == '@latteDatabase>':
                    #print("<@lateeDatabase")
                    pypage.append("\n\t\t"+'import MySQLdb')
                    pypage.append("\n\t\t"+'latteDB=MySQLdb.connect(host=lattedb["host"],user=lattedb["user"],passwd=lattedb["password"],db=lattedb["dbName"])\n')
                    ex_i = i + 17
                    
                #데이터베이스 정보 include 해주기!!
                elif self.page[i] == '<' and self.page[i+1:i+19] == '@latteDatabaseExt>':
                    #print("<@lateeDatabaseExt")
                    pypage.append("\n\t\t"+'import DBMappingParser')
                    ex_i = i + 17
               
                else:
                    loop = 0
                    pypage.append("\n")
                    for j in range(loop_count):
                        pypage.append('\t')       
                    
                    pypage.append('self.result+=str("""')
                    
                    while True:
                        pypage.append( self.page[ i+loop ] )
                        loop += 1
                        
                        if self.page[ i+loop ] == '<':

                            pypage.append(' """)')
                            ex_i = i + loop
                            break 
            
            # 이 예외는 거의 파일의 끝에 도달했을 시 발생함
            except IndexError:
                #print("end")
                pypage.append(' """)'+"\n")
                break
        
        #print("end!!")   
        pypage.append('\t\t'+'self.sessionDic=session\n')
        pypage.append('\t\t'+'pass\n')
        pypage.append('\t'+'def getHtml(self):\n')
        pypage.append('\t\t'+'return self.result\n')
        pypage.append('\t\t'+'pass\n')
        pypage.append('\t'+'def getSession(self):\n')
        pypage.append('\t\t'+'return self.sessionDic\n')
        pypage.append('\t\t'+'pass\n') 
        # 파이썬 코드 만들어보기
        pystring = ""
        for p in pypage:
            if p=='\n':
                pystring += p+"\t\t"
            else:
                pystring += p
                
        self.pystring=pystring
    
    def outPy(self):
        # .py 로 저장하는데 저장할 때 원본 .pyl 파일명을 따름
        with open("topy/"+self.pyl_path.split('.')[0]+"_pyl.py", mode='w', encoding='utf-8') as result_file:
            result_file.write(self.pystring)
            
if __name__ == '__main__':
    str1 = """<h1>filter Test<h1>
<$
test="hello filter Test"
$>
<$=test $>"""
    p = pylToPy("urlTest.pyl",str1)
    p.outPy()

