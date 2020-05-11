# -*- coding:utf-8 -*-
import sys
from os.path import abspath, dirname, realpath


def base_path() -> str:
    """
    添加环境变量
    :return:
    """
    # 运行文件路径
    current_path = dirname(dirname(abspath(__file__)))
    sys.path.append(current_path)

    # 入口文件路径
    realpath_ = abspath(realpath(sys.argv[0]))
    sys.path.append(realpath_)

    if realpath_.endswith(".py"):
        base_dir = current_path
    else:
        base_dir = dirname(realpath_)
    return base_dir


BASE_PATH = base_path()
sys.path.append(BASE_PATH)
# BASE_PATH = dirname(abspath(__file__))
# print(BASE_PATH)
