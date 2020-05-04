# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QStatusBar, QMainWindow
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication

from lib import settings

_translate = QCoreApplication.translate


class StatusbarUI(object):
    def __new__(cls, *args, **kwargs) -> object:
        if not hasattr(cls, "_instance"):  # 反射
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, main_window: QMainWindow):
        if not hasattr(self, "_init_flag"):  # 反射
            self._init_flag = True  # 只初始化一次
            self.main_window = main_window
            self.statusbar = QStatusBar(self.main_window)

    def setup_ui(self) -> None:
        font = QFont()
        font.setPointSize(10)
        self.statusbar.setFont(font)

        # self.statusbar.setGeometry(QtCore.QRect(0, 0, 900, 50))
        # self.statusbar.setFixedHeight(30)
        self.statusbar.setObjectName("statusbar")
        self.main_window.setStatusBar(self.statusbar)

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.statusbar.setWindowTitle(_translate("StatusbarUI", "状态栏"))


class StatusbarView(StatusbarUI):
    def setup_ui(self) -> None:
        super().setup_ui()

        if not settings.STATUSBAR_SHOW:
            self.statusbar.hide()

    def retranslate_ui(self) -> None:
        super().retranslate_ui()
