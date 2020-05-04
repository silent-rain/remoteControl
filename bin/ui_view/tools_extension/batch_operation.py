# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget, QTabWidget
from PyQt5.QtCore import Qt, QCoreApplication

_translate = QCoreApplication.translate

"""
批量操作模块
"""


class BatchOperation(object):
    def __init__(self, tab_widget: QTabWidget):
        self.tab_widget = tab_widget

        self.tab = QWidget(self.tab_widget, Qt.WindowFlags())

    def setup_ui(self) -> None:
        self.tab.setObjectName("tab")
        self.tab_widget.addTab(self.tab, "")

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab), _translate("ToolsExtensionView", "批量操作"))
