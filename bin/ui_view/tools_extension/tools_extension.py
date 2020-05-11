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


class ToolsExtensionUI(object):
    def __init__(self, main_window: QMainWindow):
        """
        工具扩展
        外观模式
        :param main_window:
        """
        self.main_window = main_window

        self.dock_widget = DockWidgetBase(self.main_window)
        self.tab_widget = QTabWidget(self.dock_widget.widget_contents)

        self.ui_list = []
        self.log_info_ui = LogInfoUI(self.tab_widget)  # 日志信息
        self.batch_operation_ui = BatchOperationUI(self.tab_widget)  # 批量操作

    def load_ui(self) -> None:
        """
        加载模块
        :return:
        """
        self.ui_list.append(self.log_info_ui)
        self.ui_list.append(self.batch_operation_ui)

    def show_ui(self) -> None:
        """
        显示数据
        :return:
        """
        for view in self.ui_list:
            view.setup_ui()
            view.retranslate_ui()

    def options(self) -> None:
        """
        参数设置
        :return:
        """
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

        # 显示位置
        self.main_window.addDockWidget(Qt.BottomDockWidgetArea, self.dock_widget)

    def setup_ui(self) -> None:
        self.dock_widget.setup_ui()
        self.options()

        self.tab_widget.setCurrentIndex(1)
        # noinspection PyArgumentList
        self.dock_widget.layout.addWidget(self.tab_widget)

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
    def __init__(self, tools_extension_ui: ToolsExtensionUI):
        """
        工具栏扩展
        外观模式
        :param tools_extension_ui:
        """
        self.tools_extension_ui = tools_extension_ui

        # 工具扩展子类信号
        self.connect_list = []
        self.log_info_connect = LogInfoConnect(self.tools_extension_ui.log_info_ui)  # 日志信号

    def setup_ui(self) -> None:
        self.communicate_connect()

        self.tools_extension_ui.dock_widget.hideEvent = self.hide_event
        self.tools_extension_ui.dock_widget.showEvent = self.hide_event

        # 工具扩展子类信号
        self.load_connect()
        self.show_connect()

    def communicate_connect(self) -> None:
        # 状态栏是否显示
        communicate.tools_extension_show.connect(self.tools_extension_show)

    def tools_extension_show(self, flag: bool) -> None:
        if flag:
            # 显示
            self.tools_extension_ui.dock_widget.setHidden(False)
        else:
            # 隐藏
            self.tools_extension_ui.dock_widget.setHidden(True)

    def hide_event(self, event: QHideEvent) -> None:
        """
        菜单栏中的  工具扩展
        :param event:
        :return:
        """
        if event:
            pass
        if self.tools_extension_ui.dock_widget.isHidden():
            communicate.tools_extension_checked.emit(False)
        else:
            communicate.tools_extension_checked.emit(True)

    def retranslate_ui(self) -> None:
        pass

    def load_connect(self) -> None:
        """
        加载模块
        :return:
        """
        self.connect_list.append(self.log_info_connect)

    def show_connect(self) -> None:
        """
        显示数据
        :return:
        """
        for connect in self.connect_list:
            connect.setup_ui()
            connect.retranslate_ui()
