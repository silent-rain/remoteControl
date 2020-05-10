# -*- coding: utf-8 -*-
import os
import sys

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.append(BASE_PATH)
# print(BASE_PATH)
from bin.logic.client.client import Client
from lib import basePath

if basePath:
    # 防止被软件清理
    pass

if __name__ == '__main__':
    app = Client(("127.0.0.1", 2020))
    app.run()
