# -*- coding: utf-8 -*-
import psutil
from PyQt5.QtWidgets import QStatusBar, QMainWindow, QLabel
from PyQt5.QtGui import QFont, QPixmap, QHideEvent
from PyQt5.QtCore import QCoreApplication, QTimer, QDateTime, QThread

from lib import settings
from lib.communicate import communicate

_translate = QCoreApplication.translate

"""
状态栏模块

ShowTime        显示时间
NetSpeed        监控网速
MonitorPort     监听端口
OnlineHost      上线主机
Placeholder     占位
"""


class ShowTime(object):
    def __init__(self, statusbar: QStatusBar, stretch: int):
        """
        显示时间
        :param statusbar:
        :param stretch:
        """
        self.statusbar = statusbar

        self.time_abel = QLabel(self.statusbar)
        self.timer = QTimer()
        self.time_text = ""
        self.stretch = stretch

    def setup_ui(self) -> None:
        self.time_abel.setFixedWidth(230)
        self.statusbar.addWidget(self.time_abel, self.stretch)

        self.timer.timeout.connect(self.time_refresh_receive)
        self.timer.start(1000)  # 设置间隔时间,否则cpu占用会上升

    def time_refresh_receive(self) -> None:
        # 获取系统当前时间
        data_time = QDateTime().currentDateTime()
        # 设置系统时间的显示格式
        time_display = 'yyyy-MM-dd hh:mm:ss dddd'
        self.time_text = data_time.toString(time_display)
        self.retranslate_ui()

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.time_abel.setText(_translate("StatusbarUI", "北京时间: " + self.time_text))


class Placeholder(object):
    def __init__(self, statusbar: QStatusBar, stretch: int):
        """
        占位
        :param statusbar:
        :param stretch:
        """
        self.statusbar = statusbar

        self.label = QLabel(self.statusbar)
        self.stretch = stretch

    def setup_ui(self) -> None:
        self.statusbar.addWidget(self.label, self.stretch)

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        pass


class OnlineHost(object):
    def __init__(self, statusbar: QStatusBar, stretch: int = -1):
        """
        上线主机
        :param statusbar:
        :param stretch:
        """
        self.statusbar = statusbar
        self.stretch = stretch

        self.online = QLabel(self.statusbar)
        self.online_icon = QLabel(self.statusbar)

        self.online_host = 0

    def set_background(self) -> None:
        """
        设置背景: 填充图片
        :return:
        """
        # 图片背景: background-image: url(:/images/background.png);
        self.online_icon.setStyleSheet("background-image: url({0});".format(settings.TOOLBAR_UI["host"]))
        # 自动填充背景
        # self.online_icon.setAutoFillBackground(True)

    def set_background2(self) -> None:
        pix = QPixmap(settings.TOOLBAR_UI["host"])
        self.online_icon.setPixmap(pix)  # 在label上显示图片

    def setup_ui(self):
        self.online_icon.setScaledContents(True)  # 让图片自适应label大
        self.online_icon.setFixedWidth(25)  # 图片宽度
        self.set_background2()

        self.online.setFixedWidth(100)

        stretch_icon = - (abs(self.stretch) + 1)
        self.statusbar.addWidget(self.online_icon, stretch_icon)
        self.statusbar.addWidget(self.online, self.stretch)

    # noinspection PyArgumentList
    def retranslate_ui(self):
        self.online.setText(_translate("StatusbarUI", "上线主机: {0} 台".format(self.online_host)))


class NetSpeedThread(QThread):
    def __init__(self):
        """
        实时网速
        """
        super().__init__()

        self.speed_recv = 0
        self.speed_sent = 0

        self.speed = None

    @property
    def get_net_speed(self) -> (str, str):
        return self.speed_recv, self.speed_sent

    def update(self, speed: QLabel) -> None:
        self.speed = speed

    @staticmethod
    def calculate(speed: int) -> str:
        t = 1024 * 1024 * 1024 * 1024  # TB/s
        g = 1024 * 1024 * 1024  # GB/s
        m = 1024 * 1024  # MB/s
        k = 1024  # KB/s

        if speed > t:
            return str("%.1f" % (speed / t)) + "TB/s"
        elif speed > g:
            return str("%.1f" % (speed / g)) + "GB/s"
        elif speed > m:
            return str("%.1f" % (speed / m)) + "MB/s"
        elif speed > k:
            return str("%.1f" % (speed / k)) + "KB/s"
        else:
            return str("%.1f" % speed) + "B/s"

    def run(self) -> None:
        old_net_recv = psutil.net_io_counters().bytes_recv
        old_net_sent = psutil.net_io_counters().bytes_sent
        while True:
            self.sleep(1)  # 睡眠时间
            new_net_recv = psutil.net_io_counters().bytes_recv
            new_net_sent = psutil.net_io_counters().bytes_sent

            self.speed_recv = self.calculate(new_net_recv - old_net_recv)
            self.speed_sent = self.calculate(new_net_sent - old_net_sent)

            if self.speed:
                self.retranslate_ui()

            old_net_recv = new_net_recv
            old_net_sent = new_net_sent

    # noinspection PyArgumentList
    def retranslate_ui(self):
        self.speed.setText(_translate("StatusbarUI",
                                      "send: %s recv: %s" % (self.speed_sent, self.speed_recv)))


class NetSpeed(object):
    def __init__(self, statusbar: QStatusBar, stretch: int):
        """
        获取网速
        :param statusbar:
        :param stretch:
        """
        self.statusbar = statusbar
        self.stretch = stretch

        self.send_recv_text = QLabel(self.statusbar)
        self.net_speed = NetSpeedThread()

    def setup_ui(self):
        self.send_recv_text.setFixedWidth(180)
        self.statusbar.addWidget(self.send_recv_text, self.stretch)

        self.net_speed.update(self.send_recv_text)
        self.net_speed.start()

    # noinspection PyArgumentList
    def retranslate_ui(self):
        self.send_recv_text.setText(_translate("StatusbarUI", "send: 0.0B/s recv: 0.0B/s"))


class MonitorPort(object):
    def __init__(self, statusbar: QStatusBar, stretch: int):
        """
        监听端口
        :param statusbar:
        :param stretch:
        """
        self.statusbar = statusbar
        self.stretch = stretch

        self.port_label = QLabel(self.statusbar)
        self.port = 0

    def setup_ui(self):
        self.port_label.setFixedWidth(110)
        self.statusbar.addWidget(self.port_label, self.stretch)

    # noinspection PyArgumentList
    def retranslate_ui(self):
        self.port_label.setText(_translate("StatusbarUI", "监控端口: %s" % settings.PORT))


class StatusbarUI(object):
    def __init__(self, main_window: QMainWindow):
        """
        状态栏
        外观模式
        :param main_window:
        """
        self.main_window = main_window

        self.statusbar = QStatusBar(self.main_window)

        self.ui_list = []
        self.show_time = ShowTime(self.statusbar, 1)  # 时间模块
        self.placeholder = Placeholder(self.statusbar, 2)  # 占位符
        self.net_speed = NetSpeed(self.statusbar, -4)  # 网速
        self.monitor_port = MonitorPort(self.statusbar, -3)  # 监听端口
        self.online_host = OnlineHost(self.statusbar, -1)  # 上线主机

    def options(self) -> None:
        font = QFont()
        font.setPointSize(10)
        self.statusbar.setFont(font)

        # self.statusbar.setGeometry(QtCore.QRect(0, 0, 900, 50))
        self.statusbar.setFixedHeight(30)
        self.main_window.setStatusBar(self.statusbar)
        # self.main_window.setStatusBar()
        # self.statusbar.setContextMenuPolicy(Qt.DefaultContextMenu)

    def setup_ui(self) -> None:
        self.statusbar.setObjectName("statusbar")
        self.options()

        self.load_ui()
        self.show_ui()

        if not settings.STATUSBAR_SHOW:
            self.statusbar.setHidden(False)

    # noinspection PyArgumentList
    def retranslate_ui(self) -> None:
        self.statusbar.setWindowTitle(_translate("StatusbarUI", "状态栏"))

    def load_ui(self) -> None:
        """
        加载模块
        :return:
        """
        self.ui_list.append(self.show_time)
        self.ui_list.append(self.placeholder)
        self.ui_list.append(self.net_speed)
        self.ui_list.append(self.monitor_port)
        self.ui_list.append(self.online_host)

    def show_ui(self) -> None:
        """
        显示数据
        :return:
        """
        for view in self.ui_list:
            view.setup_ui()
            view.retranslate_ui()


class StatusbarConnect(object):
    def __init__(self, statusbar_ui: StatusbarUI):
        self.statusbar_ui = statusbar_ui

        # self.statusbar_ui = StatusbarUI(self.main_window)
        # self.statusbar = self.statusbar_ui.statusbar

    def setup_ui(self) -> None:
        self.communicate_connect()

        self.statusbar_ui.statusbar.hideEvent = self.hide_event
        self.statusbar_ui.statusbar.showEvent = self.hide_event

    def communicate_connect(self) -> None:
        # 状态栏是否显示
        communicate.statusbar_show.connect(self.statusbar_show)

    def statusbar_show(self, flag: bool) -> None:
        if flag:
            # 显示
            self.statusbar_ui.statusbar.setHidden(False)
        else:
            # 隐藏
            self.statusbar_ui.statusbar.setHidden(True)

    def hide_event(self, event: QHideEvent):
        """
        菜单栏中的  工具导航
        :param event:
        :return:
        """
        if event:
            pass
        if self.statusbar_ui.statusbar.isHidden():
            communicate.statusbar_checked.emit(False)
        else:
            communicate.statusbar_checked.emit(True)

    def retranslate_ui(self) -> None:
        pass
