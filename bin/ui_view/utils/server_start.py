# -*- coding: utf-8 -*-
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QToolBar, QAction

from lib import settings
from lib.communicate import communicate

_translate = QCoreApplication.translate

"""
服务器开关/启动/停止
remote_control
"""


class ServerStartUI(object):
    def __init__(self, toolbar: QToolBar):
        self.toolbar = toolbar

        self.start_stop = QAction(QIcon(settings.TOOLBAR_UI["start"]), "启动", self.toolbar)

    def setup_ui(self):
        self.start_stop.setToolTip("启动服务")
        # self.start_stop.triggered.connect(self.start_stop_receive)
        self.toolbar.addAction(self.start_stop)

    def retranslate_ui(self):
        # noinspection PyArgumentList
        self.start_stop.setText(_translate("ToolbarUI", "启动"))


class ServerStartConnect(object):
    def __init__(self, server_start_ui: ServerStartUI):
        self.server_start_ui = server_start_ui

        # 控制开关
        self.start_flag = False

    def setup_ui(self) -> None:
        self.communicate_connect()
        self.server_start_ui.start_stop.triggered.connect(self.start_stop_receive)

    def communicate_connect(self) -> None:
        # 服务启动/停止, 初始化
        communicate.init_start_server.connect(self.init_start_server)
        # 服务异常停止
        communicate.start_server_error.connect(self.start_stop_receive)

    # noinspection PyArgumentList
    def start_stop_receive(self, event: bool) -> None:
        """
        启动/停止服务
        按钮
        :param event:
        :return:
        """
        if event:
            pass
        if self.start_flag:
            # 停止服务
            self.start_flag = False
            self.server_start_ui.start_stop.setIcon(QIcon(settings.TOOLBAR_UI["start"]))
            self.server_start_ui.start_stop.setText(_translate("ToolbarUI", "启动"))
            self.server_start_ui.start_stop.setToolTip("启动服务")
            communicate.start_server.emit(False)  # -> 服务器开关
        else:
            # 启动服务
            self.start_flag = True
            self.server_start_ui.start_stop.setIcon(QIcon(settings.TOOLBAR_UI["stop"]))
            self.server_start_ui.start_stop.setText(_translate("ToolbarUI", "停止"))
            self.server_start_ui.start_stop.setToolTip("停止服务")
            communicate.start_server.emit(True)  # -> 服务器开关

    # noinspection PyArgumentList
    def init_start_server(self, event: bool) -> None:
        """
        启动/停止服务
        初始化
        :return:
        """
        if event:
            # 启动服务
            self.start_flag = True
            self.server_start_ui.start_stop.setIcon(QIcon(settings.TOOLBAR_UI["stop"]))
            self.server_start_ui.start_stop.setText(_translate("ToolbarUI", "停止"))
            self.server_start_ui.start_stop.setToolTip("停止服务")
            communicate.start_server.emit(True)  # -> 服务器开关

    def retranslate_ui(self) -> None:
        pass
