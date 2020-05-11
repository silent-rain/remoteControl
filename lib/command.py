#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from subprocess import PIPE, Popen, STDOUT
import chardet
from sys import platform


class SubprocessExecute(object):
    @staticmethod
    def to_str(bytes_or_str: bytes) -> str:
        """
        把byte类型转换为str
        查看的编码格式
        :param bytes_or_str: bytes数据
        :return: 返回字符串
        """
        if isinstance(bytes_or_str, bytes):
            encoding_dic = chardet.detect(bytes_or_str)
            print(encoding_dic)
            encoding = encoding_dic["encoding"]
            print(encoding)
            value = bytes_or_str.decode(encoding)
            # value = bytes_or_str.decode('utf-8')
            # value = bytes_or_str.decode('gbk')
        else:
            value = bytes_or_str
        # 先去除每一行末尾的制表符和换行符，然后再加上换行符，使写入文件中的内容不会有空行
        return value.strip() + "\n"

    @staticmethod
    def to_str2(bytes_or_str):
        """
        把byte类型转换为str
        :param bytes_or_str: bytes数据
        :return: 返回字符串
        """
        if isinstance(bytes_or_str, bytes):
            try:
                value = bytes_or_str.decode('utf-8')
                #
            except UnicodeDecodeError:
                value = bytes_or_str.decode('gbk')
        else:
            value = bytes_or_str

        return value

    @staticmethod
    def to_str3(bytes_or_str):
        """
        把byte类型转换为str
        :param bytes_or_str: bytes数据
        :return: 返回字符串
        """
        if isinstance(bytes_or_str, bytes):
            if 'linux'.upper() in platform.upper():
                value = bytes_or_str.decode('utf-8')
            elif ('window' in platform) or ('win32' == platform):
                value = bytes_or_str.decode('gbk')
            else:
                value = bytes_or_str
        else:
            value = bytes_or_str

        return value

    def execute(self, cmd):
        """
        执行命令返回结果
        :param cmd: 命令
        :return: 返回输出
        """
        res = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        stderr = res.stderr
        stdout = res.stdout
        if stderr:
            # res_info = stderr.read().decode("gbk")
            res_info = self.to_str3(stderr.read())
        else:
            # res_info = stdout.read().decode("gbk")
            res_info = self.to_str3(stdout.read())

        return res_info


if __name__ == '__main__':
    execute = SubprocessExecute()
    # execute.execute("python -V")
    print(execute.execute("pip -V"))
    # print(execute.execute("pyinstaller -v"))
