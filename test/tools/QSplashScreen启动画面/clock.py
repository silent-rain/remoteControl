# -*- coding: utf-8 -*-
# 时钟
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

from PyQt5.QtWidgets import QLCDNumber, QApplication


class DigiClock(QLCDNumber):
    def __init__(self, parent=None):
        super(DigiClock, self).__init__(parent)

        p = self.palette()
        p.setColor(QPalette.Window, Qt.red)
        self.setPalette(p)

        self.setNumDigits(19)
        self.dragPosition = None

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(0.5)  # 1表示100%显示， 0.5 透明度50%

        timer = QTimer(self)
        # self.connect(timer, SIGNAL("timeout()"), self.showTime)
        print(dir(self))
        timer.start(1000)

        self.showTime()
        self.resize(500, 60)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
        if event.button() == Qt.RightButton:
            self.close()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def showTime(self):
        time = QTime.currentTime()
        date = QDate.currentDate()
        text = date.toString("yyyy-MM-dd") + " " + time.toString("hh:mm:ss")
        self.display(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = DigiClock()
    form.show()
    app.exec_()
