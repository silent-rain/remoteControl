# -*- coding: utf-8 -*-
import sys
from time import sleep
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QSplashScreen
from PyQt5.QtWidgets import qApp
from bin.ui_view.main_window import MainWindowView
from bin.ui_view.toolbar import ToolbarUI, ToolbarConnect
from bin.ui_view.statusbar import StatusbarUI, StatusbarConnect
from bin.ui_view.menubar import MenubarUI, MenubarConnect
from bin.ui_view.tools_extension.loginfo import LogInfoConnect, LogInfoUI
from bin.ui_view.tools_extension.tools_extension import ToolsExtensionUI, ToolsExtensionConnect
from lib import settings
from lib.logger import logger


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

    def load_data(self):
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

        self.ui_view_list = []

    def add_ui(self, ui: object) -> None:
        """
        添加模块
        :param ui: 模块对象
        :return:
        """
        if ui not in self.ui_view_list:
            self.ui_view_list.append(ui)

    def load_ui(self) -> None:
        """
        加载模块
        :return:
        """
        self.add_ui(MainWindowView(self.main_window))  # 主窗口
        self.add_ui(MenubarUI(self.main_window))  # 菜单栏
        self.add_ui(ToolbarUI(self.main_window))  # 工具导航
        self.add_ui(ToolsExtensionUI(self.main_window))  # 工具扩展
        self.add_ui(StatusbarUI(self.main_window))  # 状态栏

    def load_connect(self) -> None:
        """
        加载功能链接
        :return:
        """
        # self.add_ui(MainWindowView(self.main_window))  # 主窗口信号
        self.add_ui(MenubarConnect(self.main_window))  # 菜单栏信号
        self.add_ui(ToolbarConnect(self.main_window))  # 工具导航信号
        self.add_ui(ToolsExtensionConnect(self.main_window))  # 工具扩展信号
        self.add_ui(StatusbarConnect(self.main_window))  # 状态栏信号

    def load_tools_extension(self) -> None:
        """
        工具扩展的链接
        # ToolsExtension Connect
        :return:
        """
        self.add_ui(LogInfoConnect(LogInfoUI(ToolsExtensionUI(self.main_window).tab_widget)))

    def show_ui(self) -> None:
        """
        显示数据
        :return:
        """
        length = len(self.ui_view_list)
        for index in range(length):
            view = self.ui_view_list[index]
            view.setup_ui()
            view.retranslate_ui()

            sleep(settings.LOAD_DELAY)  # 加载延迟
            meg = "正在加载组件{0}... {1}%".format("", self.progress_count(index, length))
            self.splash.showMessage(meg, Qt.AlignHCenter | Qt.AlignBottom, Qt.black)
            logger.debug(meg)
            # qApp.processEvents()  # 允许主进程处理事件

        self.splash.showMessage("组件加载完成...", Qt.AlignHCenter | Qt.AlignBottom, Qt.black)
        logger.debug("组件加载完成...")

    @staticmethod
    def progress_count(index: int, total: int) -> int:
        percentage = int((index / total) * 100)
        return percentage

    def setup_ui(self) -> None:
        super().setup_ui()
        self.load_ui()
        self.load_connect()
        self.load_tools_extension()
        self.show_ui()
        self.splash.finish(self.main_window)  # 隐藏启动界面
        logger.info("系统信息 - 系统启动成功...")
        logger.info("申明 - 本软件使用于学习网络安全,请不要触犯法律,否则后果自负,一切与原作者无关.")
        logger.info("系统信息 - 本地IP:  [{}]    监听端口:  [{}]".format(settings.IP, settings.PORT))


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
