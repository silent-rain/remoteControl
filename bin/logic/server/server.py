# -*- coding: utf-8 -*-
# import json
import struct
# import socketserver
from socket import socket, SHUT_WR, SHUT_RDWR
from socketserver import BaseRequestHandler, ThreadingMixIn, TCPServer
from json import loads, dumps
from PyQt5.QtCore import QThread

from lib import settings
from lib.communicate import communicate
from lib.logger import logger

"""
服务器
"""

CONNECTION_POOL = {}  # 连接池


class ThreadingTCPRequestHandler(BaseRequestHandler):
    """
    StreamRequestHandler:
        对客户端发过来的数据是用rfile属性来处理的,rfile是一个类file对象.有缓冲.可以按行分次读取;
        发往客户端的数据通过wfile属性来处理,wfile不缓冲数据,对客户端发送的数据需一次性写入.
    """
    # 数据流大小
    buf_size = 1024
    online_data = []

    def online_info(self, data: list) -> None:
        """
        上线信息
        :param data:
        :return:
        """
        self.online_data = data
        # data = [None, self.client_address[0], '', '', '', '', '', '', False, False, '', '', '爱好者线主机', '', '']
        communicate.online_data.emit(data)
        out_net = data[1]
        communicate.online_sound.emit(True, out_net)

    def offline_info(self) -> None:
        # self.online_data = [None, self.client_address[0], '', '', '', '', '', '', False, False, '', '', '爱好者线主机', '', '']
        communicate.offline_data.emit(self.online_data)
        out_net = self.online_data[1]
        communicate.online_sound.emit(False, out_net)

    def setup(self) -> None:
        """
        1. 连接成功的服务器
        2. 客户端加入连接池
        :return:
        """
        # self.request.getpeername()
        # 连接池加入客户端
        if self.request not in CONNECTION_POOL:
            CONNECTION_POOL.update({self.request: self.client_address[0]})
            # self.online_info()

    def finish(self) -> None:
        """
        客户端连接断开
        :return:
        """
        # 连接池删除客户端
        CONNECTION_POOL.pop(self.request)
        # logger.warning("离线信息 - 有主机离线...")
        self.offline_info()

    def handle(self) -> None:
        """
        处理到的请求
        消息循环
        # self.request.send(info.encode('utf-8'))
        :return:
        """
        # 上线信息
        online_data = self.recv_data()
        self.online_info(online_data)
        while True:
            try:
                self.send_data("info")
            except (BrokenPipeError, OSError, struct.error) as e:
                logger.debug("系统信息 - " + str(e))
                # CONNECTION_POOL.pop(self.request)
                return None

    def recv_data(self):
        """
        接收数据
        报头+数据
        :return:
        """
        # 先接受4个字节使用struct转换成数字来获取要接收的数据长度
        head_len_bytes = self.request.recv(4)

        # 解压缩值 int 4 字节，获取数据长度
        data_length = struct.unpack('i', head_len_bytes)[0]

        # 按照长度接收数据
        recv_size = 0
        recv_data = b''
        while recv_size < data_length:
            recv_data += self.request.recv(self.buf_size)
            recv_size = len(recv_data)

        # 最后根据报头的内容提取真实的数据
        recv_data = recv_data.decode('utf-8')  # 解码
        # 反序列化
        data = loads(recv_data)

        return data

    def send_data(self, data: str) -> None:
        """
        发送数据
        报头+数据
        :param data: 数据
        :return:
        """
        # 序列化数据
        head_json = dumps(data)

        # 转成bytes数据,用于传输
        head_bytes = bytes(head_json, encoding='utf-8')

        # 为了让客户端知道报头的长度,用struck将报头长度这个数字转成固定长度:4个字节
        # 这4个字节里只包含了一个数字,该数字是报头的长度
        head_length = struct.pack('i', len(head_bytes))

        # 开始发送数据
        self.request.send(head_length)  # 先发报头的长度,4个bytes
        self.request.sendall(head_bytes)  # 再发报头的字节格式


class ThreadingTCPServer(ThreadingMixIn, TCPServer):
    """
    实现异步，支持多连接
    ForkingMixIn 每次用户连接的时候都会开启新的进程
    ThreadingMixIn 每次用户连接的时候都会开启新的线程
    """
    pass


class Server(QThread):
    def __init__(self):
        """
        实例化服务类对象
        server_address: ("127.0.0.1", 8090)
        :param
        """
        super().__init__()
        # server_address = ("127.0.0.1", 8090)

        # 服务器实例化对象
        self.server = None

        # 控制开关
        self.flag = False

    def stop_server(self) -> None:
        """
        服务器停止
        :return:
        """
        # 关闭所有链接
        # 在close()之前加上shutdown(num)即可  [shut_rd(), shut_wr(), shut_rdwr()分别代表num 为0  1  2 ]
        for conn in CONNECTION_POOL:
            # conn: socket = CONNECTION_POOL.popitem()[0]
            # self.server.close_request(conn)  # 无效
            # print(dir(conn))
            conn.shutdown(2)
            conn.close()

        # 关闭服务器
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            logger.info("操作 - 服务器停止...")

    def start_server(self) -> None:
        """
        服务器启动
        :return:
        """
        # 开始监听
        logger.info("操作 - 服务器启动...")
        logger.info("系统信息 - 本地IP: [{}]    监听端口: [{}]".format(settings.IP, settings.PORT))
        # 单线程
        # self.server = ThreadingTCPServer(('127.0.0.1', 2020), ThreadingTCPRequestHandler)
        # 实现异步，支持多连接
        self.server = ThreadingTCPServer((settings.IP, settings.PORT), ThreadingTCPRequestHandler)
        self.server.serve_forever()

    def close(self) -> None:
        """
        关闭线程
        :return:
        """
        self.stop_server()
        self.quit()


class ServerStart(QThread):
    def __init__(self, server: Server):
        """
        实例化服务类对象
        server_address: ("127.0.0.1", 8090)
        :param server:
        :param
        """
        super().__init__()
        self.server = server

    def run(self) -> None:
        """
        主运行
        :return:
        """
        try:
            # 服务器启动
            self.server.start_server()
        except OSError as e:
            logger.error("系统信息 - " + str(e))
            logger.error("系统信息 - 服务启动失败!!!")
            # 服务器异常停止
            communicate.start_server_error.emit(False)


class ServerStop(QThread):
    def __init__(self, server: Server):
        """
        实例化服务类对象
        server_address: ("127.0.0.1", 8090)
        :param server:
        :param
        """
        super().__init__()
        self.server = server

    def run(self) -> None:
        """
        主运行
        :return:
        """
        # 服务器启动
        self.server.stop_server()


class ServerConnect(object):
    def __init__(self):
        """
        服务器信号
        """
        super().__init__()
        # self.server = server
        self.server = Server()
        self.server_start: object = None
        self.server_stop: object = None

    def setup_ui(self) -> None:
        self.communicate_connect()

    def retranslate_ui(self) -> None:
        pass

    def communicate_connect(self) -> None:
        # 服务启动/停止
        communicate.start_server.connect(self.start_server)

    def start_server(self, event: bool) -> None:
        if event:
            # logger.info("操作 - 服务器启动...")
            # logger.info("系统信息 - 本地IP: [{}]    监听端口: [{}]".format(settings.IP, settings.PORT))
            self.server_start = ServerStart(self.server)
            self.server_start.start()
        else:
            # logger.info("操作 - 服务器停止...")
            self.server_stop = ServerStop(self.server)
            self.server_stop.start()


if __name__ == '__main__':
    app = Server()
    app.start()
    app.join()  # 阻塞
