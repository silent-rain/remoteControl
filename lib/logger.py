# -*- coding: utf-8 -*-
import os
import logging.config
from logging import StreamHandler
from lib.settings import LOGGING_LEVEL, LOGGING_DIR, DEBUG
from lib.communicate import communicate


# 日志打印级别
# ;DEBUG/INFO/WARNING/ERROR/CRITICAL
# LOGGING_LEVEL = "DEBUG"
# 日志路径
# LOGGING_DIR = "logs"


class SingleLevelFilter(object):
    def __init__(self, pass_level):
        self.pass_level = pass_level

    def filter(self, record) -> bool:
        if self.pass_level == record.levelno:
            return True
        return False


class CustomQtSignalHandler(StreamHandler):
    def __init__(self):
        super().__init__()

    def emit(self, record: logging.LogRecord) -> None:
        # logging.StreamHandler.emit(self, record)
        msg = self.format(record)
        # print(msg)
        # for item in dir(record):
        #     if not item.startswith("_"):
        #         message = eval("record.{}".format(item))
        #         print("item: {}    {}".format(item, message))
        # asctime = record.asctime
        # levelname = record.levelname
        # msg = record.msg
        # print(asctime)
        # print(levelname)
        # print(msg)
        if communicate:
            communicate.log_info.emit(msg)


logging.CustomQtSignalHandler = CustomQtSignalHandler

logging_config = {
    # 必选项，其值是一个整数值，表示配置格式的版本，当前唯一可用的值就是1
    'version': 1,
    # 是否禁用现有的记录器
    'disable_existing_loggers': False,

    # 过滤器
    'filters': {
        'filter_single_level_debug': {
            '()': SingleLevelFilter,
            'pass_level': logging.DEBUG
        },
        'filter_single_level_info': {
            '()': SingleLevelFilter,
            'pass_level': logging.INFO
        },
        'filter_single_level_warning': {
            '()': SingleLevelFilter,
            'pass_level': logging.WARNING
        },
        'filter_single_level_error': {
            '()': SingleLevelFilter,
            'pass_level': logging.ERROR
        },
        'filter_single_level_critical': {
            '()': SingleLevelFilter,
            'pass_level': logging.CRITICAL
        },
    },

    # 日志格式集合
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': '%Y%b%d-%H:%M:%S',
            # "datefmt": '%a, %d %b %Y %H:%M:%S',
        },
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s] - %(message)s'
        },
        'qt_console': {
            'format': '%(asctime)s - %(message)s',
        },
    },

    # 处理器集合
    'handlers': {
        # 自定义: 输出到qt信号
        'qt_console': {
            # 'level': 'DEBUG',  # 输出信息的最低级别
            'level': LOGGING_LEVEL,  # 输出信息的最低级别
            # 'class': CustomQtSignalHandler,
            'class': "logging.CustomQtSignalHandler",
            'formatter': 'qt_console',  # 使用standard格式
            # 'filters': ['filter_single_level_debug', ],
            # "stream": "ext://sys.stdout"
        },

        # 输出到控制台
        'console': {
            # 'level': 'DEBUG',  # 输出信息的最低级别
            'level': LOGGING_LEVEL,  # 输出信息的最低级别
            'class': 'logging.StreamHandler',
            'formatter': 'simple',  # 使用standard格式
            # 'filters': ['filter_single_level_debug', ],
            # "stream": "ext://sys.stdout"
        },

        # 输出至 debug 文件
        "debug": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "DEBUG",  # 日志级别
            "formatter": "standard",  # 格式化
            "filename": os.path.join(LOGGING_DIR, "debug.log"),  # 文件
            "when": "midnight",  # 每天凌晨
            "interval": 1,  # 时间间隔
            "backupCount": 6,  # 备份文件的个数，如果超过这个个数，就会自动删除
            "encoding": 'utf-8',
            "filters": ['filter_single_level_debug', ],
        },
        # 输出至 info 文件
        "info": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "INFO",
            "formatter": "standard",
            "filename": os.path.join(LOGGING_DIR, "info.log"),
            "when": "midnight",
            "interval": 1,
            "backupCount": 6,
            "encoding": 'utf-8',
            "filters": ['filter_single_level_info', ],
        },
        # 输出至 warning 文件
        "warning": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "WARNING",
            "formatter": "standard",
            "filename": os.path.join(LOGGING_DIR, "warning.log"),
            "when": "midnight",
            "interval": 1,
            "backupCount": 6,
            "encoding": 'utf-8',
            "filters": ['filter_single_level_warning', ],
        },
        # 输出至 error 文件
        "error": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "ERROR",
            "formatter": "standard",
            "filename": os.path.join(LOGGING_DIR, "error.log"),
            "when": "midnight",
            "interval": 1,
            "backupCount": 6,
            "encoding": 'utf-8',
            "filters": ['filter_single_level_error', ],
        },
        # 输出至 critical 文件
        "critical": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "CRITICAL",
            "formatter": "standard",
            "filename": os.path.join(LOGGING_DIR, "critical.log"),
            "when": "midnight",
            "interval": 1,
            "backupCount": 6,
            "encoding": 'utf-8',
            "filters": ['filter_single_level_critical', ],
        },
        # 输出到文件
        'all': {
            # 'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            "filename": os.path.join(LOGGING_DIR, "all.log"),  # 输出位置
            'maxBytes': 1024 * 1024 * 5,  # 文件大小 5M
            'backupCount': 5,  # 备份份数
            'encoding': 'utf8',  # 文件编码
        },
    },

    # 日志管理器集合
    'loggers': {
        'root': {
            'handlers': ['debug', 'info', 'warning', 'error', 'critical', 'all', 'qt_console'],
            'level': 'DEBUG',
            'propagate': False,  # 是否传递给父记录器
        },
        # 需要实例化才能用
        'simple': {
            # 'handlers': ['console'],
            'handlers': ['qt_console', 'console'],
            'level': 'DEBUG',
            'propagate': False,  # 是否传递给父记录器,
        }
    },
}

logging.config.dictConfig(logging_config)
if DEBUG:
    logger = logging.getLogger('simple')
else:
    logger = logging.getLogger('root')

if __name__ == '__main__':
    # 尝试写入不同消息级别的日志信息
    logger.debug("debug message")
    # logger.info("info message")
    # logger.warning("warning message")
    # logger.error("error message")
    # logger.critical("critical message")
