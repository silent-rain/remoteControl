# coding: utf-8
import logging


class CustomQtSignalHandler(logging.StreamHandler):
    def __init__(self):
        super().__init__()

    def emit(self, record: logging.LogRecord) -> None:
        # logging.StreamHandler.emit(self, record)
        msg = self.format(record)
        print(msg)
        # for item in dir(record):
        #     if not item.startswith("_"):
        #         message = eval("record.{}".format(item))
        #         print("item: {}    {}".format(item,message))

    def emit1(self, record):
        message = record.message
        message = message.split("---")
        print(message)


# logger = logging.getLogger()
# handler = LoggerHandlerToMysql()
# logger.addHandler(handler)
#
# logger.debug("asdasds")


# 因为它是会默认传播到祖先logger
logger = logging.getLogger('apps')
logger.setLevel(logging.DEBUG)
# 是否传播这个日志到祖先logger, 如果设置了False 就不会传到root logger(祖先Logger)的
# 默认StreamHandler那里， 也就是不会打印在页面上
logger.propagate = False
# 添加handler, 决定日志落地到哪里，可以多个
# 这个是记录在文件的Handler
# apps_handler = logging.FileHandler(filename="apps.log")
apps_handler = CustomQtSignalHandler()
# 设置这个handler的处理格式， 实例化一个Formatter对象
# apps_formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
apps_formatter = logging.Formatter('%(asctime)s -- %(levelname)s -- %(message)s')
apps_handler.setFormatter(apps_formatter)
logger.addHandler(apps_handler)
# 日志会打印到apps.log, 并且不会输出到屏幕（如果logger.propagate=True就会）
logger.debug('shit')
