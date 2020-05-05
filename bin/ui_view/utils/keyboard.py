# -*- coding: utf-8 -*-
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QToolBar, QAction

from lib import settings

_translate = QCoreApplication.translate

"""
键盘记录
"""


class KeyboardUI(object):
    def __init__(self, toolbar: QToolBar):
        self.toolbar = toolbar

        self.keyboard = QAction(QIcon(settings.TOOLBAR_UI["keyboard"]), "键盘记录", self.toolbar)

    def setup_ui(self):
        self.keyboard.setToolTip("键盘记录")
        self.keyboard.triggered.connect(self.keyboard_receive)
        self.toolbar.addAction(self.keyboard)

    def keyboard_receive(self):
        print("keyboard_receive")

    def retranslate_ui(self):
        # noinspection PyArgumentList
        self.keyboard.setText(_translate("ToolbarUI", "键盘记录"))
