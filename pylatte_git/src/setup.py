'''
Created on 2012. 8. 4.

@author: HwanSeung Lee(rucifer1217@gmail.com)
'''
from distutils.core import setup, Extension

classifierList=['Pylatte',
                'Pylatte:Database:DBMappingParser',
                'Pylatte:WebServer:configParser',
                'Pylatte:WebServer:formFile',
                'Pylatte:WebServer:latteServer',
                'Pylatte:WebServer:latteServerStart',
           'Pylatte:WebServer:latteSockeServer',
           'Pylatte:WebServer:methodGetGetParam',
           'Pylatte:WebServer:methodGetPostParam',
           'Pylatte:WebServer:postMultipartForm',
           'Pylatte:WebServer:pylToPy',
           'Pylatte:WebServer:requestHeaderInfo',
           'Pylatte:WebServer:sessionUtil']

setup(name='Pylatte',
      author='HwanSeung lee',
      author_email='rucifer1217@gmail.com',
      url='pylatte.org',
      version='0.9.8',
      classifiers = classifierList,
      packages=['Pylatte','Pylatte.Database','Pylatte.WebServer'],
      description='python Web Framework - pylatte'
)
