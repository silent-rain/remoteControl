# -*- coding: utf-8 -*-
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QToolBar, QAction

from lib import settings

_translate = QCoreApplication.translate

"""
远程终端
"""


class TerminalUI(object):
    def __init__(self, toolbar: QToolBar):
        self.toolbar = toolbar

        self.terminal = QAction(QIcon(settings.TOOLBAR_UI["terminal"]), "远程终端", self.toolbar)

    def setup_ui(self):
        self.terminal.setToolTip("远程终端")
        self.terminal.triggered.connect(self.terminal_receive)
        self.toolbar.addAction(self.terminal)

    def terminal_receive(self):
        print("terminal_receive")

    def retranslate_ui(self):
        # noinspection PyArgumentList
        self.terminal.setText(_translate("ToolbarUI", "远程终端"))
