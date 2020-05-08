# -*- coding: utf-8 -*-
# import json
import struct
# import socketserver
from socketserver import BaseRequestHandler, ThreadingMixIn, TCPServer
from json import loads, dumps
from threading import Thread

from lib import settings
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
        print("连接池加入客户端: ", self.client_address)

    def finish(self) -> None:
        """
        客户端连接断开
        :return:
        """
        # 连接池删除客户端
        CONNECTION_POOL.pop(self.request)
        print("连接池删除客户端: ", self.client_address)

    def handle(self) -> None:
        """
        处理到的请求
        消息循环
        :return:
        """
        while True:
            # msg = self.request.recv(1024).decode('utf-8')
            msg = self.recv_data()
            print(msg)
            info = input('>>>')
            # self.request.send(info.encode('utf-8'))
            self.send_data(info)

    def recv_data(self) -> str:
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


class Server(Thread):
    def __init__(self, server_address: tuple):
        """
        实例化服务类对象
        :param server_address: ("127.0.0.1", 8090)
        """
        super().__init__()
        # server_address = ("127.0.0.1", 8090)
        # 单线程
        # self.server = ThreadingTCPServer(('127.0.0.1', 8090), ThreadingTCPRequestHandler)
        # 实现异步，支持多连接
        self.server = ThreadingTCPServer(server_address, ThreadingTCPRequestHandler)

        self.stop_flag = False

    def stop_server(self):
        """
        服务器停止
        :return:
        """
        # 关闭所有链接
        # for conn in connection_pool:
        #     # self.server.close_request(conn)
        #     self.server.block_on_close()

        # 关闭服务器
        self.server.shutdown()
        self.server.server_close()

    def run(self) -> None:
        """
        服务器启动
        :return:
        """
        logger.info("系统信息 - 服务器启动....")
        self.server.serve_forever()

        # while True:
        #     cmd = input("输入指令: ")
        #     if cmd == "quit()":
        #         self.stop_flag = True
        #
        #     if self.stop_flag:
        #         self.stop_server()
        #         self.stop_flag = False
        #         break


if __name__ == '__main__':
    server = Server((settings.IP, settings.PORT))
    server.start()
    server.join()  # 阻塞
