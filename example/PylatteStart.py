'''
Created on 2012. 8. 4.

@author: HwanSeung Lee(rucifer1217@gmail.com)
'''
import logging
import pylatte.web.latteServerStart as latteServerStart


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
latteServerStart.start()


