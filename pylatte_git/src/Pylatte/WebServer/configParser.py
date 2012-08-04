'''
Created on 2011. 8. 4.

@author: HwanSeung Lee(rucifer1217@gmail.com)
'''
from xml.dom.minidom import parse

class pyLatteConfigPaser():
    
    mappingExcute=dict();
    mappingUrl=dict();
    urlMap=dict();
    
    databaseInfo=tuple();
    
    filterPyl=dict();
    filterUrl=dict();
    filterMap=dict();
    
    def __init__(self):
        self.doc=parse("pylatte_config.xml")
        
        #Mapping information
        self.parseUrlMapingExcute() #Bring the path to access(execute) pyl file actually from a xml file
        self.parseUrlMappingUrl() 	#Bring the virtual URL to link to one pyl file from a xml file
        self.makeUrlMap()			#Make dictionay data pairs
        print(self.urlMap)
        
        #Filtering information
        self.parseFilterPyl()		#Bring the path to filter pyl file actually from a xml file
        self.parseFilterUrl()		#Bring the path to be filtered pyl files from a xml file
        self.makeFilterMap()		#Make dictionay data pairs
        print(self.filterMap)
        
        pass
    
    def parseUrlMapingExcute(self):
        mappingList=self.doc.getElementsByTagName("pylatte");
        for item in mappingList:
            for item1 in item.childNodes:
                if(item1.nodeName=="pylatte-name"):
                    name=item1.firstChild.nodeValue
                if(item1.nodeName=="pylatte-pyl"):
                    pyName=item1.firstChild.nodeValue
            self.mappingExcute[name]=pyName
        pass
    
    def parseUrlMappingUrl(self):
        mappingList=self.doc.getElementsByTagName("pylatte-mapping");
        for item in mappingList:
            for item1 in item.childNodes:
                if(item1.nodeName=="pylatte-name"):
                    name=item1.firstChild.nodeValue
                if(item1.nodeName=="url-mapping"):
                    urlName=item1.firstChild.nodeValue
            self.mappingUrl[name]=urlName
        pass
    
    def makeUrlMap(self):
        for item in self.mappingExcute.keys():
            self.urlMap[self.mappingUrl[item]]=self.mappingExcute[item]
        
        pass
    
    def parseFilterPyl(self):
        mappingList=self.doc.getElementsByTagName("filter");
        for item in mappingList:
            for item1 in item.childNodes:
                if(item1.nodeName=="filter-name"):
                    name=item1.firstChild.nodeValue
                if(item1.nodeName=="filter-pyl"):
                    pyName=item1.firstChild.nodeValue
            self.filterPyl[name]=pyName
        pass
    
    def parseFilterUrl(self):
        mappingList=self.doc.getElementsByTagName("filter-mapping");
        for item in mappingList:
            filterUrlList=[];
            for item1 in item.childNodes:
                if(item1.nodeName=="filter-name"):
                    name=item1.firstChild.nodeValue
                if(item1.nodeName=="filter-url"):
                    filterUrlList.append(item1.firstChild.nodeValue)
            self.filterUrl[name]=filterUrlList
        pass
    
    def makeFilterMap(self):
        for item in self.filterUrl.keys():
            self.filterMap[self.filterPyl[item]]=self.filterUrl[item]
        pass

    
    def getUrlMap(self):
        return self.urlMap
    def getDataBaseInfo(self):
        return self.databaseInfo
    def getFilterMap(self):
        return self.filterMap
    pass

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


if __name__ == '__main__':
    #f = open("pylatte_config.xml","r",encoding="utf-8")
    
    p = pyLatteConfigPaser();
    #p.Parse(f.read())
    pass
    
