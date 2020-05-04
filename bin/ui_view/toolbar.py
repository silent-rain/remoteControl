# -*- coding: utf-8 -*-
from PyQt5.QtCore import QSize, Qt, QCoreApplication
from PyQt5.QtWidgets import QToolBar, QMainWindow

from lib import settings

_translate = QCoreApplication.translate


# noinspection PyArgumentList
class ToolbarUI(object):
    def __new__(cls, *args, **kwargs) -> object:
        if not hasattr(cls, "_instance"):  # 反射
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, main_window: QMainWindow):
        if not hasattr(self, "_init_flag"):  # 反射
            self._init_flag = True  # 只初始化一次
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

        if not settings.TOOLBAR_SHOW:
            self.toolBar.hide()

    def retranslate_ui(self) -> None:
        super().retranslate_ui()
