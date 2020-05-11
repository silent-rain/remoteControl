# -*- coding: utf-8 -*-
from PyQt5.QtGui import QIcon, QCloseEvent
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QMessageBox
from PyQt5.QtCore import QCoreApplication, QMetaObject

from lib import settings
from lib.communicate import communicate

_translate = QCoreApplication.translate

"""
主窗口模块
"""


class MainWindowUI(object):
    def __init__(self, main_window: QMainWindow):
        """
        主窗口
        :param main_window:
        """
        self.main_window = main_window

    def setup_ui(self) -> None:
        self.main_window.setObjectName("main_window")
        self.main_window.resize(850, 500)

        # noinspection PyArgumentList,PyCallByClass
        QMetaObject.connectSlotsByName(self.main_window)

        self.set_window_icon()
        self.center()

        # 隐藏工具栏上的右键菜单
        # self.main_window.setContextMenuPolicy(Qt.NoContextMenu)

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.main_window.setWindowTitle(_translate("MainWindowUI", "远程协助"))

    def set_window_icon(self) -> None:
        """
        设置窗口的图标
        引用资源 qtResource.py
        :return:
        """
        self.main_window.setWindowIcon(QIcon(settings.MAIN_UI["app"]))

    def center(self) -> None:
        """
        控制窗口显示在屏幕中心
        :return:
        """
        # 获得窗口
        qr = self.main_window.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.main_window.move(qr.topLeft())


class MainWindowConnect(object):
    def __init__(self, main_window_ui: MainWindowUI):
        """
        主窗口信号
        :param main_window_ui:
        """
        self.main_window_ui = main_window_ui

    def setup_ui(self) -> None:
        self.communicate_connect()

        # 主窗口关闭 事件
        self.main_window_ui.main_window.closeEvent = self.close_event

    def communicate_connect(self) -> None:
        pass

    def close_event(self, event: QCloseEvent) -> None:
        """
        主窗口重置退出事件
        退出消息提示框
        直接继承main_window的背景色
        :param event:
        :return:
        """
        message_box = QMessageBox(self.main_window_ui.main_window)
        # noinspection PyArgumentList
        reply = message_box.information(
            self.main_window_ui.main_window,
            _translate("MainWindowUI", "温馨提示"),
            _translate("MainWindowUI", "您确认要退出???"),
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )
        if reply == QMessageBox.Yes:
            communicate.start_server.emit(False)  # 程序退出后关闭服务器
            communicate.log_info.emit("系统信息 - 正在关闭服务器...")
            communicate.log_info.emit("系统信息 - 程序退出...")
            event.accept()
        else:
            event.ignore()

    def retranslate_ui(self) -> None:
        pass
