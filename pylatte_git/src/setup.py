'''
Created on 2012. 8. 4.

@author: HwanSeung Lee(rucifer1217@gmail.com)
'''
from distutils.core import setup, Extension

classifierList=['Pylatte',
                'Pylatte:Database:DBMappingParser',
                'Pylatte:Web:configParser',
                'Pylatte:Web:formFile',
                'Pylatte:Web:latteServer',
                'Pylatte:Web:latteServerStart',
           'Pylatte:Web:latteSockeServer',
           'Pylatte:Web:methodGetGetParam',
           'Pylatte:Web:methodGetPostParam',
           'Pylatte:Web:postMultipartForm',
           'Pylatte:Web:pylToPy',
           'Pylatte:Web:requestHeaderInfo',
           'Pylatte:Web:sessionUtil']

setup(name='Pylatte',
      author='HwanSeung lee',
      author_email='rucifer1217@gmail.com',
      url='pylatte.org',
      version='0.9.8.1.5',
      classifiers = classifierList,
      packages=['Pylatte','Pylatte.Database','Pylatte.Web'],
      description='python Web Framework - pylatte'
)
