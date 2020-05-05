# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget, QDockWidget, QHBoxLayout, QTabWidget, QMainWindow
from PyQt5.QtCore import Qt, QCoreApplication, QSize

from bin.ui_view.tools_extension.loginfo import LOGInfo
from bin.ui_view.tools_extension.batch_operation import BatchOperation
from bin.ui_view.utils import load_animation
from lib import settings

_translate = QCoreApplication.translate

"""
工具栏扩展
"""


class BaseDockOne(object):
    def __init__(self, main_window: QMainWindow):
        """
        单一QDockWidget布局
        :param main_window:
        """
        self.main_window = main_window

        # QDockWidget
        self.dock_widget = QDockWidget(self.main_window)
        self.dock_widget_contents = QWidget(self.dock_widget, Qt.WindowFlags())

        # QHBoxLayout
        self.layout_widget = QWidget(self.dock_widget_contents, Qt.WindowFlags())
        self.layout = QHBoxLayout(self.layout_widget)

    @staticmethod
    def size_hint():
        """
        在这里定义dock的初始大小
        :return:
        """
        return QSize(850, 180)

    def setup_ui(self) -> None:
        self.dock_widget.setObjectName("dock_widget")
        self.dock_widget_contents.setObjectName("dock_widget_contents")
        self.layout_widget.setObjectName("layout_widget")
        self.layout.setObjectName("layout")

        self.layout.setContentsMargins(0, 0, 0, 0)

        # 初始化QDockWidget的高度
        self.dock_widget_contents.sizeHint = self.size_hint

        self.dock_widget_contents.setLayout(self.layout)
        self.dock_widget.setWidget(self.dock_widget_contents)

        # MainWindow.addDockWidget(Qt.DockWidgetArea(8), self.dock_widget)
        self.main_window.addDockWidget(Qt.BottomDockWidgetArea, self.dock_widget)

        # QDockWidget 位置发生变动
        self.dock_widget.dockLocationChanged.connect(self.set_window_transparent)

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.dock_widget.setWindowTitle(_translate("ToolsExtensionView", "工具扩展"))

    def set_window_transparent(self, event: Qt.DockWidgetArea) -> None:
        if settings.LOAD_EFFECT_ON:
            load_animation.load_animation(self.dock_widget)


class ToolsExtensionView(BaseDockOne):
    def __init__(self, main_window):
        super().__init__(main_window)

        self.tab_widget = QTabWidget(self.layout_widget)

        self.ui_view_list = []

    def add_ui_view(self, view: object) -> None:
        if view not in self.ui_view_list:
            self.ui_view_list.append(view)

    def load_ui(self) -> None:
        """
        加载模块
        :return:
        """
        self.add_ui_view(LOGInfo(self.tab_widget))  # 日志信息
        self.add_ui_view(BatchOperation(self.tab_widget))  # 批量操作

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

        if not settings.TOOLS_EXTENSION_SHOW:
            self.dock_widget.hide()

    def setup_ui(self) -> None:
        super().setup_ui()

        self.tab_widget.setCurrentIndex(1)
        # noinspection PyArgumentList
        self.layout.addWidget(self.tab_widget)

        self.options()

        # 窗口移动事件重写
        # self.dock_widget.moveEvent = self.move_event

        self.load_ui()
        self.show_ui()

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        super().retranslate_ui()
