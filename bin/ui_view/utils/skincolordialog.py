# -*- coding: utf-8 -*-
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QColorDialog, QMainWindow
from PyQt5.QtCore import QCoreApplication

from lib import settings

_translate = QCoreApplication.translate

"""
皮肤调色模块
"""


class SkinColorDialogView(object):
    def __init__(self, main_window: QMainWindow):
        self.main_window = main_window

        # 初始化颜色
        self.color = QColor(*settings.SKIN_COLOR)
        # 创建颜色对话框--但不显示
        self.color_dialog = QColorDialog(self.color, self.main_window)

        # 创建调色板
        self.palette = QPalette()

    def update_color(self, event: QColor) -> None:
        """
        更新颜色
        两种方式同时
        :param event:
        :return:
        """
        # print(event, type(event))
        # print(self.color_dialog.selectedColor(), type(self.color_dialog.selectedColor()))

        # QPalette.Background   表示设置背景色
        # QPalette.WindowText  表示设置文本颜色
        self.palette.setColor(QPalette.Background, event)  # 给调色板设置颜色
        # self.palette.setColor(QPalette.Background, self.color_dialog.selectedColor())  # 给调色板设置颜色

        # 给控件设置颜色
        if event.isValid():
            self.main_window.setStyleSheet('QWidget {background-color:%s}' % event.name())
            self.main_window.setPalette(self.palette)

    def setup_ui(self) -> None:
        # 颜色选取信号
        # 会向槽函数传递一个值---QColor
        # self.color_dialog.colorSelected.connect(self.update_color)  # 选中最终颜色时发出信号-点击对话框的确定按钮时
        self.color_dialog.currentColorChanged.connect(self.update_color)  # 当前颜色变化时

        # self.cd.setOption(QColorDialog.NoButtons)  #选项控制--单个选项
        # QColorDialog.NoButtons   不显示“ 确定”和“ 取消”按钮。（对“实时对话框”有用）
        # QColorDialog.ShowAlphaChannel   对话框中增加alpha设置项
        self.color_dialog.setOptions(QColorDialog.NoButtons | QColorDialog.ShowAlphaChannel)  # 选项控制--多个选项

        # 打开对话框,获取颜色
        # noinspection PyCallByClass
        # self.color = self.color_dialog.getColor(self.color, None)

        # 打开对话框
        self.color_dialog.show()

    def retranslate_ui(self) -> None:
        pass
