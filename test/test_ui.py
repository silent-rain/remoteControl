# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
# from ui.skin_palette import Ui_Form
# from bin.ui_view.utils.skin_palette import SkinPaletteView
# from bin.ui_view.utils.skincolordialog import SkinColorDialogView
from ui.tools_extension import Ui_MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = QMainWindow(None, Qt.WindowFlags())
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    ui.retranslateUi(main_window)
    main_window.show()

    sys.exit(app.exec_())
