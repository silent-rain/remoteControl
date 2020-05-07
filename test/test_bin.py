# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

# from bin.ui_view.utils.skin_palette import SkinPaletteView
from bin.ui_view.utils.skincolordialog import SkinColorDialogUI
# from skincolordialog import SkinColorDialogView
# from bin.ui_view.utils.about import AboutUI
from lib import settings
from lib.play_music import PlayMusic

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = QMainWindow(None, Qt.WindowFlags())

    # ui = SkinColorDialogUI(main_window)
    # ui.run()
    # ui.setup_ui()
    # ui.retranslate_ui()

    s = PlayMusic()
    for i in range(20):
        s.open(settings.SOUND_ONLINE)
        s.stop()
        s.start(1)
        s.open(settings.SOUND_ONLINE)


    main_window.show()

    sys.exit(app.exec_())
