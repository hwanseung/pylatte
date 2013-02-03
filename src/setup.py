'''
Created on 2012. 8. 4.

@author: HwanSeung Lee(rucifer1217@gmail.com)
'''
from distutils.core import setup, Extension

classifierList=['pylatte',
                'pylatte:database:DBMappingParser',
                'pylatte:web:middleware:configSetMiddleware',
                'pylatte:web:configParser',
                'pylatte:web:formFile',
                'pylatte:web:latteServer',
                'pylatte:web:latteServerStart',
                'Pylatte:Web:pylToPy',
                'Pylatte:Web:requestHeaderInfo',
                'Pylatte:Web:sessionUtil']

setup(name='Pylatte',
      author='HwanSeung lee',
      author_email='pylatte@pylatte.org',
      url='http://pylatte.org',
      version='1.0',
      classifiers = classifierList,
      packages=['pylatte','pylatte.database','pylatte.web','pylatte.web.middleware'],
      install_requires=['ply','mysql-connector-python','pymongo3'],
      description='pylatte(python Web Framework) '
)
