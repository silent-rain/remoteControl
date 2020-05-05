# -*- coding: utf-8 -*-
from PyQt5.QtCore import QSize, Qt, QCoreApplication
from PyQt5.QtGui import QHideEvent
from PyQt5.QtWidgets import QToolBar, QMainWindow

from lib import settings
from lib.communicate import communicate

_translate = QCoreApplication.translate

"""
工具导航 ToolbarView
"""


class ToolbarUI(object):
    def __new__(cls, *args, **kwargs) -> object:
        if not hasattr(cls, "_instance"):  # 反射
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, main_window: QMainWindow):
        if not hasattr(self, "_init_flag"):  # 反射
            self._init_flag = True  # 只初始化一次
            self.main_window = main_window
            self.toolbar = QToolBar(self.main_window)

    def options(self) -> None:
        # 设置 QToolBar 图标大小
        self.toolbar.setIconSize(QSize(50, 50))

        # 字体在右边
        # self.tools_main.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        # 字体在下面
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        # 窗口添加工具栏
        self.main_window.addToolBar(Qt.TopToolBarArea, self.toolbar)

    def setup_ui(self) -> None:
        self.toolbar.setObjectName("toolBar")

        self.options()

        if not settings.TOOLBAR_SHOW:
            self.toolbar.hide()

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.toolbar.setWindowTitle(_translate("ToolbarUI", "工具导航"))


class ToolbarConnect(object):
    def __init__(self, main_window: QMainWindow):
        self.main_window = main_window

        self.toolbar_ui = ToolbarUI(self.main_window)
        self.toolbar = self.toolbar_ui.toolbar

    def setup_ui(self) -> None:
        self.communicate_connect()
        self.toolbar.hideEvent = self.hide_event
        self.toolbar.showEvent = self.hide_event

    def communicate_connect(self) -> None:
        # 工具栏是否显示
        communicate.toolbar_show.connect(self.toolbar_show)

    def toolbar_show(self, flag: bool) -> None:
        if flag:
            # 显示
            self.toolbar.setHidden(False)
        else:
            # 隐藏
            self.toolbar.setHidden(True)

    def hide_event(self, event: QHideEvent):
        """
        菜单栏中的  工具导航
        :param event:
        :return:
        """
        if event:
            pass
        if self.toolbar.isHidden():
            communicate.toolbar_checked.emit(False)
        else:
            communicate.toolbar_checked.emit(True)

    def retranslate_ui(self) -> None:
        pass
