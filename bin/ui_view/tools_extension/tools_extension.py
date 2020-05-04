# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget, QDockWidget, QHBoxLayout, QTabWidget, QMainWindow
from PyQt5.QtCore import Qt, QCoreApplication, QRect, QSize

from bin.ui_view.tools_extension.loginfo import LOGInfo
from bin.ui_view.tools_extension.batch_operation import BatchOperation
from lib import settings
from lib.communicate import communicate

_translate = QCoreApplication.translate

"""
工具栏扩展模块
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
        self.dock_widget_contents = QWidget(self.main_window, Qt.WindowFlags())

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

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.dock_widget.setWindowTitle(_translate("ToolsExtensionView", "工具扩展"))


class ToolsExtensionView(BaseDockOne):
    def __init__(self, main_window):
        super().__init__(main_window)

        self.tab_widget = QTabWidget(self.layout_widget)
        self.tab_widget.setCurrentIndex(1)

        # noinspection PyArgumentList
        self.layout.addWidget(self.tab_widget)

        self.ui_view_list = []

    def add_ui_view(self, view: object) -> None:
        if view not in self.ui_view_list:
            self.ui_view_list.append(view)

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

        # self.dock_widget.setGeometry(QRect(0, 0, 850, 200))
        # self.tab_widget.resize(850, 200)
        # self.tab_widget.setGeometry(QRect(0, 0, 850, 200))
        self.dock_widget.size = QSize(850, 200)

        if not settings.TOOLS_EXTENSION_SHOW:
            self.dock_widget.hide()

    def setup_ui(self) -> None:
        super().setup_ui()
        self.options()

        self.add_ui_view(LOGInfo(self.tab_widget))  # 日志信息
        self.add_ui_view(BatchOperation(self.tab_widget))  # 批量操作

        for view in self.ui_view_list:
            view.setup_ui()
            view.retranslate_ui()

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        super().retranslate_ui()

    def communicate_connect(self):
        communicate.tools_extension_show.connect(self.tools_extension_show_receive)

    def tools_extension_show_receive(self, flag):
        print(flag)
