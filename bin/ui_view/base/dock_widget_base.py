# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget, QDockWidget, QHBoxLayout, QMainWindow
from PyQt5.QtCore import Qt, QCoreApplication, QSize

from bin.ui_view.utils import load_animation
from lib import settings

_translate = QCoreApplication.translate

"""
QDockWidget 基类
"""


class DockWidgetBase2(object):
    def __init__(self, main_window: QMainWindow):
        """
        QDockWidget 基类
        :param main_window:
        """
        self.main_window = main_window

        # QDockWidget
        self.dock_widget = QDockWidget(self.main_window)
        self.widget_contents = QWidget(self.dock_widget, Qt.WindowFlags())

        # QHBoxLayout
        # self.layout_widget = QWidget(self.dock_widget_contents, Qt.WindowFlags())
        self.layout = QHBoxLayout(self.widget_contents)

    @staticmethod
    def size_hint() -> QSize:
        """
        在这里定义dock的初始大小
        :return:
        """
        return QSize(850, 100)

    def options(self) -> None:
        """
        参数设置
        :return:
        """
        self.dock_widget.setObjectName("dock_widget")
        self.widget_contents.setObjectName("dock_widget_contents")
        # self.layout_widget.setObjectName("layout_widget")
        self.layout.setObjectName("layout")

        self.layout.setContentsMargins(0, 0, 0, 0)

        self.widget_contents.setLayout(self.layout)
        self.dock_widget.setWidget(self.widget_contents)

        # 显示位置,子类进行设置
        # MainWindow.addDockWidget(Qt.DockWidgetArea(8), self.dock_widget)
        # self.main_window.addDockWidget(Qt.BottomDockWidgetArea, self.dock_widget)

    def setup_ui(self) -> None:
        self.options()

        # 初始化QDockWidget的高度
        self.widget_contents.sizeHint = self.size_hint

        # QDockWidget 位置发生变动
        self.dock_widget.dockLocationChanged.connect(self.dock_location_changed)

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.dock_widget.setWindowTitle(_translate("ToolsExtensionView", "工具扩展"))

    def dock_location_changed(self, event: Qt.DockWidgetArea) -> None:
        """
        QDockWidget 浮动事件
        :param event:
        :return:
        """
        if event:
            pass
        if settings.LOAD_EFFECT_ON:
            load_animation.load_animation(self.widget_contents)


class DockWidgetBase(QDockWidget):
    def __init__(self, main_window: QMainWindow):
        """
        QDockWidget 基类
        :param main_window:
        """
        super().__init__(main_window)

        # QDockWidget
        self.widget_contents = QWidget(self, Qt.WindowFlags())

        # QHBoxLayout
        self.layout = QHBoxLayout(self.widget_contents)

    @staticmethod
    def size_hint() -> QSize:
        """
        在这里定义dock的初始大小
        :return:
        """
        return QSize(850, 100)

    def options(self) -> None:
        """
        参数设置
        :return:
        """
        self.setObjectName("dock_widget")
        self.widget_contents.setObjectName("dock_widget_contents")
        self.layout.setObjectName("layout")

        self.layout.setContentsMargins(0, 0, 0, 0)

        self.widget_contents.setLayout(self.layout)
        self.setWidget(self.widget_contents)

        # 显示位置,子类进行设置
        # MainWindow.addDockWidget(Qt.DockWidgetArea(8), self)
        # self.main_window.addDockWidget(Qt.BottomDockWidgetArea, self)

    def setup_ui(self) -> None:
        self.options()

        # 初始化QDockWidget的高度
        self.widget_contents.sizeHint = self.size_hint

        # QDockWidget 位置发生变动
        self.dockLocationChanged.connect(self.dock_location_changed)

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.setWindowTitle(_translate("ToolsExtensionView", "工具扩展"))

    def dock_location_changed(self, event: Qt.DockWidgetArea) -> None:
        """
        QDockWidget 浮动事件
        :param event:
        :return:
        """
        if event:
            pass
        if settings.LOAD_EFFECT_ON:
            load_animation.load_animation(self.widget_contents)
