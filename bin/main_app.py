# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import Qt, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow

from bin.ui_view.main_ui import MainWindowView
from bin.ui_view.toolbar_view import ToolbarView
from bin.ui_view.statusbar_view import StatusbarView
from bin.ui_view.menubar_view import MenubarView


class MainView(object):
    def __init__(self, main_window: QMainWindow):
        """
        外观模式
        :param main_window:
        """
        self.main_window = main_window
        self.ui_view_list = []

    def add_ui_view(self, view: object) -> None:
        self.ui_view_list.append(view)

    @staticmethod
    def setup_ui(view: QObject) -> None:
        view.setup_ui()

    @staticmethod
    def retranslate_ui(view: QObject) -> None:
        view.retranslate_ui()

    def middleware(self) -> None:
        """
        中间层
        :return:
        """
        self.add_ui_view(MainWindowView(self.main_window))  # 主窗口
        self.add_ui_view(ToolbarView(self.main_window))  # 工具栏
        self.add_ui_view(StatusbarView(self.main_window))  # 状态栏
        self.add_ui_view(MenubarView(self.main_window))  # 菜单栏

    def main(self) -> None:
        self.middleware()

        for view in self.ui_view_list:
            view.setup_ui()
            view.retranslate_ui()


class MainApp(object):
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = QMainWindow(None, Qt.WindowFlags())

        self.main_ui = MainView(self.main_window)

    def setup_ui(self) -> None:
        self.main_ui.main()

    def main(self) -> None:
        self.setup_ui()
        self.main_window.show()
        sys.exit(self.app.exec_())


if __name__ == '__main__':
    app = MainApp()
    app.main()
