import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


logger.info("Starting logger")
string = "Hello World"
logger.debug(string)
logger.info("String has been printed")
