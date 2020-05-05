# -*- coding: utf-8 -*-
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QToolBar, QAction

from lib import settings

_translate = QCoreApplication.translate

"""
语音监控
"""


class VoiceMonitorUI(object):
    def __init__(self, toolbar: QToolBar):
        self.toolbar = toolbar

        self.voice_monitor = QAction(QIcon(settings.TOOLBAR_UI["voice"]), "语音监控", self.toolbar)

    def setup_ui(self):
        self.voice_monitor.setToolTip("语音监控")
        self.voice_monitor.triggered.connect(self.voice_monitor_receive)
        self.toolbar.addAction(self.voice_monitor)

    def voice_monitor_receive(self):
        print("voice_monitor_receive")

    def retranslate_ui(self):
        # noinspection PyArgumentList
        self.voice_monitor.setText(_translate("ToolbarUI", "语音监控"))
