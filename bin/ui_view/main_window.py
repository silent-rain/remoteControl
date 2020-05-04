# -*- coding: utf-8 -*-
from PyQt5.QtGui import QIcon, QPalette, QPixmap, QBrush, QCloseEvent, QResizeEvent, QColor
from PyQt5.QtWidgets import QWidget, QMainWindow, QDesktopWidget, QMessageBox
from PyQt5.QtCore import QCoreApplication, QMetaObject, Qt

from lib import settings

_translate = QCoreApplication.translate

"""
主窗口模块
"""


class MainWindowUI(object):
    def __new__(cls, *args, **kwargs) -> object:
        if not hasattr(cls, "_instance"):  # 反射
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, main_window: QMainWindow):
        if not hasattr(self, "_init_flag"):  # 反射
            self._init_flag = True  # 只初始化一次
            self.main_window = main_window
            # 中心窗口
            self.centralwidget = QWidget(self.main_window, Qt.WindowFlags())

            # 创建调色板
            self.palette = QPalette()
            # 颜色初始化
            # self.color_init = QColor(107, 173, 246)
            self.color_init = QColor(QColor(*settings.SKIN_COLOR))

            # 消息对话框
            self.message_box = QMessageBox(self.main_window)

    def setup_ui(self) -> None:
        self.main_window.setObjectName("main_window")
        self.main_window.resize(850, 500)

        self.centralwidget.setObjectName("centralwidget")
        self.main_window.setCentralWidget(self.centralwidget)

        # noinspection PyArgumentList,PyCallByClass
        QMetaObject.connectSlotsByName(self.main_window)

    def retranslate_ui(self) -> None:
        pass


class MainWindowView(MainWindowUI):
    def setup_ui(self) -> None:
        super().setup_ui()

        self.set_window_icon()
        self.set_window_background()
        self.set_window_background4()
        self.center()
        # self.main_window.resizeEvent = self.resize_event
        self.main_window.closeEvent = self.close_event

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        super().retranslate_ui()
        self.main_window.setWindowTitle(_translate("MainWindowUI", "远程控制"))

    def set_window_icon(self) -> None:
        """
        设置窗口的图标
        引用资源 qtResource.py
        :return:
        """
        self.main_window.setWindowIcon(QIcon(settings.MAIN_UI["app"]))

    def set_window_background(self) -> None:
        """
        设置背景: 背景色
        :return:
        """
        # 导航栏透明(linux无效): border-top-color: transparent;
        # 背景透明(linux背景漆黑): background:transparent;
        # 边框透明(linux无效果): border: transparent;
        # 背景色: background-color: rgb(100, 200, 255);

        # 整体背景
        # 如果设置背景色,透明失效
        # self.main_window.setStyleSheet("background-color: rgb(100, 200, 255);")
        # self.main_window.setStyleSheet("background-color: rgb(107, 173, 246);")
        self.main_window.setStyleSheet("background-color: rgb{};".format(self.color_init.getRgb()[:3]))

        # 不显示标题栏，亦无边框
        # 无法移动
        # self.main_window.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)

        # 设置背景（全透明）
        # 如果设置背景色,透明失效
        # 效果为一般为漆黑
        # self.main_window.setAttribute(Qt.WA_TranslucentBackground, True)

    def set_window_background2(self) -> None:
        """
        设置背景: 填充图片
        :return:
        """
        # 图片背景: background-image: url(:/images/background.png);
        self.main_window.setStyleSheet("background-image: url({0});".format(settings.MAIN_UI["background"]))
        # 自动填充背景
        # self.main_window.setAutoFillBackground(False)

    def set_window_background3(self, event: QResizeEvent = None) -> None:
        """
        设置背景: 平铺图片
        :return:
        """
        palette = QPalette()
        # 需要png格式，jpg失败！
        # pix = QPixmap("../src/image/background.jpg")  # 直接使用
        pix = QPixmap(settings.MAIN_UI["background"])  # 打包资源
        # pix = pix.scaled(self.main_window.width(), self.main_window.height())
        if event:
            # 窗口变化,重新获取窗口大小
            pix = pix.scaled(event.size())
        else:
            # 平铺
            pix = pix.scaled(self.main_window.size())
        palette.setBrush(QPalette.Background, QBrush(pix))
        self.main_window.setPalette(palette)

    def set_window_background4(self) -> None:
        """
        使用调色板
        :return:
        """
        self.palette.setColor(QPalette.Background, self.color_init)  # 给调色板设置颜色
        self.main_window.setPalette(self.palette)  # 给控件设置颜色

    def center(self) -> None:
        """
        控制窗口显示在屏幕中心
        :return:
        """
        # 获得窗口
        qr = self.main_window.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.main_window.move(qr.topLeft())

    def resize_event(self, event: QResizeEvent) -> None:
        """
        重置窗口事件
        :param event:
        :return:
        """
        self.set_window_background3(event)

    # noinspection PyArgumentList
    def close_event(self, event: QCloseEvent) -> None:
        """
        重置退出事件
        退出消息提示框
        直接继承main_window的背景色
        :param event:
        :return:
        """
        # self.message_box = QMessageBox(self.main_window)
        # 标题图标
        # msg.setWindowIcon(QIcon(settings.mainUi["confirm"]))

        # 设置背景图片
        # 背景图片： "background-image: url(:/image/mainUi/background.png);"
        # msg.setStyleSheet("background-image: url({0});".format(settings.mainUi["background"]))

        reply = self.message_box.information(
            self.main_window,
            _translate("MainWindowUI", "温馨提示"),
            _translate("MainWindowUI", "您确认要退出???"),
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )
        if reply == QMessageBox.Yes:
            # self.communicate.server_status.emit(False)  # 程序退出后关闭服务器
            # self.communicate.log_info.emit(self.logger.info("正在关闭服务器..."))
            # self.communicate.log_info.emit(self.logger.info("程序退出..."))
            event.accept()
        else:
            event.ignore()
