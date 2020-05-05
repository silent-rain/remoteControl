# -*- coding: utf-8 -*-
from PyQt5.QtCore import QEasingCurve, QPropertyAnimation, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QSplashScreen

from lib import settings
from lib.settings import TRANSPARENT

"""
加载效果
退出效果
"""


def load_animation(window: object, property_name: bytes = b'windowOpacity'):
    animation = QPropertyAnimation()
    animation.setTargetObject(window)  # 设置动画目标对象

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
    animation.setStartValue(0.2)  # 设置开始不透明
    animation.setKeyValueAt(0.2, 0.4)  # 在动画的某时间点插入一个值
    animation.setKeyValueAt(0.4, 0.6)
    animation.setKeyValueAt(1, 1)  # 在动画的结束点是不透明的
    # 0透明, 1不透明
    # animation.setEndValue(1)  # 设置结束透明度
    animation.setEndValue(TRANSPARENT)  # 设置结束透明度

    animation.setDirection(3000)  # 设置动画单次时长---单位毫秒

    animation.setEasingCurve(QEasingCurve.InQuad)  # 设置动画的节奏
    animation.start()  # 动画开始---非阻塞


def loading():
    splash = QSplashScreen()
    # splash.setPixmap(QPixmap(":/images/loading.png"))
    splash.setPixmap(QPixmap(settings.MAIN_UI["loading"]))
    splash.show()
    top_right = Qt.AlignRight | Qt.AlignTop
    splash.showMessage("正在启动中", top_right, Qt.white)

    # QSplashScreen * splash = new QSplashScreen;
    # splash->setPixmap(QPixmap(“: / images / start.png”));
    # splash->show();

    # Qt::Alignment
    # top_right = Qt::AlignRight | Qt::AlignTop;
    # splash->showMessage(“正在启动中”, top_right, Qt::white);
    # mainWindows
    # window;
    # window.show();
    # splash->finish( & window);
    # delete
    # splash
