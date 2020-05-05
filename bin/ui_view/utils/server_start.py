# -*- coding: utf-8 -*-
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QToolBar, QAction

from lib import settings
from lib.logger import logger

_translate = QCoreApplication.translate

"""
服务器开关/启动/停止
remote_control
"""


class ServerStartUI(object):
    def __init__(self, toolbar: QToolBar):
        self.toolbar = toolbar

        self.start_stop = QAction(QIcon(settings.TOOLBAR_UI["start"]), "启动", self.toolbar)
        # 控制开关
        self.start_flag = False

    def setup_ui(self):
        self.start_stop.setToolTip("启动服务")
        self.start_stop.triggered.connect(self.start_stop_receive)
        self.toolbar.addAction(self.start_stop)

    # noinspection PyArgumentList
    def start_stop_receive(self):
        """
        启动/停止服务
        :return:
        """
        if self.start_flag:
            self.start_flag = False
            self.start_stop.setIcon(QIcon(settings.TOOLBAR_UI["start"]))
            self.start_stop.setText(_translate("ToolbarUI", "启动"))
            self.start_stop.setToolTip("启动服务")
            logger.info("系统信息 - 启动服务...")
        else:
            self.start_flag = True
            self.start_stop.setIcon(QIcon(settings.TOOLBAR_UI["stop"]))
            self.start_stop.setText(_translate("ToolbarUI", "停止"))
            self.start_stop.setToolTip("停止服务")
            logger.info("系统信息 - 停止服务...")
        print("启动/停止服务----信号未处理")

    def retranslate_ui(self):
        # noinspection PyArgumentList
        self.start_stop.setText(_translate("ToolbarUI", "启动"))
