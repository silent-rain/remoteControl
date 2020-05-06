import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog, QLabel
from PyQt5.QtGui import QColor, QPalette


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 300)
        self.setWindowTitle('QFontDialog')

        self.label = QLabel('塘沽五中', self)
        self.label.move(100, 10)

        self.cd = QColorDialog(QColor(250, 0, 0), self)  # 创建颜色对话框--但不显示
        # 参数1  默认颜色

        self.pl = QPalette()  # 创建调色板

        btn = QPushButton('按钮', self)
        btn.move(100, 250)
        btn.clicked.connect(self.AA)

    def AA(self):
        r = self.cd.exec()  # 用户点击确定按钮返回值1；用户点击取消按钮返回值0
        if r:
            self.pl.setColor(QPalette.Background, self.cd.selectedColor())  # 给调色板设置颜色
            self.setPalette(self.pl)  # 给控件设置颜色


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
