'''
Created on 2012. 8. 4.

@author: HwanSeung Lee(rucifer1217@gmail.com)
'''
import logging
import Pylatte.Web.latteServerStart as latteServerStart


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
latteServerStart.start()


