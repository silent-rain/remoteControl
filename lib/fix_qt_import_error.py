# -*- coding:utf-8 -*-
# Fix qt import error
# Include this file before import PyQt5
import os
import sys

"""
Qt打包报错补丁
"""


def fix_qt_import_error_append_run_path() -> None:
    if getattr(sys, 'frozen', False):
        pathlist = []

        # If the application is run as a bundle, the pyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app
        # path into variable _MEIPASS'.
        pathlist.append(sys._MEIPASS)

        # the application exe path
        _main_app_path = os.path.dirname(sys.executable)
        pathlist.append(_main_app_path)

        # append to system path enviroment
        os.environ["PATH"] += os.pathsep + os.pathsep.join(pathlist)


fix_qt_import_error_append_run_path()
