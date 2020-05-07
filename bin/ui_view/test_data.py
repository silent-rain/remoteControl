from lib.communicate import communicate
from lib.mysql.models import OnlineInfo
from lib.mysql.orm import session
from lib.settings import DB_ONLINE_TITLE


class TestDataConnect(object):
    def __init__(self):
        """
        测试数据集
        """

    def setup_ui(self) -> None:
        # self.online_data_db_create()
        self.online_data_emit()

    @staticmethod
    def online_data_db_create() -> None:
        """
        创建数据至数据库
        :return:
        """
        # 创建多条数据
        hosts = []
        for i in range(50):
            host = OnlineInfo()
            host.out_net = "192.168.0.%s" % i
            host.group = "在线主机"
            hosts.append(host)

        for i in range(50, 100):
            host = OnlineInfo()
            host.out_net = "192.168.0.%s" % i
            host.group = "爱好者线主机"
            hosts.append(host)

        session.add_all(hosts)
        session.commit()
        print("添加测试上线数据成功！")

    @staticmethod
    def online_data_emit() -> None:
        """
        查看数据库
        获取所有数据
        发送至分组以及信息展示
        :return:
        """
        # 查询所有数据 [[],[]]
        hosts = session.query(OnlineInfo).all()
        hosts_list = []
        for host in hosts:
            host_item = []
            for title in DB_ONLINE_TITLE:
                host_item.append(host.__dict__.get(title, None))
            hosts_list.append(host_item)

        # 测试上线
        for item in hosts_list:
            # 单条发送
            communicate.online_data.emit(item)
            out_net = item[1]
            communicate.online_sound.emit(True, out_net)

    @staticmethod
    def offline_data_emit() -> None:
        """
        查看数据库
        获取所有数据
        发送至分组以及信息展示
        :return:
        """
        # 查询所有数据 [[],[]]
        hosts = session.query(OnlineInfo).all()
        hosts_list = []
        for host in hosts:
            host_item = []
            for title in DB_ONLINE_TITLE:
                host_item.append(host.__dict__.get(title, None))
            hosts_list.append(host_item)

        # 测试下线
        for item in hosts_list:
            import time
            time.sleep(5)
            # 单条发送
            communicate.online_data.emit(item)
            out_net = item[1]
            communicate.online_sound.emit(False, out_net)

    @staticmethod
    def online_data__list_emit() -> None:
        """
        查看数据库
        获取所有数据
        发送至分组以及信息展示
        :return:
        """
        # 查询所有数据 [[],[]]
        hosts = session.query(OnlineInfo).all()
        hosts_list = []
        for host in hosts:
            host_item = []
            for title in DB_ONLINE_TITLE:
                host_item.append(host.__dict__.get(title, None))
            hosts_list.append(host_item)

            # 单条发送
            communicate.online_data.emit(host_item)

    def retranslate_ui(self) -> None:
        pass
