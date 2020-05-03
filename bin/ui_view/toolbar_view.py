# -*- coding: utf-8 -*-
from PyQt5.QtCore import QSize, Qt, QCoreApplication
from PyQt5.QtWidgets import QToolBar, QMainWindow

_translate = QCoreApplication.translate


# noinspection PyArgumentList
class ToolbarUI(object):
    def __init__(self, main_window: QMainWindow):
        self.main_window = main_window

        self.toolBar = QToolBar(self.main_window)

    def setup_ui(self) -> None:
        self.toolBar.setObjectName("toolBar")

        # 设置 QToolBar 图标大小
        self.toolBar.setIconSize(QSize(50, 50))

        # 字体在右边
        # self.tools_main.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        # 字体在下面
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        # 窗口添加工具栏
        self.main_window.addToolBar(Qt.TopToolBarArea, self.toolBar)

    def retranslate_ui(self) -> None:
        self.toolBar.setWindowTitle(_translate("ToolbarUI", "工具导航"))


class ToolbarView(ToolbarUI):
    def setup_ui(self) -> None:
        super().setup_ui()

    def retranslate_ui(self) -> None:
        super().retranslate_ui()
