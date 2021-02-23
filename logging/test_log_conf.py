import logging
from logging.config import fileConfig

fileConfig('log.conf')
logger = logging.getLogger()
logger.debug(" test logger conf")
