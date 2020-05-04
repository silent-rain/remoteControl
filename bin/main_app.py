# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

from bin.ui_view.main_window import MainWindowView
from bin.ui_view.toolbar import ToolbarView
from bin.ui_view.statusbar import StatusbarView
from bin.ui_view.menubar import MenubarView
from bin.ui_view.tools_extension.tools_extension import ToolsExtensionView


class MainView(object):
    def __init__(self, main_window: QMainWindow):
        """
        外观模式
        :param main_window:
        """
        self.main_window = main_window
        self.ui_view_list = []

    def add_ui_view(self, view: object) -> None:
        if view not in self.ui_view_list:
            self.ui_view_list.append(view)

    def setup_ui(self) -> None:
        self.add_ui_view(MainWindowView(self.main_window))  # 主窗口
        self.add_ui_view(MenubarView(self.main_window))  # 菜单栏
        self.add_ui_view(ToolbarView(self.main_window))  # 工具导航
        self.add_ui_view(ToolsExtensionView(self.main_window))  # 工具扩展
        self.add_ui_view(StatusbarView(self.main_window))  # 状态栏

        for view in self.ui_view_list:
            view.setup_ui()
            view.retranslate_ui()


class MainApp(object):
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = QMainWindow(None, Qt.WindowFlags())

        self.main_ui = MainView(self.main_window)

    def setup_ui(self) -> None:
        self.main_ui.setup_ui()

    def main(self) -> None:
        self.setup_ui()
        self.main_window.show()
        sys.exit(self.app.exec_())
