# -*- coding:utf-8 -*-
# author：Anson
from __future__ import unicode_literals
"""
usage:
   logging.debug 
   logging.info
   logging.warning
   logging.error
   logging.critical
"""

import os
import logging
import logging.handlers

from settings import LOG_PATH


class LogFormatter(logging.Formatter):
    DEFAULT_FORMAT = '%(asctime)s [%(levelname)1.1s %(module)s:%(lineno)d] %(message)s'
    DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

    def __init__(self, fmt=DEFAULT_FORMAT,
                 datefmt=DEFAULT_DATE_FORMAT):
        logging.Formatter.__init__(self, datefmt=datefmt)
        self._fmt = fmt

    def format(self, record):
        record.message = record.getMessage()
        record.asctime = self.formatTime(record, self.datefmt)
        formatted = self._fmt % record.__dict__

        if record.exc_info:
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)
        if record.exc_text:
            lines = [formatted.rstrip()]
            lines.extend(ln for ln in record.exc_text.split('\n'))
            formatted = '\n'.join(lines)
        return formatted.replace("\n", "\n    ")


def logger_to_file(logger, log_file_prefix, log_file_max_size, log_file_num_backups):
    channel = logging.handlers.RotatingFileHandler(
        filename=log_file_prefix,
        maxBytes=log_file_max_size,
        backupCount=log_file_num_backups)
    channel.setFormatter(LogFormatter())
    logger.addHandler(channel)


def get_logger(log_name, level=logging.DEBUG):
    LOG = logging.getLogger(log_name)
    LOG.setLevel(level)
    log_path = LOG_PATH
    file_path = os.path.join(log_path, '%s.log'%(log_name))
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))
    logger_to_file(LOG, file_path, 500000000, 7)
    return LOG
