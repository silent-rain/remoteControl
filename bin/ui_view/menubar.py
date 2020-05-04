# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMenuBar, QMainWindow, QMenu, QAction
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication

from lib import settings

_translate = QCoreApplication.translate


class MenubarUI(object):
    def __new__(cls, *args, **kwargs) -> object:
        if not hasattr(cls, "_instance"):  # 反射
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, main_window: QMainWindow):
        if not hasattr(self, "_init_flag"):  # 反射
            self._init_flag = True  # 只初始化一次
            self.main_window = main_window
            self.menubar = QMenuBar(main_window)

    def setup_ui(self) -> None:
        font = QFont()
        font.setPointSize(10)
        self.menubar.setFont(font)

        # self.menubar.setGeometry(QRect(0, 0, 800, 25))
        self.menubar.setFixedHeight(30)
        self.menubar.setObjectName("menubar")
        self.main_window.setMenuBar(self.menubar)

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.menubar.setWindowTitle(_translate("MenubarUI", "菜单栏"))


class MenubarView(MenubarUI):
    ui_view_list = []

    def add_ui_view(self, view: object) -> None:
        if view not in self.ui_view_list:
            self.ui_view_list.append(view)

    def setup_ui(self) -> None:
        super().setup_ui()
        self.ui_view_list.append(OptionMenu(self.menubar, self.main_window))
        self.ui_view_list.append(ViewMenu(self.menubar))
        self.ui_view_list.append(HelpMenu(self.menubar))

        for view in self.ui_view_list:
            view.setup_ui()
            view.retranslate_ui()

    def retranslate_ui(self) -> None:
        super().retranslate_ui()


class OptionMenu(object):
    def __init__(self, menubar: QMenuBar, main_window: QMainWindow):
        self.menubar = menubar
        self.main_window = main_window

        # 向菜单栏中添加新的QMenu对象，父菜单
        self.option = QMenu(self.menubar)

        # 程序设置
        self.setting = QAction(QIcon(settings.MENUBAR_UI["setting"]), '&Setting', self.menubar)

        # 生成服务端
        self.make_server = QAction(QIcon(settings.MENUBAR_UI["make_server"]), '&Make Server', self.menubar)

        # 分隔符
        self.option.addSeparator()

        # 退出
        self.exit = QAction(QIcon(settings.MENUBAR_UI["exit"]), '&Exit', self.menubar)

    def setup_ui(self) -> None:
        self.setting.setShortcut('Ctrl+Alt+S')
        self.setting.setStatusTip('Setting')
        self.setting.setObjectName("setting")
        self.option.addAction(self.setting)
        self.setting.triggered.connect(self.setting_receive)

        self.make_server.setShortcut('Ctrl+N')
        self.make_server.setStatusTip('make server')
        self.make_server.setObjectName("make_server")
        self.option.addAction(self.make_server)
        self.make_server.triggered.connect(self.make_server_receive)

        self.exit.setShortcut('Ctrl+Q')
        self.exit.setStatusTip('Exit')
        self.exit.setObjectName("exit")
        self.option.addAction(self.exit)
        # self.exit.triggered.connect(QCoreApplication.quit)  # 直接退出程序
        self.exit.triggered.connect(self.exit_receive)

        self.menubar.addAction(self.option.menuAction())

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.option.setTitle(_translate("MenubarUI", "选项"))
        self.setting.setText(_translate("MenubarUI", "程序设置"))
        self.make_server.setText(_translate("MenubarUI", "生成服务端"))
        self.exit.setText(_translate("MenubarUI", "退出"))

    def setting_receive(self):
        """
        程序设置
        :return:
        """
        print("setting_receive")

    def make_server_receive(self):
        """
        生成服务端
        :return:
        """
        print("make_server_receive")

    def exit_receive(self):
        """
        退出程序
        :return:
        """
        self.main_window.close()


class ViewMenu(object):
    def __init__(self, menubar: QMenuBar):
        self.menubar = menubar

        # 向菜单栏中添加新的QMenu对象，父菜单
        self.view = QMenu(self.menubar)

        # 工具箱扩展
        self.tools_extension = QAction(QIcon(""), '&Tools Extension', self.menubar)

        # 工具栏
        self.toolbar = QAction(QIcon(""), '&Toolbar', self.menubar)

        # 状态栏
        self.statusbar = QAction(QIcon(""), '&Statusbar', self.menubar)

    def setup_ui(self) -> None:
        self.tools_extension.setStatusTip('Tools Extension')
        self.tools_extension.setObjectName("tools_extension")
        self.view.addAction(self.tools_extension)
        self.tools_extension.triggered.connect(self.tools_extension_receive)
        # self.tools_extension.changed.connect(self.tools_extension_receive)

        self.toolbar.setStatusTip('Toolbar')
        self.toolbar.setObjectName("toolbar")
        self.view.addAction(self.toolbar)
        self.toolbar.triggered.connect(self.toolbar_receive)

        self.statusbar.setStatusTip('Statusbar')
        self.statusbar.setObjectName("statusbar")
        self.view.addAction(self.statusbar)
        self.statusbar.triggered.connect(self.statusbar_receive)

        self.menubar.addAction(self.view.menuAction())

        self.tools_extension.setCheckable(True)
        self.toolbar.setCheckable(True)
        self.statusbar.setCheckable(True)

        if settings.TOOLS_EXTENSION_SHOW:
            self.tools_extension.setChecked(True)

        if settings.TOOLBAR_SHOW:
            self.toolbar.setChecked(True)

        if settings.STATUSBAR_SHOW:
            self.statusbar.setChecked(True)

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.view.setTitle(_translate("MenubarUI", "查看"))
        self.tools_extension.setText(_translate("MenubarUI", "工具箱"))
        self.toolbar.setText(_translate("MenubarUI", "工具栏"))
        self.statusbar.setText(_translate("MenubarUI", "状态栏"))

    def tools_extension_receive(self):
        """
        工具箱
        :return:
        """
        if self.tools_extension.isChecked():
            print("显示")
        else:
            print("隐藏")
        print("tools_extension_receive")

    def toolbar_receive(self):
        """
        工具栏
        :return:
        """
        if self.toolbar.isChecked():
            print("显示")
        else:
            print("隐藏")
        print("toolbar_receive")

    def statusbar_receive(self):
        """
        状态栏
        :return:
        """
        if self.statusbar.isChecked():
            print("显示")
        else:
            print("隐藏")
        print("statusbar_receive")


class HelpMenu(object):
    def __init__(self, menubar: QMenuBar):
        self.menubar = menubar

        # 向菜单栏中添加新的QMenu对象，父菜单
        self.help = QMenu(self.menubar)

        # 关于
        self.about = QAction(QIcon(settings.MENUBAR_UI["about"]), '&Tools Extension', self.menubar)

    def setup_ui(self) -> None:
        self.about.setStatusTip('Tools Extension')
        self.about.setObjectName("tools_extension")
        self.help.addAction(self.about)
        self.about.triggered.connect(self.about_receive)

        self.menubar.addAction(self.help.menuAction())

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.help.setTitle(_translate("MenubarUI", "帮助"))
        self.about.setText(_translate("MenubarUI", "关于"))

    def about_receive(self):
        print("about_receive")
