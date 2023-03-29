# *** Logging stuff ***

import logging

logging.basicConfig(filename='logs.log',filemode='w',format='%(ascitime)s %(message)s')

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("Harmless debug Message")
logger.info("Just an information")


