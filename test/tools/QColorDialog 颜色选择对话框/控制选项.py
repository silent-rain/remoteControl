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

        # self.cd.setOption(QColorDialog.NoButtons)  #选项控制--单个选项
        # QColorDialog.NoButtons   不显示“ 确定”和“ 取消”按钮。（对“实时对话框”有用）
        # 参数2 on 表示有效    False表示取消

        self.cd.setOptions(QColorDialog.NoButtons | QColorDialog.ShowAlphaChannel)  # 选项控制--多个选项
        # QColorDialog.ShowAlphaChannel   对话框中增加alpha设置项

        self.cd.currentColorChanged.connect(self.BB)  # 当前颜色变化时发出信号

    def BB(self):
        s = self.cd.currentColor()  # 返回当前颜色
        # setCurrentColor(QColor())   设置当前颜色
        self.pl.setColor(QPalette.Background, s)
        self.setPalette(self.pl)

    def AA(self):
        r = self.cd.exec()
        if r:
            self.pl.setColor(QPalette.Background, self.cd.selectedColor())  # 给调色板设置颜色
            self.setPalette(self.pl)  # 给控件设置颜色


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
