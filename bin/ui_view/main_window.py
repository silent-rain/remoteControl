# -*- coding: utf-8 -*-
from PyQt5.QtGui import QIcon, QPalette, QPixmap, QBrush, QCloseEvent, QResizeEvent, QColor
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QMessageBox
from PyQt5.QtCore import QCoreApplication, QMetaObject

from bin.ui_view.utils import load_animation
from lib import settings
from lib.communicate import communicate

_translate = QCoreApplication.translate

"""
主窗口模块
"""


class MainWindowUI(object):
    def __init__(self, main_window: QMainWindow):
        """
        主窗口
        :param main_window:
        """
        self.main_window = main_window

        # 创建调色板
        self.palette = QPalette()
        # 颜色初始化
        # self.color_init = QColor(107, 173, 246)
        self.color_init = QColor(*settings.SKIN_COLOR)

    def setup_ui(self) -> None:
        self.main_window.setObjectName("main_window")
        self.main_window.resize(850, 500)

        # noinspection PyArgumentList,PyCallByClass
        QMetaObject.connectSlotsByName(self.main_window)

        self.set_window_icon()
        self.set_window_background()
        self.set_window_background4()
        self.center()
        # self.main_window.resizeEvent = self.resize_event
        # self.main_window.closeEvent = self.close_event  # 放在信号区

        # 隐藏工具栏上的右键菜单
        # self.main_window.setContextMenuPolicy(Qt.NoContextMenu)

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.main_window.setWindowTitle(_translate("MainWindowUI", "远程协助"))

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

        #  设置透明用
        # self.main_window.setWindowOpacity(0.5)

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
        message_box = QMessageBox(self.main_window)
        # noinspection PyArgumentList
        reply = message_box.information(
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


class MainWindowConnect(object):
    def __init__(self, main_window_ui: MainWindowUI):
        """
        主窗口信号
        :param main_window_ui:
        """
        self.main_window_ui = main_window_ui

    def setup_ui(self) -> None:
        self.communicate_connect()

        # 主窗口关闭 事件
        self.main_window_ui.main_window.closeEvent = self.close_event

    def communicate_connect(self) -> None:
        pass

    def close_event(self, event: QCloseEvent) -> None:
        """
        主窗口重置退出事件
        退出消息提示框
        直接继承main_window的背景色
        :param event:
        :return:
        """
        message_box = QMessageBox(self.main_window_ui.main_window)
        # noinspection PyArgumentList
        reply = message_box.information(
            self.main_window_ui.main_window,
            _translate("MainWindowUI", "温馨提示"),
            _translate("MainWindowUI", "您确认要退出???"),
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )
        if reply == QMessageBox.Yes:
            communicate.start_server.emit(False)  # 程序退出后关闭服务器
            communicate.log_info.emit("系统信息 - 正在关闭服务器...")
            communicate.log_info.emit("系统信息 - 程序退出...")
            event.accept()
        else:
            event.ignore()

    def retranslate_ui(self) -> None:
        pass
