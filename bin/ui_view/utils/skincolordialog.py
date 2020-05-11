# -*- coding: utf-8 -*-
from PyQt5.QtGui import QColor, QPalette, QBrush
from PyQt5.QtWidgets import QColorDialog, QWidget
from PyQt5.QtCore import QCoreApplication, QPropertyAnimation

from lib import settings
from lib.communicate import communicate

"""
皮肤调色模块
"""

_translate = QCoreApplication.translate


class SkinColorDialogUI(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 初始化颜色
        self.color = QColor(*settings.SKIN_COLOR)
        # 创建颜色对话框--但不显示
        # self.color_dialog = QColorDialog(self.color, self.main_window)
        self.color_dialog = QColorDialog(self.color, self)

        # 创建调色板
        self.palette = QPalette()

        self.options()

    def update_color(self, event: QColor) -> None:
        """
        更新颜色
        两种方式同时
        :param event:
        :return:
        """
        # print(event, type(event))
        # print(self.color_dialog.selectedColor(), type(self.color_dialog.selectedColor()))

        # QPalette.Background   表示设置背景色
        # QPalette.WindowText  表示设置文本颜色
        self.palette.setColor(QPalette.Background, event)  # 给调色板设置颜色
        self.palette.setBrush(QPalette.Base, QBrush(QColor(*event.getRgb())))
        # self.palette.setColor(QPalette.Background, self.color_dialog.selectedColor())  # 给调色板设置颜色

        # 给控件设置颜色
        if event.isValid():
            # self.main_window.setStyleSheet('QWidget {background-color:%s}' % event.name())
            # self.main_window.setPalette(self.palette)
            self.color_dialog.setStyleSheet('QWidget {background-color:%s}' % event.name())
            self.color_dialog.setPalette(self.palette)
            # 发色信号
            communicate.skin_color.emit(event)

    def options(self) -> None:
        """
        参数设置
        """
        # 颜色选取信号
        # 会向槽函数传递一个值---QColor
        # self.color_dialog.colorSelected.connect(self.update_color)  # 选中最终颜色时发出信号-点击对话框的确定按钮时
        self.color_dialog.currentColorChanged.connect(self.update_color)  # 当前颜色变化时

        # self.cd.setOption(QColorDialog.NoButtons)  #选项控制--单个选项
        # QColorDialog.NoButtons   不显示“ 确定”和“ 取消”按钮。（对“实时对话框”有用）
        # QColorDialog.ShowAlphaChannel   对话框中增加alpha设置项
        self.color_dialog.setOptions(QColorDialog.NoButtons | QColorDialog.ShowAlphaChannel)  # 选项控制--多个选项

        # 打开对话框,会等待完成
        # noinspection PyCallByClass
        # self.color_dialog.getColor(self.color, None)

        # 最终回调函数
        self.color_dialog.finished.connect(self.finished_color)

    def setup_ui(self) -> None:
        # 打开对话框,等待打开
        # self.color_dialog.open()
        self.color_dialog.show()

    def finished_color(self, event: int) -> None:
        """
        设置颜色到全局变量
        :param event:
        :return:
        """
        if event:
            pass
        color = self.color_dialog.currentColor().getRgb()[:3]
        settings.SKIN_COLOR = color


class SkinColorDialogConnect(object):
    def __init__(self):
        """
        皮肤调节 信号
        观察者模式
        """
        self.window_list = []

        # 创建调色板
        self.palette = QPalette()

    def setup_ui(self) -> None:
        self.communicate_connect()

    def retranslate_ui(self) -> None:
        pass

    def communicate_connect(self) -> None:
        # 皮肤调节
        communicate.skin_color.connect(self.update_window_skin_color)

    def load_window(self, window: object) -> None:
        """
        加载窗口对象
        :return:
        """
        self.window_list.append(window)

    def update_window_skin_color(self, event: QPalette) -> None:
        """
        窗口皮肤调节
        :return:
        """
        # 给控件设置颜色
        if event.isValid():
            self.palette.setColor(QPalette.Background, event)  # 给调色板设置颜色
            self.palette.setBrush(QPalette.Base, QBrush(QColor(*event.getRgb())))

            for window in self.window_list:
                # self.main_window_ui.main_window.setStyleSheet('QWidget {background-color:%s}' % event.name())
                # self.main_window_ui.main_window.setPalette(self.palette)
                # window.setStyleSheet('QWidget {background-color:%s}' % event.name())  # 控件
                window.setStyleSheet("background-color: rgb{};".format(event.getRgb()[:3]))
                window.setPalette(self.palette)


class WindowTransparentConnect2(object):
    def __init__(self):
        """
        窗口如透明效果,非阻塞
        观察者模式
        废弃
        """
        self.window_list = []
        self.load_window_list = []

        # 创建调色板
        self.palette = QPalette()
        # 颜色初始化
        # self.color_init = QColor(107, 173, 246)
        self.color_init = QColor(*settings.SKIN_COLOR)

    @staticmethod
    def options(animation: QPropertyAnimation, property_name: bytes = b'windowOpacity') -> None:
        """
        废弃
        更改透明度
        :param animation:
        :param property_name:
        :return:
        """
        # 创建对象

        # 设置动画属性
        # 注意：字节类型
        # pos---位置动画---QPoint
        # size---大小动画---QSize
        # geometry----位置+大小动画----QRect
        # windowOpacity---窗口的透明度(0.0是透明的    1.0是不透明)---好像只适合顶层窗口
        animation.setPropertyName(property_name)

        # animation.setStartValue(QPoint(0, 0))  # 设置开始位置---按钮的左上角位置
        # animation.setEndValue(QPoint(300, 300))  # 设置结束位置
        # animation.setStartValue(QSize(0, 0))  # 设置开始大小
        # animation.setEndValue(QSize(300, 300))  # 设置结束大小
        # animation.setStartValue(QRect(0, 0,100,100))  # 设置开始位置和大小
        # animation.setEndValue(QRect(100,100,300, 300))  # 设置结束位置和大小

        # 参数1 0.0到1.0  0.0表示开始点，1.0表示结束点
        # 在动画的中间插入透明度0.2
        # animation.setStartValue(0.2)  # 设置开始不透明
        # animation.setKeyValueAt(0.2, 0.4)  # 在动画的某时间点插入一个值
        # animation.setKeyValueAt(0.4, 0.6)
        # animation.setKeyValueAt(1, 1)  # 在动画的结束点是不透明的
        # 0透明, 1不透明
        # animation.setEndValue(1)  # 设置结束透明度
        animation.setEndValue(settings.TRANSPARENT)  # 设置结束透明度

        # animation.setDirection(3000)  # 设置动画单次时长---单位毫秒

        # animation.setEasingCurve(QEasingCurve.InQuad)  # 设置动画的节奏
        animation.start()  # 动画开始---非阻塞

    def stop(self) -> None:
        """
        效果全部终止
        :return:
        """
        for window in self.load_window_list:
            window.stop()

    def setup_ui(self) -> None:
        pass

    def retranslate_ui(self) -> None:
        pass


class WindowTransparentConnect(object):
    def __init__(self):
        """
        窗口如透明效果,非阻塞
        观察者模式
        """
        self.window_list = []
        self.load_window_list = []

        # 创建调色板
        self.palette = QPalette()
        # 颜色初始化
        # self.color_init = QColor(107, 173, 246)
        self.color_init = QColor(*settings.SKIN_COLOR)

    def options(self) -> None:
        """
        参数设置
        :return:
        """
        self.palette.setColor(QPalette.Background, self.color_init)  # 给调色板设置颜色
        # self.palette.setBrush(QPalette.Base, QBrush(QColor(255, 255, 255, 0)))
        self.palette.setBrush(QPalette.Base, QBrush(self.color_init))

    def set_window_transparent(self, window: QWidget) -> None:
        """
        设置窗口背景色
        :param window:
        :return:
        """
        # 窗口透明度
        # self.main_window.setWindowOpacity(0.5)
        window.setAutoFillBackground(True)
        window.setWindowOpacity(0.8)  # 0.0-1.0

        # 给控件设置颜色
        window.setStyleSheet("background-color: rgb{};".format(self.color_init.getRgb()[:3]))
        window.setPalette(self.palette)

    def load_window(self, window: object) -> None:
        """
        加载窗口对象
        :return:
        """
        self.window_list.append(window)

    def show_window(self) -> None:
        if not settings.LOAD_EFFECT_ON:
            # 特效模式
            return None
        for window in self.window_list:
            self.set_window_transparent(window)

    def setup_ui(self) -> None:
        self.options()
        self.show_window()

    def retranslate_ui(self) -> None:
        pass
