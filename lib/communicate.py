# -*- coding: utf-8 -*-
from PyQt5.QtCore import QObject, pyqtSignal


class Communicate(QObject):
    # 系统信息
    log_info = pyqtSignal(str)  # 日志信息

    # 模块显示/隐藏
    tools_extension_show = pyqtSignal(bool)  # 工具箱扩展是否显示
    toolbar_show = pyqtSignal(bool)  # 工具栏是否显示
    statusbar_show = pyqtSignal(bool)  # 状态栏是否显示


communicate = Communicate()
