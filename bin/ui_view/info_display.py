# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QTreeWidget, QTreeWidgetItem, QHeaderView, QWidget
from PyQt5.QtCore import QCoreApplication, Qt, QRect, QSize

from bin.ui_view.base.dock_widget_base import DockWidgetBase
from bin.ui_view.base.table_widget_base import TableWidgetBase
from bin.ui_view.utils import load_animation
from lib import settings
from lib.communicate import communicate

_translate = QCoreApplication.translate

"""
分组信息 GroupInfoUI

信息展示 DisplayInfoUI
"""


class TableWidgetUI(TableWidgetBase):

    def __init__(self):
        """
        信息展示 模块
        """
        super().__init__()
        # self.headers_us = ["Id", "Date", "Type", "Message"]
        # noinspection PyArgumentList
        self.headers_title = [
            _translate("DisplayInfoUI", "Id"),
            _translate("DisplayInfoUI", "外网"),
            _translate("DisplayInfoUI", "内网"),
            _translate("DisplayInfoUI", "计算机"),
            _translate("DisplayInfoUI", "操作系统"),
            _translate("DisplayInfoUI", "处理器"),
            _translate("DisplayInfoUI", "内存"),
            _translate("DisplayInfoUI", "硬盘容量"),
            _translate("DisplayInfoUI", "视频"),
            _translate("DisplayInfoUI", "语音"),
            _translate("DisplayInfoUI", "开机时间"),
            _translate("DisplayInfoUI", "服务版本"),
            _translate("DisplayInfoUI", "区域"),
            _translate("DisplayInfoUI", "备注"),
        ]

        self.header_width = [60]

    def setup_ui(self):
        super().setup_ui()
        # self.setMinimumHeight(200)

    # noinspection PyArgumentList
    def retranslate_ui(self):
        self.setWindowTitle(_translate("DisplayInfoUI", "信息展示"))


class DisplayInfoUI(object):
    def __new__(cls, *args, **kwargs) -> object:
        if not hasattr(cls, "_instance"):  # 反射
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, main_window: QMainWindow):
        """
        信息展示
        :param main_window:
        """
        if not hasattr(self, "_init_flag"):  # 反射
            self.main_window = main_window

            self.table_widget = TableWidgetUI()

    def setup_ui(self):
        self.table_widget.setup_ui()

        # self.setMinimumHeight(200)
        self.main_window.setCentralWidget(self.table_widget)

        if settings.LOAD_EFFECT_ON:
            # 特效
            load_animation.load_animation(self.table_widget)

        # print(dir(self.table_widget))

    def retranslate_ui(self):
        pass


class GroupInfoUI(DockWidgetBase):
    def __new__(cls, *args, **kwargs) -> object:
        if not hasattr(cls, "_instance"):  # 反射
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, main_window: QMainWindow):
        """
        工具扩展
        :param main_window:
        """
        if not hasattr(self, "_init_flag"):  # 反射
            super().__init__(main_window)
            self._init_flag = True  # 只初始化一次
            self.main_window = main_window

            self.tree_widget = GroupTreeWidgetUI(self.layout_widget)

    def setup_ui(self) -> None:
        super().setup_ui()
        # noinspection PyArgumentList
        self.layout.addWidget(self.tree_widget.group_tree)

        self.tree_widget.setup_ui()

        if not settings.TOOLS_EXTENSION_SHOW:
            # self.dock_widget.hide()
            self.dock_widget.setHidden(True)
        if settings.LOAD_EFFECT_ON:
            # 特效
            load_animation.load_animation(self.tree_widget.group_tree)

        # QDockWidget 显示位置
        self.main_window.addDockWidget(Qt.LeftDockWidgetArea, self.dock_widget)

        # 初始化QDockWidget的高度
        self.dock_widget_contents.sizeHint = self.size_hint

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.dock_widget.setWindowTitle(_translate("DisplayInfoUI", "分组信息"))

    @staticmethod
    def size_hint() -> QSize:
        """
        在这里定义 QDockWidget 的初始大小
        :return:
        """
        return QSize(200, 0)


class GroupTreeWidgetUI(object):
    def __init__(self, layout_widget: QWidget):
        self.layout_widget = layout_widget

        self.group_tree = QTreeWidget(self.layout_widget)
        # noinspection PyArgumentList
        self.headers_title = [
            _translate("DisplayInfoUI", "Id"),
            _translate("DisplayInfoUI", "主机信息"),
            _translate("DisplayInfoUI", "备注"),
        ]
        self.header_width = [60, 130]

    def options(self) -> None:
        """
        设置参数
        :return:
        """
        self.group_tree.setObjectName("group_tree")
        self.group_tree.setGeometry(QRect(0, 0, 100, 0))

        # 启用或禁用排序
        # __sortingEnabled = self.treeWidget.isSortingEnabled()
        # self.group_tree.setSortingEnabled(False)
        # 此处内容排序
        # self.group_tree.setSortingEnabled(__sortingEnabled)

        # 窗口小部件的背景将是透明的
        # self.group_tree.setAutoFillBackground(True)

        # 优化2 设置根节点的背景颜色
        # brush_red = QBrush(Qt.red)
        # root.setBackground(0, brush_red)
        # brush_blue = QBrush(Qt.blue)
        # root.setBackground(1, brush_blue)

        # 背景透明与表头冲突, 会呈现黑色
        # self.group_tree.setStyleSheet(
        #     # "QHeaderView::section{background-color: rgba(255, 0, 0, 0);};"  # 背景颜色
        #     "QHeaderView::section{background:transparent;};"  # 表头透明
        # )

        # 背景透明，标题头不透明
        # pll = self.list_group.palette()
        # pll.setBrush(QPalette.Base, QBrush(QColor(255, 255, 255, 0)))
        # self.list_group.setPalette(pll)

    def set_headers(self) -> None:
        """
        设置标题
        :return:
        """
        # 设置列数
        # self.group_tree.setColumnCount(1)
        self.group_tree.setColumnCount(len(self.headers_title))

        # 设置树形控件头部的标题, 默认值为1
        # 单个设置标题,顺序
        # for title in self.headers_title:
        #     self.group_tree.setHeaderLabel(title)
        # 一次设置多个标题,顺序
        # self.group_tree.setHeaderLabels(self.headers_title)

        # 单个设置标题,精准
        for index, title in enumerate(self.headers_title):
            self.group_tree.headerItem().setText(index, title)

        # 隐藏隐藏表头
        # self.group_tree.header().setVisible(False)
        # self.group_tree.setHeaderHidden(True)

        # 设置树形控件的列的宽度
        for index, width in enumerate(self.header_width):
            self.group_tree.setColumnWidth(index, width)

    def default_master_node(self) -> None:
        """
        设置默认主节点
        :return:
        """
        # noinspection PyArgumentList
        default_master_node = [
            _translate("DisplayInfoUI", "在线主机(0)"),
            _translate("DisplayInfoUI", "下线主机(0)"),
        ]
        for index, node in enumerate(default_master_node):
            QTreeWidgetItem(self.group_tree)
            # 节点设置在第1列
            self.group_tree.topLevelItem(index).setText(0, node)
            # self.group_tree.topLevelItem(1).setText(0, _translate("Form", "分组12"))

    def setup_ui(self):
        self.options()
        self.set_headers()
        self.default_master_node()

        # self.root_online_item()
        # self.root_offline_item()

        # 优化3 给节点添加响应事件
        # self.list_group.clicked.connect(self.on_clicked)
        # 项目进入触发 itemExpanded
        # 项目退出触发 itemCollapsed
        # 当用户在窗口小部件内单击时会发出此信号。 itemClicked
        # 内容改变时发生：itemChanged
        # self.group_tree.itemClicked.connect(self.on_clicked)

        # self.list_group.expandAll()  # 节点全部展开

    def test(self):
        item_0 = QTreeWidgetItem(self.treeWidget)

        item_1 = QTreeWidgetItem(item_0)
        item_1.setCheckState(0, Qt.Checked)

        item_1 = QTreeWidgetItem(item_0)
        item_1.setCheckState(0, Qt.Checked)

    def add_root(self):
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)

        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Checked)

        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Checked)

    def root_online_item(self):
        # 设置根节点
        self.root_online = QTreeWidgetItem(self.group_tree)
        self.root_online.setText(0, _translate("list_group", "在线主机"))
        # root.setIcon(0, QIcon('./images/root.png'))
        # 加载根节点的所有属性与子控件
        self.group_tree.addTopLevelItem(self.root_online)

    def root_offline_item(self):
        # 设置根节点
        self.root_offline = QTreeWidgetItem(self.group_tree)
        self.root_offline.setText(0, _translate("list_group", "离线主机"))
        # root.setIcon(0, QIcon('./images/root.png'))
        # 加载根节点的所有属性与子控件
        self.group_tree.addTopLevelItem(self.root_offline)

    def online_host(self, ip, host_name):
        """
        在线主机
        :param ip:
        :param host_name:
        :return:
        """
        host = QTreeWidgetItem(self.root_online)
        host.setText(0, ip)
        host.setText(1, host_name)
        # child3.setIcon(0, QIcon('./images/music.png'))
        # 优化1 设置节点的状态
        host.setCheckState(0, Qt.Unchecked)

    def offline_host(self, ip, host_name):
        """
        离线主机
        :param ip:
        :param host_name:
        :return:
        """
        host = QTreeWidgetItem(self.root_offline)
        host.setText(0, ip)
        host.setText(1, host_name)
        # child3.setIcon(0, QIcon('./images/music.png'))
        host.setCheckState(0, Qt.Unchecked)
        # print(child3.isSelected())
        # print(child3.isSelected())

        # child3.addChild(self.root_offline)  # 添加子节点

    def on_clicked(self):
        item = self.group_tree.currentItem()
        # print('Key=%s,value=%s' % (item.text(0), item.text(1)))
        if item.text(0) == "在线主机":
            return None
        elif item.text(0) == "离线主机":
            return None

        if item.checkState(0) == Qt.Checked:
            item.setCheckState(0, Qt.Unchecked)
        elif item.checkState(0) == Qt.Unchecked:
            item.setCheckState(0, Qt.Checked)

    def add_data_recv(self, data):
        out_ip = data["out_ip"]
        host_name = data["host_name"]
        if data["flag"]:
            self.online_host(out_ip, host_name)
        else:
            self.offline_host(out_ip, host_name)

    def communicate_connect(self):
        communicate.request_data.connect(self.add_data_recv)  # 下线主机

    # noinspection PyArgumentList
    def re_translate_ui(self):
        self.group_tree.headerItem().setText(0, _translate("Form", "Id"))
        self.group_tree.headerItem().setText(1, _translate("Form", "主机信息"))
        self.group_tree.headerItem().setText(2, _translate("Form", "备注"))
