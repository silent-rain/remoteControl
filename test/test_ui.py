# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
# from ui.skin_palette import Ui_Form
from ui.group_tree import Ui_Form

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = QMainWindow(None, Qt.WindowFlags())
    ui = Ui_Form()
    ui.setupUi(main_window)
    ui.retranslateUi(main_window)
    main_window.show()

    sys.exit(app.exec_())
