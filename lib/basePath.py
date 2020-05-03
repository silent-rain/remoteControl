# -*- coding:utf-8 -*-
import sys
from os.path import abspath, dirname, realpath
from lib import fix_qt_import_error


def base_path():
    """
    添加环境变量
    :return:
    """
    # 项目根路径
    current_path = abspath(dirname(dirname(__file__)))
    sys.path.append(current_path)

    # EXE运行路径
    realpath_ = abspath(realpath(sys.argv[0]))

    base_dir = None
    if realpath_.endswith(".py"):
        base_dir = current_path
    elif realpath_.endswith(".exe"):
        base_dir = dirname(realpath_)

    return base_dir


BASE_PATH = base_path()
sys.path.append(BASE_PATH)
# BASE_PATH = os.path.abspath(os.path.dirname(__file__))
# print(BASE_PATH)
