# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtCore import QCoreApplication

from bin.ui_view.base.table_widget_base import TableWidgetBase
from lib.communicate import communicate

_translate = QCoreApplication.translate

"""
日志信息模块
"""


class LogTableWidgetUI(TableWidgetBase):
    def __init__(self):
        super().__init__()
        # self.headers_us = ["Id", "Date", "Type", "Message"]
        # noinspection PyArgumentList
        self.headers_title = [
            _translate("LogInfoUI", "Id"),
            _translate("LogInfoUI", "日期"),
            _translate("LogInfoUI", "类型"),
            _translate("LogInfoUI", "信息"),
        ]
        self.header_width = [60, 150, 80]

    def setup_ui(self):
        super().setup_ui()
        # self.setMinimumHeight(200)

    def retranslate_ui(self):
        pass


class LogInfoUI(object):
    def __new__(cls, *args, **kwargs) -> object:
        if not hasattr(cls, "_instance"):  # 反射
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, tab_widget: QTabWidget):
        """
        日志UI
        :param tab_widget:
        """
        if not hasattr(self, "_init_flag"):  # 反射
            self._init_flag = True  # 只初始化一次

            self.tab_widget = tab_widget
            self.log_tab = LogTableWidgetUI()

    def setup_ui(self) -> None:
        self.log_tab.setObjectName("tab")
        self.tab_widget.addTab(self.log_tab, "")

        self.log_tab.setup_ui()

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.log_tab), _translate("ToolsExtensionView", "日志信息"))


class LogInfoConnect(object):
    def __init__(self, log_ui: LogInfoUI):
        self.log_ui = log_ui

        self.log_tab = self.log_ui.log_tab

    def get_object(self):
        pass

    def setup_ui(self) -> None:
        self.communicate_connect()

    def communicate_connect(self) -> None:
        # 日志信息
        communicate.log_info.connect(self.log_info)

    def log_info(self, message: str):
        """
        日志解析写入至表格
        :param message:
        :return:
        """
        info_list = [item for item in message.split(" - ")]
        info_list.insert(0, "")
        self.log_tab.add_data2(info_list)
        self.log_tab.scrollToBottom()  # 最后一行

    def retranslate_ui(self) -> None:
        pass
