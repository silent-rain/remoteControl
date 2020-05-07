# -*- coding: utf-8 -*-
import sys
import os

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

from lib import basePath
from bin.main_app import MainApp

if basePath:
    # 防止被软件清理
    pass

if __name__ == '__main__':
    app = MainApp()
    app.setup_ui()
