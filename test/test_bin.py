# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

# from bin.ui_view.utils.skin_palette import SkinPaletteView
from bin.ui_view.utils.skincolordialog import SkinColorDialogView
# from skincolordialog import SkinColorDialogView
# from bin.ui_view.utils.about import AboutUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = QMainWindow(None, Qt.WindowFlags())

    ui = SkinColorDialogView(main_window)
    ui.run()
    # ui.setup_ui()
    # ui.retranslate_ui()

    main_window.show()

    sys.exit(app.exec_())
