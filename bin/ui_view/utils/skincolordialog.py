# -*- coding: utf-8 -*-
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QColorDialog
from PyQt5.QtCore import QCoreApplication, Qt

_translate = QCoreApplication.translate


class SkinColorDialogView(object):
    def __init__(self, main_window):
        self.main_window = main_window

        self.widget_window = QWidget(main_window, Qt.WindowFlags())
        self.color_dialog = QColorDialog()

        self.col = None

    def show_dialog(self) -> None:
        if self.col.isValid():
            self.main_window.setStyleSheet('QWidget {background-color:%s}' % self.col.name())

    def setup_ui(self) -> None:
        self.widget_window.setGeometry(300, 300, 350, 80)
        self.widget_window.setWindowTitle('ColorDialog')
        self.widget_window.setFocus()  # 设置焦点

        # 颜色选取信号
        self.color_dialog.currentColorChanged.connect(self.show_dialog)

        # 获取颜色
        # noinspection PyCallByClass
        init_color = QColor(107, 173, 246)
        self.col = self.color_dialog.getColor(init_color, None)

        # print(dir(self.color_dialog))
        # print(dir(self.col))

        # color = QColor(0, 0, 0)
        # self.button = QPushButton(self.widget_window)
        # self.button.setFocusPolicy(Qt.NoFocus)
        # self.button.move(20, 20)
        # self.button.clicked.connect(self.show_dialog)
        # self.widget1 = QWidget(self.widget_window)
        # self.widget1.setStyleSheet('QWidget{background-color:%s}' % color.name())
        # self.widget1.setGeometry(130, 22, 100, 100)

    # noinspection PyArgumentList
    def retranslate_ui(self):
        self.widget_window.setWindowTitle(_translate("SkinColorDialogView", "皮肤调色板"))
