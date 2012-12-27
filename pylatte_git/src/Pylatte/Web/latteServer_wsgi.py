'''
Created on 2011. 7. 16.

@author: Hwanseung Lee(rucifer1217@gmail.com)
'''
import re
from cgi import parse_qs, escape

import Pylatte.Web.configParser as configParser
import Pylatte.Web.requestHeaderInfo as requestHeaderInfo   #To use request Header information in pyl files.

def index(environ, start_response):
    """This function will be mounted on "/" and display a link
    to the hello world page."""
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'''Hello World Application
               This is the Hello World application:

`continue <hello/>`_

''']

def hello(environ, start_response):
    """Like the example above, but it uses the name specified in the
URL."""
    # get the name from the url if it was specified there.
    args = environ['myapp.url_args']
    if args:
        subject = escape(args[0])
    else:
        subject = 'World'
    start_response('200 OK', [('Content-Type', 'text/html')])
    result = '''Hello %(subject)s
    Hello %(subject)s!

''' % {'subject': subject}

    return [bytes(result,'utf-8')]

def not_found(environ, start_response):
    """Called if no URL matches."""
    start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
    return [b'Not Found']

# map urls to functions
urls = [
    (r'^$', index),
    (r'hello/?$', hello),
    (r'hello/(.+)$', hello)
]


def application(environ, start_response):
    urlMap=None
    headerInfo=requestHeaderInfo.requestHeaderInfo(environ)
    param = parse_qs(environ.get('QUERY_STRING', ''))
    path = environ.get('PATH_INFO', '').lstrip('/')
    
    print("GET method Parameters "+str(param))
    print(path)
    
    print("start to parser Config")
    parser=configParser.pyLatteConfigPaser()
    if urlMap==None:
        print(1)
    #    pass
    urlMap=parser.getUrlMap()
    print(urlMap.__len__())
    databaseInfo = parser.getDataBaseInfo()
    filterMap=parser.getFilterMap()
    print("end to parser Config\n")


    for regex, callback in urls:
        match = re.search(regex, path)
        if match is not None:
            print(match.groups())
            environ['myapp.url_args'] = match.groups()
            return callback(environ, start_response)
    return not_found(environ, start_response)


# import the helper functions we need to get and render tracebacks
from sys import exc_info
from traceback import format_tb

class ExceptionMiddleware(object):
    """The middleware we use."""

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        """Call the application can catch exceptions."""
        appiter = None
        # just call the application and send the output back
        # unchanged but catch exceptions
        try:
            appiter = self.app(environ, start_response)
            for item in appiter:
                yield item
        # if an exception occours we get the exception information
        # and prepare a traceback we can render
        except:
            e_type, e_value, tb = exc_info()
            traceback = ['Traceback (most recent call last):']
            traceback += format_tb(tb)
            traceback.append('%s: %s' % (e_type.__name__, e_value))
            # we might have not a stated response by now. try
            # to start one with the status code 500 or ignore an
            # raised exception if the application already started one.
            try:
                start_response('500 INTERNAL SERVER ERROR', [
                               ('Content-Type', 'text/plain')])
            except:
                pass
            yield '\n'.join(traceback)

        # wsgi applications might have a close function. If it exists
        # it *must* be called.
        if hasattr(appiter, 'close'):
            appiter.close()
    
    
if __name__ == '__main__':
        
    from wsgiref.simple_server import make_server
    application = application
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()
