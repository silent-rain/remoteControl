# -*- coding: utf-8 -*-
from PyQt5.QtGui import QCursor, QHideEvent
from PyQt5.QtWidgets import QMainWindow, QTreeWidget, QTreeWidgetItem, QWidget, QAction, QMenu, QInputDialog
from PyQt5.QtCore import QCoreApplication, Qt, QRect, QSize

from bin.ui_view.base.dock_widget_base import DockWidgetBase
from bin.ui_view.base.table_widget_base import TableWidgetBase
from bin.ui_view.utils import load_animation
from lib import settings
from lib.communicate import communicate
from lib.logger import logger

_translate = QCoreApplication.translate

"""
分组信息 GroupInfoUI

信息展示 DisplayInfoUI
"""


class TableWidgetUI(TableWidgetBase):
    def __init__(self):
        """
        信息展示 基类
        """
        super().__init__()
        # self.headers_us = ["Id", "Date", "Type", "Message"]
        # self.headers_title_us = ["Id", "out_net", "in_net", "host_name", "system", "cpu", "memory", "disk",
        #                          "video", "voice", "boot_time", "version", "group", "position", "note"]

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
            _translate("DisplayInfoUI", "分组"),
            _translate("DisplayInfoUI", "区域"),
            _translate("DisplayInfoUI", "备注"),
        ]

        self.header_width = [60]

    def setup_ui(self) -> None:
        super().setup_ui()
        # self.setMinimumHeight(200)

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.setWindowTitle(_translate("DisplayInfoUI", "信息展示"))


class GroupTreeWidgetUI(object):
    def __init__(self, layout_widget: QWidget):
        """
        分组信息基类
        :param layout_widget:
        """
        self.layout_widget = layout_widget

        self.group_tree = QTreeWidget(self.layout_widget)
        # noinspection PyArgumentList
        self.headers_title = [
            _translate("DisplayInfoUI", "Id"),
            # _translate("DisplayInfoUI", "外网"),
            _translate("DisplayInfoUI", "主机信息"),
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
            _translate("DisplayInfoUI", "分组"),
            _translate("DisplayInfoUI", "区域"),
            _translate("DisplayInfoUI", "备注"),
        ]
        # self.headers_title = [
        #     _translate("DisplayInfoUI", "Id"),
        #     _translate("DisplayInfoUI", "主机信息"),
        #     _translate("DisplayInfoUI", "备注"),
        # ]
        self.header_width = [90, 100]
        self.hide_column = [self.headers_title.index(item) for item in self.headers_title[2:-1]]

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
        # pll = self.group_tree.palette()
        # pll.setBrush(QPalette.Base, QBrush(QColor(255, 255, 255, 0)))
        # self.group_tree.setPalette(pll)

        # 节点全部展开
        # self.group_tree.expandAll()

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

        # 隐藏第一列
        # self.group_tree.hideColumn(0)
        for column in self.hide_column:
            self.group_tree.hideColumn(column)

    def default_master_node(self) -> None:
        """
        设置默认主节点
        :return:
        """
        # noinspection PyArgumentList
        default_master_node = [
            _translate("DisplayInfoUI", "在线主机"),
            _translate("DisplayInfoUI", "下线主机"),
        ]
        for index, node in enumerate(default_master_node):
            master = QTreeWidgetItem(self.group_tree)
            # 节点信息设置
            # self.group_tree.topLevelItem(index).setText(0, node)
            master.setText(0, node)
            master.setText(1, "(0)")

    def setup_ui(self) -> None:
        self.options()
        self.set_headers()
        self.default_master_node()

        # 优化3 给节点添加响应事件
        # self.list_group.clicked.connect(self.on_clicked)
        # 项目进入触发 itemExpanded
        # 项目退出触发 itemCollapsed
        # 当用户在窗口小部件内单击时会发出此信号。 itemClicked
        # 内容改变时发生：itemChanged
        # self.group_tree.itemClicked.connect(self.on_clicked)

        # 鼠标点击事件
        self.group_tree.itemClicked.connect(self.master_item_clicked)

    def master_item_clicked(self, event1: QTreeWidgetItem, event2: int) -> None:
        """
        鼠标单击事件
        获取根节点所有信息
        发送信号 -> 信息展示
        :param event1:
        :param event2:
        :return:
        """
        if event2:
            pass
        if event1.parent() is not None:
            # 不是根节点
            return None
        data = self.get_current_master_item_data()
        communicate.display_info.emit(data)

    def master_item_real_time_refresh(self):
        """
        数据实时刷新
        系统初始化发送数据 -> 信息展示
        :return:
        """
        master = self.group_tree.currentItem()
        if master is None:
            master: QTreeWidgetItem = self.group_tree.topLevelItem(0)
        if master.parent():
            master = master.parent()

        node_count = master.childCount()

        data_info = []
        for i in range(node_count):
            child = master.child(i)
            child_data_info = []
            for index in range(len(self.headers_title)):
                child_data_info.append(child.text(index))
            data_info.append(child_data_info)
        communicate.display_info.emit(data_info)

    def get_current_master_item_data(self) -> list:
        """
        获取当前根节点下的所有信息
        :return:
        """
        master: QTreeWidgetItem = self.group_tree.currentItem()
        node_count = master.childCount()

        data_info = []
        for i in range(node_count):
            child = master.child(i)
            child_data_info = []
            for index in range(len(self.headers_title)):
                child_data_info.append(child.text(index))
            data_info.append(child_data_info)
        return data_info

    def get_top_row_count(self) -> int:
        """
        获取根节个数
        :return:
        """
        # 获取根节个数
        count = self.group_tree.topLevelItemCount()
        # 根据索引获取根节点
        # master = self.group_tree.topLevelItem(1)
        return count

    def get_child_row_count(self, p_int: int) -> int:
        """
        获取子节个数
        :param p_int: 上一级节点索引
        :return:
        """
        # 获取子节个数
        count = self.group_tree.topLevelItem(p_int).childCount()
        # 根据上一级节点获取子节点对象
        # item = self.group_tree.topLevelItem(p_int).child(0)
        return count

    def add_master_item(self, title: str = "新根节点") -> QTreeWidgetItem:
        """
        添加根节点
        :param title:
        :return:
        """
        master = QTreeWidgetItem(self.group_tree)
        master.setText(0, title)
        # child.setFlags(Qt.ItemIsEnabled | Qt.ItemIsEditable)
        return master

    def master_exists(self, _name: str) -> (bool, QTreeWidgetItem):
        """
        判断根节点名称是否存在
        :param _name: 名称
        :return: 返回存在的节点
        """
        # 获取根节个数
        master_count = self.group_tree.topLevelItemCount()
        for index in range(master_count):
            # 获取根节点
            master: QTreeWidgetItem = self.group_tree.topLevelItem(index)
            name = master.text(0)
            if name == _name:
                return master
        return None

    def master_exists2(self, index: int) -> (bool, QTreeWidgetItem):
        """
        判断根节点索引是否存在
        :param index: 名称
        :return: 返回存在的节点
        """
        # 获取根节个数
        master_count = self.group_tree.topLevelItemCount()
        if index <= master_count:
            master = self.group_tree.topLevelItem(index)
            return master
        return None

    def add_child_item(self, name: str, item: list) -> None:
        """
        根据name获取根节点
        根节点不存在,创建根节点
        添加子节点
        :param name: 根节点 name
        :param item: 数据序列
        :return:
        """
        # 判断根节点是否存在返回根节点
        master: QTreeWidgetItem = self.master_exists(name)
        if not master:
            # 添加一个根节点
            master: QTreeWidgetItem = self.add_master_item(name)

        count = master.childCount()  # 获根节点的子节点个数
        item.pop(0)
        item.insert(0, count + 1)  # 插入ID
        child = QTreeWidgetItem()
        child.setCheckState(0, Qt.Unchecked)
        for index, value in enumerate(item):
            child.setText(index, str(value))
        master.addChild(child)

        # 更新分组计数
        self.update_count()

        if settings.REAL_TIME_REFRESH:
            # 实时刷新上线数据
            self.master_item_real_time_refresh()

    def add_child_item2(self, index: int, item: list) -> None:
        """
        根据索引获取根节点
        索引不存在就创建一个根节点
        添加子节点

        bug:
        存在安全问题,如果检索的索引远远超出界限,将不能正确插入所需要的节点
        :param index: 根节点索引
        :param item: 数据序列
        :return:
        """
        # 获取根节点
        master = self.master_exists2(index)
        if not master:
            # 添加一个根节点
            master = self.add_master_item()

        count = master.childCount()
        item.pop(0)
        item.insert(0, count + 1)  # 插入ID
        child = QTreeWidgetItem()
        child.setCheckState(0, Qt.Unchecked)
        for index, value in enumerate(item):
            child.setText(index, str(value))
        master.addChild(child)

    def add_child_item3(self, item: list) -> None:
        """
        获取当前根节点
        添加子节点
        :param item: 数据序列
        :return:
        """
        # 获取当前根节点
        master: QTreeWidgetItem = self.group_tree.currentItem()
        if master.parent():
            print("当前不是根节点")
            return
        count = master.childCount()
        item.pop(0)
        item.insert(0, count + 1)  # 插入ID
        child = QTreeWidgetItem()
        child.setCheckState(0, Qt.Unchecked)
        for index, value in enumerate(item):
            child.setText(index, value)
        master.addChild(child)

    def child_exists(self, _name: str) -> (bool, QTreeWidgetItem):
        """
        判断子节点名称是否存在
        :param _name: 名称
        :return: 返回存在的节点
        """
        # 获取根节个数
        master_count = self.group_tree.topLevelItemCount()
        for index in range(master_count):
            # 获取根节点
            master: QTreeWidgetItem = self.group_tree.topLevelItem(index)
            child_count = master.childCount()
            for index_node in range(child_count):
                child = master.child(index_node)
                name = child.text(1)
                if name == _name:
                    return child
        return None

    def del_child_item(self, name: str, out_net: str) -> None:
        """
        根据name获取根节点
        根节点不存在,创建根节点
        添加子节点
        :param name: 根节点 分组
        :param out_net: 子节点 主机信息
        :return:
        """
        # 判断根节点是否存在返回根节点
        master: QTreeWidgetItem = self.master_exists(name)
        if not master:
            logger.error("主机下线失败 - 分组不存在: {}".format(name))
            return None
        child = self.child_exists(out_net)
        if not child:
            logger.error("主机下线失败 - 主机信息未找到: {}".format(out_net))
            return None
        # 删除子节点
        master.removeChild(child)

        # 更新分组计数
        self.update_count()

        if settings.REAL_TIME_REFRESH:
            # 实时刷新上线数据
            self.master_item_real_time_refresh()

    def update_count(self) -> None:
        """
        更新主节点 计数信息
        :return:
        """
        # QTreeWidgetItem(self.group_tree).text(0)
        # 获取根节个数
        count = self.group_tree.topLevelItemCount()
        # 根据索引获取根节点
        for index in range(count):
            master = self.group_tree.topLevelItem(index)
            child_count = master.childCount()
            # 在线主机 (0)
            text = "({})".format(child_count)
            master.setText(1, text)

    # noinspection PyArgumentList
    def re_translate_ui(self) -> None:
        self.group_tree.headerItem().setText(0, _translate("GroupInfoUI", "Id"))
        self.group_tree.headerItem().setText(1, _translate("GroupInfoUI", "主机信息"))
        self.group_tree.headerItem().setText(2, _translate("GroupInfoUI", "备注"))

    def test_date(self) -> None:
        for i in range(10):
            self.add_child_item2(0, [str(i), str(i * 100), ""])
        for i in range(200):
            self.add_child_item2(1, [str(i), str(i * 100), ""])
        self.update_count()


class DisplayInfoUI(object):
    def __init__(self, main_window: QMainWindow):
        """
        信息展示
        :param main_window:
        """
        self.main_window = main_window

        self.table_widget = TableWidgetUI()

    def setup_ui(self) -> None:
        self.table_widget.setup_ui()

        # self.setMinimumHeight(200)
        self.main_window.setCentralWidget(self.table_widget)

        if settings.LOAD_EFFECT_ON:
            # 特效
            load_animation.load_animation(self.table_widget)

        # print(dir(self.table_widget))

    def retranslate_ui(self) -> None:
        pass


class GroupInfoUI(DockWidgetBase):
    def __init__(self, main_window: QMainWindow):
        """
        分组信息
        :param main_window:
        """
        super().__init__(main_window)
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


class GroupInfoRightMenuConnect(object):
    def __init__(self, group_info_ui: GroupInfoUI):
        """
        分组信息中右键菜单
        :param group_info_ui:
        """
        self.group_info_ui = group_info_ui

        # self.group_ui = GroupInfoUI(self.main_window)
        self.tree_widget = self.group_info_ui.tree_widget
        self.group_tree = self.group_info_ui.tree_widget.group_tree

        self.pop_menu = QMenu(self.group_tree)
        self.add = QAction()
        self.change = QAction()
        self.rename = QAction()
        self.delete = QAction()

    def setup_ui(self) -> None:
        # 在包含有QTreeWidget的窗体中添加customContextMenuRequested的信号处理
        self.group_tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.group_tree.customContextMenuRequested.connect(self.right_menu_pos_show)  # 开放右键策略

        # 增加分组
        self.pop_menu.addAction(self.add)
        self.add.triggered.connect(self.add_event)

        # 修改分组
        self.pop_menu.addAction(self.change)
        self.change.triggered.connect(self.change_event)

        # 删除分组
        self.pop_menu.addAction(self.delete)
        self.delete.triggered.connect(self.delete_event)

    def right_menu_pos_show(self) -> None:
        """
        调整位置
        右键点击时调用的函数
        菜单显示前，将它移动到鼠标点击的位置
        :return:
        """
        # 获取右键位置
        pos = QCursor().pos()
        self.pop_menu.move(pos)
        self.pop_menu.show()

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.add.setText(_translate("GroupInfoUI", "增加分组"))
        self.change.setText(_translate("GroupInfoUI", "修改分组"))
        self.rename.setText(_translate("GroupInfoUI", "重命名"))
        self.delete.setText(_translate("GroupInfoUI", "删除分组"))

    def add_event(self, event: bool, title: str = "新根节点") -> None:
        """
        添加根节点
        :param title:
        :param event:
        :return:
        """
        if event:
            pass
        master = QTreeWidgetItem(self.group_tree)
        master.setText(0, title)
        # self.tree_widget.add_master_item(title)

    def change_event(self, event: bool) -> None:
        """
        修改分组
        :param event:
        :return:
        """
        if event:
            pass

        # 当前节点
        current_item = self.group_tree.currentItem()
        parent = current_item.parent()  # 父节点
        if parent is not None:
            logger.info("操作 - 不能修改子节点!")
            return None
        index = self.group_tree.currentIndex().row()
        if index == 0 or index == 1:
            logger.info("操作 - 默认根节点不允许修改!")
            return None

        # noinspection PyArgumentList
        text, ok = QInputDialog(self.group_info_ui.main_window).getText(
            self.group_info_ui.main_window,
            '温馨提示',
            '修改分组：')
        if ok and text:
            current_item.setText(0, text)
        elif not text:
            logger.info("操作 - 不能为空!")
        else:
            logger.info("操作 - 取消修改分组!")

    def delete_event(self, event: bool) -> None:
        """
        删除根节点
        :param event:
        :return:
        """
        if event:
            pass

        # 当前节点
        current_item = self.group_tree.currentItem()
        parent = current_item.parent()  # 父节点
        if parent is not None:
            logger.info("操作 - 不能删除子节点!")
            return None

        index = self.group_tree.currentIndex().row()
        if index == 0 or index == 1:
            logger.info("操作 - 默认节点不允许删除!")
            return None

        # 获取子节点个数
        count = current_item.childCount()
        if not count:
            self.group_tree.takeTopLevelItem(index)
            return None
        logger.info("操作 - 该节点不是空的!")


class GroupInfoConnect(object):
    def __init__(self, group_info_ui: GroupInfoUI, display_info_ui: DisplayInfoUI):
        """
        分组信息 信号
        :param group_info_ui:
        """
        self.group_info_ui = group_info_ui
        self.display_info_ui = display_info_ui

    def setup_ui(self) -> None:
        self.communicate_connect()

        # 重写事件
        self.group_info_ui.dock_widget.hideEvent = self.hide_event
        self.group_info_ui.dock_widget.showEvent = self.hide_event

    def retranslate_ui(self) -> None:
        pass

    def communicate_connect(self) -> None:
        # 状态栏是否显示
        communicate.group_tree_show.connect(self.group_tree_show)

        # 数据交互
        communicate.online_data.connect(self.online_data)  # 单条上线数据
        communicate.offline_data.connect(self.offline_data)  # 单条下线数据
        communicate.display_info.connect(self.display_info)  # 展示信息

    def display_info(self, event: list) -> None:
        """
        数据发送至展示信息
        :param event:
        :return:
        """
        self.display_info_ui.table_widget.empty_all()
        self.display_info_ui.table_widget.add_data_list(event)

    def group_tree_show(self, flag: bool) -> None:
        """
        分组信息 显示/隐藏
        :param flag:
        :return:
        """
        if flag:
            # 显示
            self.group_info_ui.dock_widget.setHidden(False)
        else:
            # 隐藏
            self.group_info_ui.dock_widget.setHidden(True)

    def hide_event(self, event: QHideEvent) -> None:
        """
        发色信号 -> 菜单栏
        菜单栏中的  分组信息
        :param event:
        :return:
        """
        if event:
            pass
        if self.group_info_ui.dock_widget.isHidden():
            communicate.group_tree_checked.emit(False)
        else:
            communicate.group_tree_checked.emit(True)

    def online_data(self, event: list):
        """
        添加单条数据
        上线数据添加至 分组
        headers_title_us = ["Id", "out_net", "in_net", "host_name", "system", "cpu", "memory", "disk",
                    "video", "voice", "boot_time", "version", "group", "position", "note"]
        :param event:
        :return:
        """
        group = event[-3]
        self.group_info_ui.tree_widget.add_child_item(group, event)
        communicate.online_count.emit(1)

    def offline_data(self, event: list):
        """
        删除单条数据
        下线数据添加至 下线主机分组
        在线主机分组删除
        headers_title_us = ["Id", "out_net", "in_net", "host_name", "system", "cpu", "memory", "disk",
                    "video", "voice", "boot_time", "version", "group", "position", "note"]
        :param event:
        :return:
        """
        group = event[-3]
        out_net = event[1]
        self.group_info_ui.tree_widget.del_child_item(group, out_net)
        communicate.online_count.emit(-1)
