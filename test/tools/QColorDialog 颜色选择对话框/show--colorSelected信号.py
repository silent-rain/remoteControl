import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog, QLabel
from PyQt5.QtGui import QColor, QPalette


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.main_window = self

        # 初始化颜色
        self.color = QColor(107, 173, 246)
        # 创建颜色对话框--但不显示
        self.color_dialog = QColorDialog(self.color, self.main_window)

        # 创建调色板
        self.palette = QPalette()

    def setup_ui(self) -> None:
        # 颜色选取信号
        # 会向槽函数传递一个值---QColor
        # self.color_dialog.colorSelected.connect(self.update_color)  # 选中最终颜色时发出信号-点击对话框的确定按钮时
        self.color_dialog.currentColorChanged.connect(self.update_color)  # 当前颜色变化时

        # self.cd.setOption(QColorDialog.NoButtons)  #选项控制--单个选项
        # QColorDialog.NoButtons   不显示“ 确定”和“ 取消”按钮。（对“实时对话框”有用）
        # QColorDialog.ShowAlphaChannel   对话框中增加alpha设置项
        self.color_dialog.setOptions(QColorDialog.NoButtons | QColorDialog.ShowAlphaChannel)  # 选项控制--多个选项

        # 打开对话框,获取颜色
        # noinspection PyCallByClass
        # self.color = self.color_dialog.getColor(self.color, None)

        # 打开对话框
        self.color_dialog.show()

    def update_color2(self, event: QColor):
        self.palette.setColor(QPalette.Background, event)  # 给调色板设置颜色
        self.setPalette(self.palette)  # 给控件设置颜色

    def update_color(self, event: QColor) -> None:
        # print(event, type(event))
        # print(self.color_dialog.selectedColor(), type(self.color_dialog.selectedColor()))

        # QPalette.Background   表示设置背景色
        # QPalette.WindowText  表示设置文本颜色
        self.palette.setColor(QPalette.Background, event)  # 给调色板设置颜色
        # self.palette.setColor(QPalette.Background, self.color_dialog.selectedColor())  # 给调色板设置颜色

        self.main_window.setPalette(self.palette)  # 给控件设置颜色


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.setup_ui()
    demo.show()
    sys.exit(app.exec_())
