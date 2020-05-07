# -*- coding: utf-8 -*-
import sys
from time import sleep
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QSplashScreen
from PyQt5.QtWidgets import qApp

from bin.ui_view.info_display import DisplayInfoUI, GroupInfoUI, GroupInfoRightMenuConnect, GroupInfoConnect
from bin.ui_view.main_window import MainWindowUI
from bin.ui_view.toolbar import ToolbarUI, ToolbarConnect
from bin.ui_view.statusbar import StatusbarUI, StatusbarConnect
from bin.ui_view.menubar import MenubarUI, MenubarConnect
from bin.ui_view.tools_extension.tools_extension import ToolsExtensionUI, ToolsExtensionConnect
from bin.ui_view.utils.skincolordialog import SkinColorDialogConnect, WindowTransparentConnect
from lib import settings
from lib.logger import logger
from lib.mysql.admin import ORMConnect


class LoadingUI(object):
    def __init__(self, main_window: QMainWindow):
        """
        启动动画
        """
        self.main_window = main_window

        self.splash = QSplashScreen()

    def setup_ui(self) -> None:
        font = QFont()
        font.setPointSize(12)
        self.splash.setFont(font)

        # 因为QSplashScreen类实现的组件本身就是无边框界面所以我们可以省略Qt::FramelessWindowHint
        # self.splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        # 正确的写法是只添加Qt::WindowStaysOnTopHint标志
        # setWindowFlags(Qt.WindowStaysOnTopHint)

        # 设置全屏显示
        # self.splash.showFullScreen()

        # 加载图片
        # self.splash.setPixmap(QPixmap(":/images/loading.png"))
        # self.splash.setPixmap(QPixmap(settings.MAIN_UI["background"]))
        self.splash.setPixmap(QPixmap(settings.MAIN_UI["loading"]))

        # 显示信息
        self.splash.showMessage("系统正在启动中...", Qt.AlignHCenter | Qt.AlignBottom, Qt.white)
        # self.splash.showMessage("加载... 0%", Qt.AlignHCenter | Qt.AlignBottom, Qt.white)
        logger.debug("系统正在启动中...")

        self.splash.show()  # 显示启动界面
        # qApp.processEvents()  # 允许主进程处理事件

        # 加载数据
        # self.load_data()

        # self.main_window.show()
        # self.splash.finish(self.main_window)  # 隐藏启动界面

    def load_data(self) -> None:
        """
        模拟加载数据
        :return:
        """
        for i in range(1, 5):  # 模拟主程序加载过程
            # time.sleep(1)  # 加载数据
            msg = "加载... {0}%".format(i * 10)
            self.splash.showMessage(msg, Qt.AlignHCenter | Qt.AlignBottom, Qt.red)
            logger.debug(msg)
            qApp.processEvents()  # 允许主进程处理事件


class MainUI(LoadingUI):
    def __init__(self, main_window: QMainWindow):
        """
        外观模式
        :param main_window:
        """
        super().__init__(main_window)
        self.main_window = main_window

        # UI 加载
        self.ui_list = []
        self.main_window_ui = MainWindowUI(self.main_window)  # 主窗口
        self.menubar_ui = MenubarUI(self.main_window)  # 菜单栏
        self.toolbar_ui = ToolbarUI(self.main_window)  # 工具导航
        self.display_info_ui = DisplayInfoUI(self.main_window)  # 信息展示
        self.group_info_ui = GroupInfoUI(self.main_window)  # 分组信息
        self.tools_extension_ui = ToolsExtensionUI(self.main_window)  # 工具扩展
        self.statusbar_ui = StatusbarUI(self.main_window)  # 状态栏

        # 模块信号
        self.connect_list = []
        # self.main_window_connect = MainWindowConnect(self.main_window_ui)  # 主窗口信号
        self.menubar_connect = MenubarConnect(self.menubar_ui)  # 菜单栏信号
        self.toolbar_connect = ToolbarConnect(self.toolbar_ui)  # 工具导航信号
        self.group_info_connect = GroupInfoConnect(self.group_info_ui, self.display_info_ui)  # 分组信息信号
        self.group_info_right_menu_connect = GroupInfoRightMenuConnect(self.group_info_ui)  # 分组信息右键信号
        self.tools_extension_connect = ToolsExtensionConnect(self.tools_extension_ui)  # 工具扩展信号; 主要加载日志信号
        self.statusbar_connect = StatusbarConnect(self.statusbar_ui)  # 状态栏信号

        # 观察者模式
        self.skin_color_dialog_connect = SkinColorDialogConnect()  # 皮肤调节信号
        self.window_transparent_connect = WindowTransparentConnect()  # 透明度装饰

        # 插件
        self.orm_connect = ORMConnect()  # 数据库注册

    def load_ui(self) -> None:
        """
        加载UI模块
        :return:
        """
        self.ui_list.append(self.main_window_ui)
        self.ui_list.append(self.menubar_ui)
        self.ui_list.append(self.toolbar_ui)
        self.ui_list.append(self.display_info_ui)
        self.ui_list.append(self.group_info_ui)
        self.ui_list.append(self.tools_extension_ui)
        self.ui_list.append(self.statusbar_ui)

    def load_connect(self) -> None:
        """
        加载 链接信号
        :return:
        """
        # 外观模式
        self.connect_list.append(self.menubar_connect)
        self.connect_list.append(self.toolbar_connect)
        self.connect_list.append(self.tools_extension_connect)
        self.connect_list.append(self.group_info_connect)
        self.connect_list.append(self.group_info_right_menu_connect)
        self.connect_list.append(self.statusbar_connect)

        # 观察者
        self.connect_list.append(self.skin_color_dialog_connect)
        self.connect_list.append(self.window_transparent_connect)

        # 插件
        self.connect_list.append(self.orm_connect)

    def load_window(self) -> None:
        """
        皮肤调节
        加载更新对象
        :return:
        """
        self.skin_color_dialog_connect.load_window(self.main_window)
        self.skin_color_dialog_connect.load_window(self.menubar_ui.help_menu.about_ui.layout_widget)

    def load_transparent(self) -> None:
        """
        窗口透明度加载
        :return:
        """
        self.window_transparent_connect.load_window(self.main_window)
        self.window_transparent_connect.load_window(self.menubar_ui.help_menu.about_ui.layout_widget)

    def show_ui(self) -> None:
        """
        显示数据
        :return:
        """
        all_list = self.ui_list + self.connect_list
        length = len(all_list)
        for index in range(length):
            view = all_list[index]
            view.setup_ui()
            view.retranslate_ui()

            sleep(settings.LOAD_DELAY)  # 加载延迟
            meg = "正在加载组件{0}... {1}%".format("", self.progress_count(index, length))
            self.splash.showMessage(meg, Qt.AlignHCenter | Qt.AlignBottom, Qt.black)
            # qApp.processEvents()  # 允许主进程处理事件

        self.splash.showMessage("组件加载完成...", Qt.AlignHCenter | Qt.AlignBottom, Qt.black)
        logger.debug("系统信息 - 组件加载完成...")
        if settings.DEBUG:
            logger.debug("系统信息 - 当前DEBUG模式...")

    @staticmethod
    def progress_count(index: int, total: int) -> int:
        """
        百分比计算
        :param index:
        :param total:
        :return:
        """
        percentage = int((index / total) * 100)
        return percentage

    def setup_ui(self) -> None:
        super().setup_ui()
        self.load_ui()
        self.load_connect()
        self.load_window()
        self.load_transparent()
        self.show_ui()

        self.splash.finish(self.main_window)  # 隐藏启动界面

        logger.info("系统信息 - 系统启动成功...")
        logger.info("申明 - 本软件使用于学习软件开发,请不要触犯法律,否则后果自负,一切与原作者无关.")


class MainApp(object):
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = QMainWindow(None, Qt.WindowFlags())

        self.main_ui = MainUI(self.main_window)

    def setup_ui(self) -> None:
        self.main_ui.setup_ui()
        # self.app.processEvents()  # 设置启动画面不影响其他效果
        self.main_window.show()
        sys.exit(self.app.exec_())
