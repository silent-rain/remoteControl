# -*- coding: utf-8 -*-
from lib.mysql.models import OnlineInfo
from lib.mysql.orm import create_db

"""
数据库注册
"""

if OnlineInfo:
    # 防止被清理
    pass


class ORMConnect(object):
    def __init__(self):
        """
        数据库注册
        """

    @staticmethod
    def setup_ui() -> None:
        create_db()  # 映射模型对应的表

    def retranslate_ui(self) -> None:
        pass
