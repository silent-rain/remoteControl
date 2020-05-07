# -*- coding: utf-8 -*-
from PyQt5.QtCore import QCoreApplication, QSize, Qt
from PyQt5.QtGui import QFont, QPixmap, QColor, QPalette
from PyQt5.QtWidgets import QWidget, QLabel, QTextEdit, QDesktopWidget, QGridLayout, QPushButton

from lib import settings

_translate = QCoreApplication.translate

"""
About 窗口
"""


class AboutUI(object):
    def __init__(self):
        """
        关于
        """
        self.layout_widget = QWidget(None, Qt.Dialog)
        self.layout = QGridLayout(self.layout_widget)

        self.label = QLabel(self.layout_widget)
        self.title = QLabel(self.layout_widget)
        self.text = QTextEdit(self.layout_widget)
        self.button = QPushButton(self.layout_widget)

        # 创建调色板
        self.palette = QPalette()
        # 颜色初始化
        # self.color_init = QColor(107, 173, 246)
        self.color_init = QColor(*settings.SKIN_COLOR)

    def set_window_background(self) -> None:
        """
        设置背景: 背景色
        :return:
        """
        # 整体背景
        # 如果设置背景色,透明失效
        # self.main_window.setStyleSheet("background-color: rgb(100, 200, 255);")
        # self.main_window.setStyleSheet("background-color: rgb(107, 173, 246);")
        self.layout_widget.setStyleSheet("background-color: rgb{};".format(self.color_init.getRgb()[:3]))

        # 给调色板设置颜色
        self.palette.setColor(QPalette.Background, self.color_init)
        self.layout_widget.setPalette(self.palette)  # 给控件设置颜色

    def center(self) -> None:
        """
        控制窗口显示在主窗口中心
        :return:
        """
        # 获得窗口
        qr = self.layout_widget.frameGeometry()

        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.layout_widget.move(qr.topLeft())

    def show(self) -> None:
        """
        显示窗口
        :return:
        """
        self.layout_widget.show()

    def setup_ui(self) -> None:
        self.center()
        self.set_window_background()

        # 阻塞除当前窗体之外的所有的窗体
        self.layout_widget.setWindowModality(Qt.ApplicationModal)

        self.layout_widget.setObjectName("layout_widget")
        self.layout.setObjectName("gridLayout")
        self.label.setObjectName("label")
        self.title.setObjectName("title")
        self.text.setObjectName("text")
        self.button.setObjectName("button")

        # self.layout_widget.setGeometry(QRect(0, 0, 551, 291))
        # self.layout_widget.resize(550, 300)
        # self.main_window.setFixedSize(QSize(550, 300))
        self.layout_widget.setFixedSize(QSize(550, 300))
        # self.layout_widget.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)

        self.layout.setContentsMargins(10, 10, 5, 5)
        self.text.setStyleSheet("border: none;")

        # 设置字体
        font = QFont()
        # font.setFamily("Arial")  # 括号里可以设置成自己想要的其它字体
        font.setPointSize(25)  # 括号里的数字可以设置成自己想要的字体大小
        font.setBold(True)
        self.title.setFont(font)

        self.layout.setColumnMinimumWidth(2, 40)

        # 设置主图
        self.label.setFixedWidth(80)
        pix = QPixmap(settings.MENUBAR_UI["view"])
        self.label.setPixmap(pix)
        self.label.setScaledContents(True)  # 图片自适应

        self.layout.addWidget(self.title, 0, 1, 1, 1)
        # spacer_item = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        # self.layout.addItem(spacer_item, 0, 2, 2, 1)
        self.layout.addWidget(self.label, 0, 0, 1, 1)
        self.layout.addWidget(self.text, 1, 1, 1, 1)
        # spacer_item1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # self.layout.addItem(spacer_item1, 1, 0, 1, 1)
        self.layout.addWidget(self.button, 2, 2, 1, 1)
        # spacer_item2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # self.layout.addItem(spacer_item2, 2, 0, 1, 2)

        self.button.clicked.connect(self.close_window)

    def close_window(self, event: bool) -> None:
        """
        关闭窗口
        :param event:
        :return:
        """
        if event:
            pass
        # self.layout_widget.close()
        self.layout_widget.hide()

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.label.setText(_translate("AboutUI", ""))
        self.title.setText(_translate("AboutUI", "远程协助 v1.0"))
        self.button.setText(_translate("AboutUI", "ok"))
        self.text.setHtml(_translate("AboutUI",
                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                     "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                     "p, li { white-space: pre-wrap; }\n"
                                     "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:10pt;\">    本软件主要使用Python基于Qt5进行编程.</span></p>\n"
                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:10pt;\">    本软件使用于学习软件开发.</span></p>\n"
                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:10pt;\">    请不要触犯法律,否则后果自负,一切与原作者无关.</span></p>\n"
                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:10pt;\">    Pythton: v3.7</span></p>\n"
                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:10pt;\">    Qt: v5.13</span></p>\n"
                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:10pt;\">    目前还在开发中......</span></p></body></html>"))
