import json
import os
import platform
import socket
import struct
import multiprocessing
import subprocess


class Terminal(object):
    def __init__(self):
        self.ip_port = ("127.0.0.1", 8090)
        self.back_log = 5
        self.buf_size = 1024
        self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_client.connect(self.ip_port)

        self.base_path = os.path.expanduser('~')

    def process(self, process):
        self.send_data(process)

    def recv_data(self):
        data_bytes = self.tcp_client.recv(4)  # 接数据
        data_length = struct.unpack('i', data_bytes)[0]  # 解压缩值 int 4 字节，获取数据长度

        # 接收数据
        recv_size = 0
        recv_data = b''
        while recv_size < data_length:
            recv_data += self.tcp_client.recv(self.buf_size)
            recv_size = len(recv_data)

        recv_data = recv_data.decode('utf-8')
        data = json.loads(recv_data)

        return data["data"]

    def send_data(self, msg):
        """
        发送数据
        :param msg: 数据
        :return:
        """
        # 报头+数据
        data_info = {
            "data_size": len(msg),
            "data": msg
        }
        data_json = json.dumps(data_info)  # 压缩数据
        data_bytes = bytes(data_json, encoding='utf-8')  # 转二进制
        data_length = struct.pack('i', len(data_bytes))  # 压缩值 int 4 字节
        self.tcp_client.send(data_length)  # 发送数据长度
        self.tcp_client.sendall(data_bytes)  # 发送数据

    @staticmethod
    def subprocess_execute(cmd, cwd=None):
        """
        执行命令返回结果
        :param cwd: 命令路径
        :param cmd: 命令
        :return: 返回输出
        """
        res = subprocess.Popen(
            cmd,
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            cwd=cwd
        )

        stdout, stderr = res.communicate()
        # print(stdout, stderr)
        # if stdout:
        #     print(stdout.decode("gbk"))
        # if stderr:
        #     print(stderr.decode("gbk"))
        res_info_list = []
        platform_sys = platform.system()
        if platform_sys == "Windows":
            if stdout:
                res_info = stdout.decode("gbk")
                res_info_list.append(res_info)
            if stderr:
                res_info = stderr.decode("gbk")
                res_info_list.append(res_info)
        elif platform_sys == "Linux":
            if stdout:
                res_info = stdout.decode("utf-8")
                res_info_list.append(res_info)
            if stderr:
                res_info = stderr.decode("utf-8")
                res_info_list.append(res_info)
        else:
            res_info = "无法确认操作系统！"
            res_info_list.append(res_info)
        # print(res_info)
        res_info = ''.join(res_info_list)
        return res_info

    def send_recv(self):
        self.process("terminal")
        self.send_data(self.base_path)  # 家目录
        while True:
            cmd_str = self.recv_data()
            cmd_list = cmd_str.split(" ")
            path = None
            if len(cmd_list) > 1:
                cmd = cmd_list[0]
                path = cmd_list[1]
            else:
                cmd = cmd_list[0]
            if cmd == "quit":
                break
            print("cmd_str", cmd_str)
            print("cmd_list", cmd_list)
            print("self.base_path", self.base_path)
            if path == "..":
                self.base_path = os.path.dirname(self.base_path)
                print(self.base_path)
            else:
                self.base_path = path
            res = self.subprocess_execute(cmd, self.base_path)
            self.send_data(res)
        self.tcp_client.close()

    def main(self):
        process = multiprocessing.Process(target=self.send_recv)
        process.start()
