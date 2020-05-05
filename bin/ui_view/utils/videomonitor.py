# -*- coding: utf-8 -*-
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QToolBar, QAction

from lib import settings

_translate = QCoreApplication.translate

"""
视频监控
"""


class VideoMonitorUI(object):
    def __init__(self, toolbar: QToolBar):
        self.toolbar = toolbar

        self.video_monitor = QAction(QIcon(settings.TOOLBAR_UI["video"]), "视频监控", self.toolbar)

    def setup_ui(self):
        self.video_monitor.setToolTip("视频监控")
        self.video_monitor.triggered.connect(self.video_monitor_receive)
        self.toolbar.addAction(self.video_monitor)

    def video_monitor_receive(self):
        print("video_monitor_receive")

    def retranslate_ui(self):
        # noinspection PyArgumentList
        self.video_monitor.setText(_translate("ToolbarUI", "视频监控"))
