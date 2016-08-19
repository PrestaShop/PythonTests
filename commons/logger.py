# -*- coding: utf-8 -*-
import logging
import datetime
import sys

from commons.Configuration import Configuration


class BufferHandler(logging.Handler):
    _cache = []

    def __init__(self):
        logging.Handler.__init__(self)
        self._cache = []

    def emit(self, record):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self._cache.append(timestamp + " [" + record.levelname + "] " + record.msg)

    def flush(self):
        tmp = self._cache
        self._cache = []
        return tmp

    def get(self):
        return self._cache


class FilterBylevel(logging.Filter):

    def __init__(self, level):
        logging.Filter.__init__(self)
        self._level_to_filter = level

    def filter(self, record):
        if record.levelno < self._level_to_filter:
            return True
        return False


class Logger(object):
    _buffer = None
    _module = None
    _scenario = None
    _browser_name = None
    _language = None

    def __init__(self, name=None, module=None, scenario=None,
                 browser_name=None, language=None):
        self._module = module
        self._scenario = scenario
        self._browser_name = browser_name
        self._language = language
        FORMAT = '%(asctime)s [%(levelname)s] %(message)s'
        if name == None:
            self._logger = logging.getLogger('stdout')
        else:
            self._logger = logging.getLogger(name)
        log_level = logging.DEBUG
        if Configuration().log_level.upper() == 'INFO':
            log_level = logging.INFO
        if Configuration().log_level.upper() == 'WARNING':
            log_level = logging.WARNING
        formatter = logging.Formatter(FORMAT)
        self._logger.setLevel(log_level)
        SUCCESS_NUM = 60
        FAILURE_NUM = 70
        logging.addLevelName(SUCCESS_NUM, "SUCCESS")

        def success(self, message, *args, **kws):
            self._log(SUCCESS_NUM, message, args, **kws)
        logging.Logger.success = success
        logging.addLevelName(FAILURE_NUM, "FAILURE")

        def failure(self, message, *args, **kws):
            self._log(FAILURE_NUM, message, args, **kws)
        logging.Logger.failure = failure
        self._buffer = BufferHandler()
        self._logger.addHandler(self._buffer)
        log_level_to_split = logging.WARNING
        eh = logging.StreamHandler(sys.stderr)
        eh.setLevel(log_level_to_split)
        eh.setFormatter(formatter)
        self._logger.addHandler(eh)
        nh = logging.StreamHandler(sys.stdout)
        nh.setLevel(log_level)
        nh.addFilter(FilterBylevel(log_level_to_split))
        nh.setFormatter(formatter)
        self._logger.addHandler(nh)
        
    def add_info_to_message(self, message):
        config = Configuration()
        if config.function_test != None:
            message = "[" + str(config.browser) + "] " + str(config.datasets_file_name).replace("'","") + " [" + str(config.function_test) + "] " + message
        else:
            message = "[" + str(config.browser) + "] " + str(config.datasets_file_name).replace("'","") + " [" + str(config._fct_test) + "] " + message
        return message

    def debug(self, message):
        message = self.add_info_to_message(message)
        self._logger.debug(message)

    def warning(self, message):
        message = self.add_info_to_message(message)
        self._logger.warning(message)

    def info(self, message):
        message = self.add_info_to_message(message)
        self._logger.info(message)

    def error(self, message):
        message = self.add_info_to_message(message)
        self._logger.error(message)

    def success(self, message):
        message = self.add_info_to_message(message)
        self._logger.success(message)

    def failure(self, message):
        message = self.add_info_to_message(message)
        self._logger.failure(message)

    def cache(self):
        return "\n".join(self._buffer.get())

    def flush(self):
        self._buffer.flush()
        self._module = None
        self._scenario = None

    @property
    def module(self):
        return self._module
    @module.setter
    def module(self, value):
        self._module = value

    @property
    def scenario(self):
        return self._scenario
    @scenario.setter
    def scenario(self, value):
        self._scenario = value
