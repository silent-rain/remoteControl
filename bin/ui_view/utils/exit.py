# -*- coding: utf-8 -*-
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QToolBar, QAction

from lib import settings

_translate = QCoreApplication.translate

"""
退出程序
"""


class ExitUI(object):
    def __init__(self, toolbar: QToolBar):
        self.toolbar = toolbar

        self.exit = QAction(QIcon(settings.MENUBAR_UI["exit"]), "退出程序", self.toolbar)

    def setup_ui(self):
        self.exit.setToolTip("退出程序")
        self.exit.triggered.connect(self.exit_receive)
        self.toolbar.addAction(self.exit)

    def exit_receive(self):
        print("exit_receive")

    def retranslate_ui(self):
        # noinspection PyArgumentList
        self.exit.setText(_translate("ToolbarUI", "退出程序"))
