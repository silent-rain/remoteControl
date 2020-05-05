# -*- coding: utf-8 -*-
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QToolBar, QAction

from lib import settings

_translate = QCoreApplication.translate

"""
文件管理
"""


class FileManagerUI(object):
    def __init__(self, toolbar: QToolBar):
        self.toolbar = toolbar

        self.file_manager = QAction(QIcon(settings.TOOLBAR_UI["file"]), "文件管理", self.toolbar)

    def setup_ui(self):
        self.file_manager.setToolTip("文件管理")
        self.file_manager.triggered.connect(self.file_manager_receive)
        self.toolbar.addAction(self.file_manager)

    def file_manager_receive(self):
        print("file_manager_receive")

    def retranslate_ui(self):
        # noinspection PyArgumentList
        self.file_manager.setText(_translate("ToolbarUI", "文件管理"))
