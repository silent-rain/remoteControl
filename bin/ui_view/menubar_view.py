# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMenuBar, QMainWindow
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication

_translate = QCoreApplication.translate


class MenubarUI(object):
    def __init__(self, main_window: QMainWindow):
        self.main_window = main_window
        self.menubar = QMenuBar(main_window)

    def setup_ui(self) -> None:
        font = QFont()
        font.setPointSize(10)
        self.menubar.setFont(font)

        # self.menubar.setGeometry(QRect(0, 0, 800, 25))
        self.menubar.setFixedHeight(30)
        self.menubar.setObjectName("menubar")
        self.main_window.setMenuBar(self.menubar)

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.menubar.setWindowTitle(_translate("MenubarUI", "菜单栏"))


class MenubarView(MenubarUI):
    def setup_ui(self) -> None:
        super().setup_ui()

    def retranslate_ui(self) -> None:
        super().retranslate_ui()
