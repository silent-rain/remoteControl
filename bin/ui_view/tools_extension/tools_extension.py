# -*- coding: utf-8 -*-
from PyQt5.QtGui import QHideEvent
from PyQt5.QtWidgets import QTabWidget, QMainWindow
from PyQt5.QtCore import Qt, QCoreApplication

from bin.ui_view.tools_extension.loginfo import LogInfoUI, LogInfoConnect
from bin.ui_view.tools_extension.batch_operation import BatchOperationUI
from bin.ui_view.base.dock_widget_base import DockWidgetBase
from lib import settings
from lib.communicate import communicate

_translate = QCoreApplication.translate

"""
工具栏扩展
"""


class ToolsExtensionUI(DockWidgetBase):
    def __new__(cls, *args, **kwargs) -> object:
        if not hasattr(cls, "_instance"):  # 反射
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, main_window: QMainWindow):
        """
        工具扩展
        :param main_window:
        """
        if not hasattr(self, "_init_flag"):  # 反射
            super().__init__(main_window)
            self._init_flag = True  # 只初始化一次
            self.main_window = main_window

            self.tab_widget = QTabWidget(self.layout_widget)
            self.ui_view_list = []

    def add_ui(self, ui: object) -> None:
        """
        添加模块
        :param ui:
        :return:
        """
        if ui not in self.ui_view_list:
            self.ui_view_list.append(ui)

    def load_ui(self) -> None:
        """
        加载模块
        :return:
        """
        self.add_ui(LogInfoUI(self.tab_widget))  # 日志信息
        self.add_ui(BatchOperationUI(self.tab_widget))  # 批量操作

    def show_ui(self) -> None:
        """
        显示数据
        :return:
        """
        for view in self.ui_view_list:
            view.setup_ui()
            view.retranslate_ui()

    def options(self) -> None:
        """
        参数设置
        :return:
        """
        super().options()
        self.tab_widget.setObjectName("tab_widget")

        # 设置焦点
        self.tab_widget.setFocusPolicy(Qt.TabFocus)
        # tab其实位置
        self.tab_widget.setLayoutDirection(Qt.LeftToRight)

        # 全背景填充
        # self.tab_widget.setAutoFillBackground(False)
        # self.tab_widget.setStyleSheet("background-color: rgb(85, 170, 255);")

        # tab位置
        self.tab_widget.setTabPosition(QTabWidget.South)
        # tab选项样式
        self.tab_widget.setTabShape(QTabWidget.Rounded)
        # 是否可以关闭tab
        self.tab_widget.setTabsClosable(False)
        # 是否可以移动tab
        self.tab_widget.setMovable(False)
        # 隐藏tab
        self.tab_widget.setTabBarAutoHide(True)

        # self.tab_widget.resize(850, 200)
        # self.tab_widget.setGeometry(QRect(0, 0, 850, 200))

    def setup_ui(self) -> None:
        super().setup_ui()
        self.options()

        self.tab_widget.setCurrentIndex(1)
        # noinspection PyArgumentList
        self.layout.addWidget(self.tab_widget)

        # 窗口移动事件重写
        # self.dock_widget.moveEvent = self.move_event

        self.load_ui()
        self.show_ui()

        if not settings.TOOLS_EXTENSION_SHOW:
            # self.dock_widget.hide()
            self.dock_widget.setHidden(True)

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.dock_widget.setWindowTitle(_translate("ToolsExtensionUI", "工具扩展"))


class ToolsExtensionConnect(object):
    def __init__(self, main_window: QMainWindow):
        self.main_window = main_window

        self.dock_widget_ui = ToolsExtensionUI(self.main_window)
        self.dock_widget = self.dock_widget_ui.dock_widget

        # 工具扩展子类信号
        self.ui_connect_list = []

    def setup_ui(self) -> None:
        self.communicate_connect()

        self.dock_widget.hideEvent = self.hide_event
        self.dock_widget.showEvent = self.hide_event

        self.load_connect()
        self.show_connect()

    def communicate_connect(self) -> None:
        # 状态栏是否显示
        communicate.tools_extension_show.connect(self.tools_extension_show)

    def tools_extension_show(self, flag: bool) -> None:
        if flag:
            # 显示
            self.dock_widget.setHidden(False)
        else:
            # 隐藏
            self.dock_widget.setHidden(True)

    def hide_event(self, event: QHideEvent):
        """
        菜单栏中的  工具扩展
        :param event:
        :return:
        """
        if event:
            pass
        if self.dock_widget.isHidden():
            communicate.tools_extension_checked.emit(False)
        else:
            communicate.tools_extension_checked.emit(True)

    def retranslate_ui(self) -> None:
        pass

    def add_connect(self, ui: object) -> None:
        """
        添加模块
        :param ui:
        :return:
        """
        if ui not in self.ui_connect_list:
            self.ui_connect_list.append(ui)

    def load_connect(self) -> None:
        """
        加载模块
        :return:
        """
        self.add_connect(LogInfoConnect(LogInfoUI(self.dock_widget)))  # 日志信号链接

    def show_connect(self) -> None:
        """
        显示数据
        :return:
        """
        for view in self.ui_connect_list:
            view.setup_ui()
            view.retranslate_ui()
