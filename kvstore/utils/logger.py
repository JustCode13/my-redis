import logging

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def info(message):
    logger.info("Just an information")

def warning(message):
    logger.warning("Its a warning")

def error(message):
    logger.error("Did you try to divide by zero?")