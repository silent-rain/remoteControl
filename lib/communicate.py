# -*- coding: utf-8 -*-
from PyQt5.QtCore import QObject, pyqtSignal


class Communicate(QObject):
    # 系统信息
    log_info = pyqtSignal(str)  # 日志信息

    # 模块显示/隐藏
    tools_extension_show = pyqtSignal(bool)  # 工具箱扩展是否显示
    tools_extension_checked = pyqtSignal(bool)  # 菜单栏中的工具箱扩展是否选中
    toolbar_show = pyqtSignal(bool)  # 工具栏是否显示
    toolbar_checked = pyqtSignal(bool)  # 菜单栏中的工具栏是否选中
    statusbar_show = pyqtSignal(bool)  # 状态栏是否显示
    statusbar_checked = pyqtSignal(bool)  # 菜单栏中的状态栏是否选中
    group_tree_show = pyqtSignal(bool)  # 分组信息是否显示
    group_tree_checked = pyqtSignal(bool)  # 菜单栏中的分组信息是否选中

    # 信号关闭
    skin_color_dialog_close = pyqtSignal(bool)  # 皮肤窗口关闭


communicate = Communicate()
