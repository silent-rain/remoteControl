# -*- coding: utf-8 -*-
from lib.mysql.models import OnlineInfo
from lib.mysql.orm import create_db, drop_db, session
from lib.settings import DB_ONLINE_TITLE

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
    # orm.create()

    # 创建多条数据
    hosts = []
    for i in range(50):
        host = OnlineInfo()
        host.out_net = "192.168.0.%s" % i
        host.group = "在线主机"
        hosts.append(host)
    session.add_all(hosts)
    session.commit()
    print("添加测试上线数据成功！")

    # 获取数据
    # stus = session.query(OnlineInfo).values()
    # print(list(stus))

    # 查询所有数据 [[],[]]
    # hosts = session.query(OnlineInfo).all()
    # new_hosts_list = []
    # for host in hosts:
    #     new_hosts = []
    #     for title in DB_ONLINE_TITLE:
    #         new_hosts.append(host.__dict__.get(title, None))
    #     new_hosts_list.append(new_hosts)
    # print(new_hosts_list)

