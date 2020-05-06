# -*- coding:utf8 -*-
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys, time
from clock import DigiClock


class SplashScreen(QSplashScreen):
    def __init__(self):
        super(SplashScreen, self).__init__(QPixmap("clock.png"))  # 启动程序的图片

    # 效果 fade =1 淡入   fade= 2  淡出，  t sleep 时间 毫秒
    def effect(self):
        self.setWindowOpacity(0)
        t = 0
        while t <= 50:
            newOpacity = self.windowOpacity() + 0.02  # 设置淡入
            if newOpacity > 1:
                break

            self.setWindowOpacity(newOpacity)
            self.show()
            t -= 1
            time.sleep(0.04)

        time.sleep(1)
        t = 0
        while t <= 50:
            newOpacity = self.windowOpacity() - 0.02  # 设置淡出
            if newOpacity < 0:
                break

            self.setWindowOpacity(newOpacity)
            t += 1
            time.sleep(0.04)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    splash = SplashScreen()
    splash.effect()
    app.processEvents()  # ＃设置启动画面不影响其他效果
    window = DigiClock()  # 程序的主类
    window.show()
    splash.finish(window)  # 启动画面完成启动
    sys.exit(app.exec_())
