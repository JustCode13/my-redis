import logging

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def info_logger(message):
    logger.info("Just an information")

def warning_logger(message):
    logger.warning("Its a warning")

def error_logger(message):
    logger.error("Did you try to divide by zero?")