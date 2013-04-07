'''
Created on 2011. 9. 1.

@author: Sangkeun Park(pskalyber@gmail.com)
'''
import logging
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
            logging.debug('No such file or directory : ' + self.doc._get_documentURI())
            
    def loadXmlFromFile(self):
        """Load XML document about database information and SQL Mapping information.
        """
        
        try:
            xmlFD = open("db_mapping.xml")
        except IOError:
            logging.debug('Error - invalid file name or path')
            return None
        else:
            try:
                self.doc = parse(xmlFD)
            except Exception:
                logging.debug("Error - loading fail")
            else:
                logging.debug("XML document loading complete")
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
                            #logging.debug(item1.firstChild.nodeValue)
                            info["host"]=item1.firstChild.nodeValue
                        if(item1.nodeName=="user"):
                            #logging.debug(item1.firstChild.nodeValue)
                            info["user"]=item1.firstChild.nodeValue
                        if(item1.nodeName=="password"):
                            #logging.debug(item1.firstChild.nodeValue);
                            info["password"]=item1.firstChild.nodeValue
                        if(item1.nodeName=="dbName"):
                            #logging.debug(item1.firstChild.nodeValue);
                            info["dbName"]=item1.firstChild.nodeValue
                    import mysql.connector
                    
                    self.latteDB=mysql.connector.connect(user=info["user"], password=info["password"], host=info["host"], database=info["dbName"])
                elif str.lower(item.getAttribute('db')) == 'mongodb':
                    info = dict()
                    for item1 in item.childNodes:
                        if(item1.nodeName=="host"):
                            #logging.debug(item1.firstChild.nodeValue)
                            info["host"]=item1.firstChild.nodeValue
                        if(item1.nodeName=="port"):
                            #logging.debug(item1.firstChild.nodeValue)
                            info["port"]=item1.firstChild.nodeValue
                    import pymongo
                    self.latteDB=pymongo.Connection(info["host"], int(info["port"]))
                    
        except AttributeError:
            logging.debug('Error - XML Parsing failed')
            
    def queryProcessing(self, node, value):
        """Execute SQL with replacing variables in SQL"""
        
        try:
            #logging.debug(node.firstChild.nodeValue)              
            cursor = self.latteDB.cursor()
            if(value):    # if 'value' is not None, '$value$' have to be replaced 
                logging.debug("SQL :"+str(node.firstChild.nodeValue))
                logging.debug("param : "+str(value))
                splitedSQL = str(node.firstChild.nodeValue).rsplit('$')
                completedSQL = ""
                valuesCount = (len(splitedSQL)-1) / 2
                logging.debug("valuesCount " +str(valuesCount));
                for i in splitedSQL:
                    for v in value.keys():
                        if i==v:    # if one phrase is matched to one variable in dictionary data, that will be replaced each other.
                            if type(value[i])==str:    # if one value is str type, it will be transformed 'value' to express str type
                                value[i]="'" + value[i] + "'"
                            i=value[i]
                            valuesCount = valuesCount -1
                    completedSQL += str(i)
                if (valuesCount > 0):
                    logging.debug('Error - Some $value$ are not replaced. ')
                    raise Exception
                logging.debug("completedSQL :"+completedSQL) 
                
                cursor.execute(completedSQL)
            else:        # if 'value' is None, execute the query node directly.
                logging.debug("completedSQL : "+node.firstChild.nodeValue) 
                cursor.execute(node.firstChild.nodeValue)
            
            if (node.nodeName == 'select'):
                self.database=cursor
                logging.debug(cursor)
                
            return self.database
        except Exception as e:
            logging.debug('Error - Failed to execute Query. Check out specified SQL on XML or parameter for $value$')
            logging.debug(e.args[0])
            
            
               
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
            logging.debug('There is no matched node or ID on the XML document')

    def makeToUseSimpleDB(self):
        
        return self.latteDB
        pass
        
