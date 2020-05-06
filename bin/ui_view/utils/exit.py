# -*- coding: utf-8 -*-
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QToolBar, QAction, QMainWindow

from lib import settings

_translate = QCoreApplication.translate

"""
退出程序
"""


class ExitUI(object):
    def __init__(self, toolbar: QToolBar, main_window: QMainWindow):
        self.toolbar = toolbar
        self.main_window = main_window

        self.exit = QAction(QIcon(settings.MENUBAR_UI["exit"]), "退出程序", self.toolbar)

    def setup_ui(self):
        self.exit.setToolTip("退出程序")
        self.exit.triggered.connect(self.exit_receive)
        self.toolbar.addAction(self.exit)

    def exit_receive(self):
        """
        退出程序
        :return:
        """
        self.main_window.close()

    def retranslate_ui(self):
        # noinspection PyArgumentList
        self.exit.setText(_translate("ToolbarUI", "退出程序"))
