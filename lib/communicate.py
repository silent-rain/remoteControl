# -*- coding: utf-8 -*-
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QColor


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

    skin_color = pyqtSignal(QColor)  # 皮肤调节

    # 数据交互
    online_data = pyqtSignal(list)  # 单条上线数据
    offline_data = pyqtSignal(list)  # 单条下线数据  # 未使用
    mysql_db = pyqtSignal(list)  # 单条上线数据  # 未使用

    display_info = pyqtSignal(list)  # 展示信息

    # 状态栏
    monitor_port = pyqtSignal(int)  # 监听端口  # 未使用
    online_count = pyqtSignal(int)  # 上线主机计数
    online_sound = pyqtSignal((bool, str))  # 上线/下线提示音  # 上线

    # 工具导航
    init_start_server = pyqtSignal()  # 服务启动 初始化信号


communicate = Communicate()
