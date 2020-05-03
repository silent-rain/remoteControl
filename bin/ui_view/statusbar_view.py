# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QStatusBar, QMainWindow
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication

_translate = QCoreApplication.translate


class StatusbarUI(object):
    def __init__(self, main_window: QMainWindow):
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

    def retranslate_ui(self) -> None:
        super().retranslate_ui()
