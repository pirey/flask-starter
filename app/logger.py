import os
import logging

from datetime import datetime
from app import config

log_format = "\n=====================================================\n%(asctime)s - %(name)s - %(levelname)s \n%(message)s\n"
log_file = os.path.join(os.path.dirname(os.path.realpath(
    __file__)), 'logs/{:%Y-%m-%d}.log'.format(datetime.now()))

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(logging.Formatter(log_format))

file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter(log_format))

logger = logging.getLogger(__name__)
if config.FLASK_ENV == 'development':
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)
logger.addHandler(stream_handler)
logger.addHandler(file_handler)
