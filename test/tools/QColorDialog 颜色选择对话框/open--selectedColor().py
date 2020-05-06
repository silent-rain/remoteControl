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

    def color(self):
        self.pl.setColor(QPalette.Background, self.cd.selectedColor())  # 给调色板设置颜色
        # QPalette.Background   表示设置背景色
        # QPalette.WindowText  表示设置文本颜色
        # selectedColor()  返回最终选择的颜色
        self.setPalette(self.pl)  # 给控件设置颜色
        pass

    def AA(self):
        self.cd.open(self.color)  # 点击确定按钮时会自动执行槽函数


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())