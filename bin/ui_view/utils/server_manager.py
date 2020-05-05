# -*- coding: utf-8 -*-
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QToolBar, QAction

from lib import settings

_translate = QCoreApplication.translate

"""
服务管理/进程管理
"""


class ServiceManagerUI(object):
    def __init__(self, toolbar: QToolBar):
        self.toolbar = toolbar

        self.server_manager = QAction(QIcon(settings.TOOLBAR_UI["server"]), "服务管理", self.toolbar)

    def setup_ui(self):
        self.server_manager.setToolTip("服务管理/进程管理")
        self.server_manager.triggered.connect(self.server_manager_receive)
        self.toolbar.addAction(self.server_manager)

    def server_manager_receive(self):
        print("server_manager_receive")

    def retranslate_ui(self):
        # noinspection PyArgumentList
        self.server_manager.setText(_translate("ToolbarUI", "服务管理"))
