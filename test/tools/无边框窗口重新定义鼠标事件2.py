#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QMouseEvent


class NoBorderWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.drag = True
        self.drag_position = 0

    def setup_ui(self) -> None:
        self.resize(600, 200)
        self.setWindowFlags(Qt.FramelessWindowHint)

    # 重新定义鼠标事件
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.PointingHandCursor))

    def mouseMoveEvent(self, event: QMouseEvent):
        if Qt.LeftButton and self.drag:
            self.move(event.globalPos() - self.drag_position)
            event.accept()

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.drag = False
        event.accept()
        self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = NoBorderWindow()
    win.setup_ui()
    win.show()
    sys.exit(app.exec_())
