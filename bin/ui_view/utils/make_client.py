# -*- coding: utf-8 -*-
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QToolBar, QAction

from lib import settings

_translate = QCoreApplication.translate

"""
创建客户端
"""


class MakeClientUI(object):
    def __init__(self, toolbar: QToolBar):
        self.toolbar = toolbar

        self.make_client = QAction(QIcon(settings.MENUBAR_UI["make_server"]), "创建客户端", self.toolbar)

    def setup_ui(self):
        self.make_client.setToolTip("创建客户端")
        self.make_client.triggered.connect(self.make_client_receive)
        self.toolbar.addAction(self.make_client)

    def make_client_receive(self):
        print("make_client_receive")

    def retranslate_ui(self):
        # noinspection PyArgumentList
        self.make_client.setText(_translate("ToolbarUI", "创建客户端"))
