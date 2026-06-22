import logging

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def info_logger(message):
    logger.info(message)

def warning_logger(message):
    logger.warning(message)

def error_logger(message):
    logger.error(message)