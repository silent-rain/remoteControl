# -*- coding: utf-8 -*-
# import json
import socket
import struct
from json import loads, dumps
from time import sleep

from lib import settings

"""
客户端
"""


class Client(object):
    def __init__(self, server_address):
        """
        客户端初始化
        :param server_address:
        """
        # self.server_address = ("127.0.0.1", 8090)
        self.server_address = server_address

        # 创建客户端实例
        self.tcp_client = None

        # 数据流大小
        self.buf_size = 1024

    def connect(self) -> bool:
        """
        连接
        :return:
        """
        while True:
            try:
                # 类型
                self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                self.tcp_client.connect(self.server_address)
                return True
            except ConnectionRefusedError as e:
                print(e)
                print("等待服务器......")
                sleep(5)

    def recv_data(self) -> str:
        """
        接收数据
        报头+数据
        :return:
        """
        # 先接受4个字节使用struct转换成数字来获取要接收的数据长度
        head_len_bytes = self.tcp_client.recv(4)

        # 解压缩值 int 4 字节，获取数据长度
        data_length = struct.unpack('i', head_len_bytes)[0]

        # 按照长度接收数据
        recv_size = 0
        recv_data = b''
        while recv_size < data_length:
            recv_data += self.tcp_client.recv(self.buf_size)
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
        self.tcp_client.send(head_length)  # 先发报头的长度,4个bytes
        self.tcp_client.sendall(head_bytes)  # 再发报头的字节格式

    def io_loop(self) -> None:
        """
        监听循环

        :return:
        """
        while True:
            # msg = input('>>>>>')
            msg = "input('>>>>>')"
            # self.tcp_client.send(msg.encode('utf-8'))
            self.send_data(msg)
            # ret = self.tcp_client.recv(1024).decode('utf-8')
            try:
                ret = self.recv_data()
                print(ret)
            except (struct.error, ConnectionResetError):
                pass

    def run(self) -> None:
        """
        客户端启动连接
        断线重连
        关闭客户端, 永不关闭
        :return:
        """
        try:
            # 连接
            self.connect()
            # 监听循环
            self.io_loop()
        except BrokenPipeError:
            # print("服务器断开")
            self.run()

        # 关闭客户端, 永不关闭
        # self.tcp_client.close()


if __name__ == '__main__':
    client = Client((settings.IP, settings.PORT))
    client.run()
