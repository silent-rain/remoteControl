#! /usr/bin/env python

# -*- coding:utf-8 -*-


import sys

from PyQt5.QtWidgets import QApplication, QWidget

from PyQt5.QtCore import Qt

from PyQt5.QtGui import QCursor


class NoBorderWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.window_UI()

    def window_UI(self):
        self.resize(600, 200)
        self.setWindowFlags(Qt.FramelessWindowHint)

    # 重新定义鼠标事件
    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.drag = True
            self.dragPosition = QMouseEvent.globalPos() - self.pos()
            QMouseEvent.accept()
            self.setCursor(QCursor(Qt.PointingHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.drag:
            self.move(QMouseEvent.globalPos() - self.dragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.drag = False
        QMouseEvent.accept()
        self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = NoBorderWindow()
    win.show()
    sys.exit(app.exec_())
