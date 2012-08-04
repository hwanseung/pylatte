'''
Created on 2011. 7. 29.

@author: HwanSeung Lee(rucifer1217@gmail.com)

#request Header information
'''
class requestHeaderInfo:
    
    dic=dict()
    def __init__(self,headerInfo):
        
        self.dic["path"]=headerInfo.path
        self.dic["Accept"]=headerInfo.headers.get('Accept', "")
        self.dic["Accept-Charset"]=headerInfo.headers.get('Accept-Charset', "")
        self.dic["Accept-Encoding"]=headerInfo.headers.get('Accept-Encoding', "")
        self.dic["Accept-Language"]=headerInfo.headers.get('Accept-Language', "")
        self.dic["Accept-Ranges"]=headerInfo.headers.get('Accept-Language', "")
        self.dic["Age"]=headerInfo.headers.get('Age', "")
        self.dic["Allow"]=headerInfo.headers.get('Allow', "")
        self.dic["Authorization"]=headerInfo.headers.get('Authorization', "")
        self.dic["Cache-Control"]=headerInfo.headers.get('Cache-Control', "")
        self.dic["Connection"]=headerInfo.headers.get('Connection', "")
        self.dic["Content-Encoding"]=headerInfo.headers.get('Content-Encoding', "")
        self.dic["Content-Language"]=headerInfo.headers.get('Content-Language', "")
        self.dic["Content-Length"]=headerInfo.headers.get('Content-Length', "")
        self.dic["Content-Location"]=headerInfo.headers.get('Content-Location', "")
        self.dic["Content-MD5"]=headerInfo.headers.get('Content-MD5', "")
        self.dic["Content-Range"]=headerInfo.headers.get('Content-Range', "")
        self.dic["Content-Type"]=headerInfo.headers.get('Content-Type', "")
        self.dic["ETag"]=headerInfo.headers.get('ETag', "")
        self.dic["Expect"]=headerInfo.headers.get('Expect', "")
        self.dic["Expires"]=headerInfo.headers.get('Expires', "")
        self.dic["From"]=headerInfo.headers.get('From', "")
        self.dic["Host"]=headerInfo.headers.get('Host', "")
        self.dic["If-Match"]=headerInfo.headers.get('If-Match', "")
        self.dic["If-Modified-Since"]=headerInfo.headers.get('If-Modified-Since', "")
        self.dic["If-None-Match"]=headerInfo.headers.get('If-None-Match', "")
        self.dic["If-Range"]=headerInfo.headers.get('If-Range', "")
        self.dic["If-Unmodified-Since"]=headerInfo.headers.get('If-Unmodified-Since', "")
        self.dic["Last-Modified"]=headerInfo.headers.get('Last-Modified', "")
        self.dic["Location"]=headerInfo.headers.get('Location', "")
        self.dic["Max-Forwards"]=headerInfo.headers.get('Max-Forwards', "")
        self.dic["Pragma"]=headerInfo.headers.get('Pragma', "")
        self.dic["Proxy-Authenticate"]=headerInfo.headers.get('Proxy-Authenticate', "")
        self.dic["Proxy-Authorization"]=headerInfo.headers.get('Proxy-Authorization', "")
        self.dic["Range"]=headerInfo.headers.get('Range', "")
        self.dic["Referer"]=headerInfo.headers.get('Referer', "")
        self.dic["Retry-After"]=headerInfo.headers.get('Retry-After', "")
        self.dic["Server"]=headerInfo.headers.get('Server', "")
        self.dic["TE"]=headerInfo.headers.get('TE', "")
        self.dic["Trailer"]=headerInfo.headers.get('Trailer', "")
        self.dic["Transfer-Encoding"]=headerInfo.headers.get('Transfer-Encoding', "")
        self.dic["Upgrade"]=headerInfo.headers.get('Upgrade', "")
        self.dic["User-Agent"]=headerInfo.headers.get('User-Agent', "")
        self.dic["Vary"]=headerInfo.headers.get('Vary', "")
        self.dic["Via"]=headerInfo.headers.get('Via', "")
        self.dic["WWW-Authenticate"]=headerInfo.headers.get('WWW-Authenticate', "")
        self.dic["Cookie"]=headerInfo.headers.get('Cookie', "")
        
        pass
    def getHeaderInfo(self):
        return self.dic
        
        pass
