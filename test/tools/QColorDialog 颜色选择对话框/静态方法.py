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
        self.btn = QPushButton('按钮', self)
        self.btn.move(50, 250)
        self.btn.clicked.connect(self.AA)
        self.btn1 = QPushButton('按钮1', self)
        self.btn1.move(150, 250)
        self.btn1.clicked.connect(self.BB)

        self.pl = QPalette()  # 创建调色板

    def BB(self):
        col = QColorDialog.getColor(QColor(0, 255, 0), self, '请选择颜色')  # 显示颜色面板
        # 参数1 默认颜色
        # 参数3  标题
        # 参数4 选项--看前面
        # 用户点击确定按钮-返回值 颜色；用户点击取消按钮 返回黑色

        self.pl.setColor(QPalette.Background, col)  # 给调色板设置颜色
        self.setPalette(self.pl)  # 给控件设置颜色

        pass

    def AA(self):
        s = self.cd.customCount()  # 返回自定义颜色的格数
        s = QColorDialog.customCount()  # 返回自定义颜色的格数
        # 16
        QColorDialog.setCustomColor(0, QColor(255, 0, 0))  # 在自定义面板中自定义颜色
        # 参数1  格的序号
        # 参数2  颜色
        # 在显示之前设置好

        s = QColorDialog.customColor(0)  # 获取自定义面板的颜色 -> QColor
        # 参数 格序号

        QColorDialog.setStandardColor(5, QColor(0, 0, 255))  # 在标准颜色面板中自定义颜色
        # 参数1  格的序号
        # 参数2  颜色

        s = QColorDialog.standardColor(5)  # 获取标准颜色面板的颜色 -> QColor
        # 参数 格序号

        self.cd.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
