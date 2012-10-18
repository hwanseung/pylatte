'''
Created on 2011. 9. 1.

@author: Sangkeun Park(pskalyber@gmail.com)
'''

from xml.dom.minidom import parse

class pyLatteDBMappingParser:

    sqlList = dict()
    tagList = list()
    parametersList = list()
    database = tuple()
    doc = -1
    
    def __init__(self):
        try:
            self.loadXmlFromFile()
            self.parseDataBaseInfo()
        except IOError:
            print('No such file or directory : ' + self.doc._get_documentURI())
            
    def loadXmlFromFile(self):
        """Load XML document about database information and SQL Mapping information.
        """
        
        try:
            xmlFD = open("db_mapping.xml")
        except IOError:
            print('Error - invalid file name or path')
            return None
        else:
            try:
                self.doc = parse(xmlFD)
            except Exception:
                print("Error - loading fail")
            else:
                print("XML document loading complete")
        return None
                
    def parseDataBaseInfo(self):
        """Get database information(host, user, password, database name) from XML document
        And Connect to MySQL to use the database"""
        
        try:
            tags = self.doc.getElementsByTagName("sql")
            
            for item in tags:
                if str.lower(item.getAttribute('db')) == 'mysql':
                    info = dict()
                    for item1 in item.childNodes:
                        if(item1.nodeName=="host"):
                            #print(item1.firstChild.nodeValue)
                            info["host"]=item1.firstChild.nodeValue
                        if(item1.nodeName=="user"):
                            #print(item1.firstChild.nodeValue)
                            info["user"]=item1.firstChild.nodeValue
                        if(item1.nodeName=="password"):
                            #print(item1.firstChild.nodeValue);
                            info["password"]=item1.firstChild.nodeValue
                        if(item1.nodeName=="dbName"):
                            #print(item1.firstChild.nodeValue);
                            info["dbName"]=item1.firstChild.nodeValue
                    import MySQLdb
                    self.latteDB=MySQLdb.connect(host=info["host"],user=info["user"],passwd=info["password"],db=info["dbName"])
                elif str.lower(item.getAttribute('db')) == 'mongodb':
                    info = dict()
                    for item1 in item.childNodes:
                        if(item1.nodeName=="host"):
                            #print(item1.firstChild.nodeValue)
                            info["host"]=item1.firstChild.nodeValue
                        if(item1.nodeName=="port"):
                            #print(item1.firstChild.nodeValue)
                            info["port"]=item1.firstChild.nodeValue
                    import pymongo
                    self.latteDB=pymongo.Connection(info["host"], int(info["port"]))
                    
        except AttributeError:
            print('Error - XML Parsing failed')
            
    def queryProcessing(self, node, value):
        """Execute SQL with replacing variables in SQL"""
        
        try:
            #print(node.firstChild.nodeValue)              
            if(value):    # if 'value' is not None, '$value$' have to be replaced 
                print("SQL :"+str(node.firstChild.nodeValue))
                print("param : "+str(value))
                splitedSQL = str(node.firstChild.nodeValue).rsplit('$')
                completedSQL = ""
                valuesCount = (len(splitedSQL)-1) / 2
                print("valuesCount " +str(valuesCount));
                for i in splitedSQL:
                    for v in value.keys():
                        if i==v:    # if one phrase is matched to one variable in dictionary data, that will be replaced each other.
                            if type(value[i])==str:    # if one value is str type, it will be transformed 'value' to express str type
                                value[i]="'" + value[i] + "'"
                            i=value[i]
                            valuesCount = valuesCount -1
                    completedSQL += str(i)
                if (valuesCount > 0):
                    print('Error - Some $value$ are not replaced. ')
                    raise Exception
                print("completedSQL :"+completedSQL) 
                self.latteDB.query(completedSQL)
            else:        # if 'value' is None, execute the query node directly.
                self.latteDB.query(node.firstChild.nodeValue)
            
            if (node.nodeName == 'select'):
                result=self.latteDB.store_result()
                self.database=result.fetch_row(maxrows=0, how=1)
            return self.database
        except Exception as e:
            print('Error - Failed to execute Query. Check out specified SQL on XML or parameter for $value$')
            print(e.args[0])
            
            
               
    def queryForList(self, parameter, value=None):
        """Looking for matched SQL with specified id from XML document"""
        try:
            parametersList = str(parameter).rsplit('.')
            
            self.tagList = self.doc.getElementsByTagName("sqlMap")
            for item in self.tagList:
                if( item.getAttribute('id') == parametersList[0] ):
                    for childItem in item.childNodes:
                        if(childItem.nodeName=="select" and childItem.getAttribute('id') == parametersList[1]):
                            return self.queryProcessing(childItem, value)
                        elif(childItem.nodeName=="insert" and childItem.getAttribute('id') == parametersList[1]):
                            return self.queryProcessing(childItem, value)
                        elif(childItem.nodeName=="update" and childItem.getAttribute('id') == parametersList[1]):
                            return self.queryProcessing(childItem, value)
                        elif(childItem.nodeName=="delete" and childItem.getAttribute('id') == parametersList[1]):
                            return self.queryProcessing(childItem, value)
                    raise Exception
            raise Exception
        except Exception:
            print('There is no matched node or ID on the XML document')

    def makeToUseSimpleDB(self):
        
        return self.latteDB
        pass
        
