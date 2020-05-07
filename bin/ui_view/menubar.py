# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMenuBar, QMainWindow, QMenu, QAction
from PyQt5.QtGui import QFont, QIcon, QColor, QPalette
from PyQt5.QtCore import QCoreApplication

from bin.ui_view.utils import load_animation
from bin.ui_view.utils.about import AboutUI
from lib import settings
from bin.ui_view.utils.skincolordialog import SkinColorDialogView
from lib.communicate import communicate

_translate = QCoreApplication.translate

"""
选项 OptionMenu
    程序设置
    生成服务端
    皮肤
    分隔符
    退出
查看 ViewMenu
    工具扩展
    工具导航
    状态栏
帮助 HelpMenu
    关于
"""


class OptionMenu(object):
    def __init__(self, menubar: QMenuBar, main_window: QMainWindow):
        """
        选项
        :param menubar:
        :param main_window:
        """
        self.menubar = menubar
        self.main_window = main_window

        # 向菜单栏中添加新的QMenu对象，父菜单
        self.option = QMenu(self.menubar)

        # 程序设置
        self.setting = QAction(QIcon(settings.MENUBAR_UI["setting"]), '&Setting', self.menubar)

        # 创建客户端
        self.make_server = QAction(QIcon(settings.MENUBAR_UI["make_server"]), '&Make Server', self.menubar)

        # 皮肤
        self.skin = QAction(QIcon(settings.MENUBAR_UI["skin"]), '&Skin Settings', self.menubar)

        # 分隔符
        self.option.addSeparator()

        # 退出
        self.exit = QAction(QIcon(settings.MENUBAR_UI["exit"]), '&Exit', self.menubar)

        # 皮肤对象
        self.skin_color_dialog = SkinColorDialogView(self.main_window)

    def setup_ui(self) -> None:
        self.setting.setShortcut('Ctrl+Alt+S')
        self.setting.setObjectName("setting")
        self.option.addAction(self.setting)
        self.setting.triggered.connect(self.setting_receive)

        self.make_server.setShortcut('Ctrl+N')
        self.make_server.setObjectName("make_server")
        self.option.addAction(self.make_server)
        self.make_server.triggered.connect(self.make_server_receive)

        self.skin.setShortcut('Ctrl+N')
        self.skin.setObjectName("skin")
        self.option.addAction(self.skin)
        self.skin.triggered.connect(self.skin_receive)

        self.exit.setShortcut('Ctrl+Q')
        self.exit.setObjectName("exit")
        self.option.addAction(self.exit)
        # self.exit.triggered.connect(QCoreApplication.quit)  # 直接退出程序
        self.exit.triggered.connect(self.exit_receive)

        self.menubar.addAction(self.option.menuAction())

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.option.setTitle(_translate("MenubarUI", "选项"))
        self.setting.setText(_translate("MenubarUI", "程序设置"))
        self.make_server.setText(_translate("MenubarUI", "创建客户端"))
        self.skin.setText(_translate("MenubarUI", "皮肤调节"))
        self.exit.setText(_translate("MenubarUI", "退出程序"))

    def setting_receive(self) -> None:
        """
        程序设置
        :return:
        """
        print("setting_receive")

    def make_server_receive(self) -> None:
        """
        生成服务端
        :return:
        """
        print("make_server_receive")

    def skin_receive(self) -> None:
        """
        调色
        :return:
        """
        self.skin_color_dialog.start()

    def exit_receive(self) -> None:
        """
        退出程序
        :return:
        """
        self.main_window.close()


class ViewMenu(object):
    def __init__(self, menubar: QMenuBar):
        """
        查看
        :param menubar:
        """
        self.menubar = menubar

        # 向菜单栏中添加新的QMenu对象，父菜单
        self.view = QMenu(self.menubar)

        # 状态栏
        self.statusbar = QAction(QIcon(""), '&Statusbar', self.menubar)
        # 工具导航
        self.toolbar = QAction(QIcon(""), '&Toolbar', self.menubar)
        # 分组信息
        self.group_info = QAction(QIcon(""), '&Group Info', self.menubar)
        # 工具扩展
        self.tools_extension = QAction(QIcon(""), '&Tools Extension', self.menubar)

    def setup_ui(self) -> None:
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setCheckable(True)
        self.statusbar.triggered.connect(self.statusbar_receive)  # 变化的信号
        # self.statusbar.changed.connect(self.statusbar_receive)  # 变化的信号
        self.view.addAction(self.statusbar)

        self.toolbar.setObjectName("toolbar")
        self.toolbar.setCheckable(True)
        self.toolbar.triggered.connect(self.toolbar_receive)
        self.view.addAction(self.toolbar)

        self.group_info.setObjectName("group_info")
        self.group_info.setCheckable(True)
        self.group_info.triggered.connect(self.group_info_receive)
        self.view.addAction(self.group_info)

        self.tools_extension.setObjectName("tools_extension")
        self.tools_extension.setCheckable(True)
        self.tools_extension.triggered.connect(self.tools_extension_receive)
        # self.tools_extension.changed.connect(self.tools_extension_receive)
        self.view.addAction(self.tools_extension)

        self.menubar.addAction(self.view.menuAction())

        if settings.TOOLS_EXTENSION_SHOW:
            self.tools_extension.setChecked(True)

        if settings.TOOLBAR_SHOW:
            self.toolbar.setChecked(True)

        if settings.STATUSBAR_SHOW:
            self.statusbar.setChecked(True)

        if settings.GROUP_TREE_SHOW:
            self.group_info.setChecked(True)

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.view.setTitle(_translate("MenubarUI", "查看"))
        self.tools_extension.setText(_translate("MenubarUI", "工具扩展"))
        self.toolbar.setText(_translate("MenubarUI", "工具导航"))
        self.statusbar.setText(_translate("MenubarUI", "状态栏"))
        self.group_info.setText(_translate("MenubarUI", "分组信息"))

    def tools_extension_receive(self) -> None:
        """
        菜单栏 -> 工具扩展
        :return:
        """
        if self.tools_extension.isChecked():
            communicate.tools_extension_show.emit(True)
        else:
            communicate.tools_extension_show.emit(False)

    def group_info_receive(self) -> None:
        """
        菜单栏 -> 分组信息
        :return:
        """
        if self.group_info.isChecked():
            communicate.group_tree_show.emit(True)
        else:
            communicate.group_tree_show.emit(False)

    def toolbar_receive(self) -> None:
        """
        菜单栏 -> 工具栏是否显示
        :return:
        """
        if self.toolbar.isChecked():
            communicate.toolbar_show.emit(True)
        else:
            communicate.toolbar_show.emit(False)

    def statusbar_receive(self) -> None:
        """
        菜单栏 -> 状态栏
        :return:
        """
        if self.statusbar.isChecked():
            communicate.statusbar_show.emit(True)
        else:
            communicate.statusbar_show.emit(False)


class HelpMenu(object):
    def __init__(self, menubar: QMenuBar, main_window: QMainWindow):
        """
        帮助
        :param menubar:
        :param main_window:
        """
        self.menubar = menubar
        self.main_window = main_window

        # 向菜单栏中添加新的QMenu对象，父菜单
        self.help = QMenu(self.menubar)

        # 关于
        self.about = QAction(QIcon(settings.MENUBAR_UI["about"]), '&Tools Extension', self.menubar)

        self.about_ui = AboutUI()

    def setup_ui(self) -> None:
        self.about.setObjectName("tools_extension")
        self.help.addAction(self.about)
        self.about.triggered.connect(self.about_receive)

        self.menubar.addAction(self.help.menuAction())

        self.about_ui.setup_ui()
        self.about_ui.retranslate_ui()

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.help.setTitle(_translate("MenubarUI", "帮助"))
        self.about.setText(_translate("MenubarUI", "关于"))

    def about_receive(self) -> None:
        self.about_ui.show()


class MenubarUI(object):
    def __init__(self, main_window: QMainWindow):
        """
        菜单栏
        外观模式
        :param main_window:
        """
        self.main_window = main_window

        self.menubar = QMenuBar(main_window)

        self.menu_list = []
        self.option_menu = OptionMenu(self.menubar, self.main_window)
        self.view_menu = ViewMenu(self.menubar)
        self.help_menu = HelpMenu(self.menubar, self.main_window)

    def setup_ui(self) -> None:
        font = QFont()
        font.setPointSize(10)
        self.menubar.setFont(font)

        # self.menubar.setGeometry(QRect(0, 0, 800, 25))
        self.menubar.setFixedHeight(30)
        self.menubar.setObjectName("menubar")
        self.main_window.setMenuBar(self.menubar)

        self.load_ui()
        self.show_ui()

        if settings.LOAD_EFFECT_ON:
            load_animation.load_animation(self.menubar)

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.menubar.setWindowTitle(_translate("MenubarUI", "菜单栏"))

    def load_ui(self) -> None:
        """
        加载模块
        :return:
        """
        self.menu_list.append(self.option_menu)
        self.menu_list.append(self.view_menu)
        self.menu_list.append(self.help_menu)

    def show_ui(self) -> None:
        """
        显示数据
        :return:
        """
        for view in self.menu_list:
            view.setup_ui()
            view.retranslate_ui()


class MenubarConnect(object):
    def __init__(self, menubar_ui: MenubarUI):
        self.menubar_ui = menubar_ui

        # 创建调色板
        self.palette = QPalette()

    def setup_ui(self) -> None:
        self.communicate_connect()

    def communicate_connect(self) -> None:
        # 菜单中工具导航
        communicate.toolbar_checked.connect(self.toolbar_checked)
        # 菜单中工具扩展
        communicate.tools_extension_checked.connect(self.tools_extension_checked)
        # 菜单中状态栏
        communicate.statusbar_checked.connect(self.statusbar_checked)
        # 菜单中分组信息
        communicate.group_tree_checked.connect(self.group_tree_checked)

        # about 皮肤调节
        communicate.skin_color.connect(self.skin_color_about)

    def group_tree_checked(self, flag: bool) -> None:
        if flag:
            # 菜单栏选中
            self.menubar_ui.view_menu.group_info.setChecked(True)
        else:
            # 菜单栏取消
            self.menubar_ui.view_menu.group_info.setChecked(False)

    def toolbar_checked(self, flag: bool) -> None:
        if flag:
            # 菜单栏选中
            self.menubar_ui.view_menu.toolbar.setChecked(True)
        else:
            # 菜单栏取消
            self.menubar_ui.view_menu.toolbar.setChecked(False)

    def tools_extension_checked(self, flag: bool) -> None:
        if flag:
            # 菜单栏选中
            self.menubar_ui.view_menu.tools_extension.setChecked(True)
        else:
            # 菜单栏取消
            self.menubar_ui.view_menu.tools_extension.setChecked(False)

    def statusbar_checked(self, flag: bool) -> None:
        if flag:
            # 菜单栏选中
            self.menubar_ui.view_menu.statusbar.setChecked(True)
        else:
            # 菜单栏取消
            self.menubar_ui.view_menu.statusbar.setChecked(False)

    def skin_color_about(self, event: QColor):
        """
        about 皮肤调节
        :param event:
        :return:
        """
        self.palette.setColor(QPalette.Background, event)  # 给调色板设置颜色
        # 给控件设置颜色
        if event.isValid():
            self.menubar_ui.help_menu.about_ui.layout_widget.setStyleSheet(
                'QWidget {background-color:%s}' % event.name())
            self.menubar_ui.help_menu.about_ui.layout_widget.setPalette(self.palette)

    def retranslate_ui(self) -> None:
        pass
