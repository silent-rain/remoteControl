# -*- coding: utf-8 -*-
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QToolBar, QAction

from lib import settings

_translate = QCoreApplication.translate

"""
远程控制
"""


class RemoteControlUI(object):
    def __init__(self, toolbar: QToolBar):
        self.toolbar = toolbar

        self.remote_control = QAction(QIcon(settings.TOOLBAR_UI["desktop"]), "远程控制", self.toolbar)

    def setup_ui(self):
        self.remote_control.setToolTip("远程控制")
        self.remote_control.triggered.connect(self.remote_control_receive)
        self.toolbar.addAction(self.remote_control)

    def remote_control_receive(self):
        print("remote_control_receive")

    def retranslate_ui(self):
        # noinspection PyArgumentList
        self.remote_control.setText(_translate("ToolbarUI", "远程控制"))
