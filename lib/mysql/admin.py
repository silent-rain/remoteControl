# -*- coding: utf-8 -*-
from lib.mysql.models import OnlineInfo
from lib.mysql.orm import create_db, drop_db, session

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

    def setup_ui(self) -> None:
        self.create()

    @staticmethod
    def create() -> None:
        """
        映射模型对应的表
        :return:
        """
        create_db()

    @staticmethod
    def drop() -> None:
        """
        删除模型对应的表
        :return:
        """
        drop_db()

    def retranslate_ui(self) -> None:
        pass


if __name__ == '__main__':
    orm = ORMConnect()
    orm.create()
    # 创建多条数据
    ips = []
    for i in range(50):
        ip = OnlineInfo()
        ip.out_net = "192.168.0.%s" % i
        ips.append(ip)
    session.add_all(ips)
    session.commit()
    print("添加数据成功！")
