# -*- coding: utf-8 -*-
import sys
from os import mkdir
from os.path import dirname, abspath, exists
import shutil
import time

BASE_PATH = dirname(dirname(dirname(dirname(abspath(__file__)))))
sys.path.append(BASE_PATH)
# print(BASE_PATH)

from lib import settings
from lib.command import SubprocessExecute
from lib.logger import logger
from lib.settings import MAKE_OPTIONS

"""
编译模块
服务端端编译
"""


class MakeServer(object):
    def __init__(self):
        self.execute = SubprocessExecute()

        self.cmd = "pyinstaller -F -y --clean "

        self.release_dir = MAKE_OPTIONS["release_dir"]
        self.server_dir = MAKE_OPTIONS["server_dir"]
        self.temp = settings.MAKE_OPTIONS["server_temp"]
        self.icon = settings.MAKE_OPTIONS["server_icon"]
        self.make_file = settings.MAKE_OPTIONS["server_file"]
        self.dist_path = settings.MAKE_OPTIONS["server_dist_path"]
        self.name = settings.MAKE_OPTIONS["server_name"]

    def init_dir(self):
        """
        初始化编译目录
        :return:
        """
        # 编译
        mkdir(self.release_dir) if not exists(self.release_dir) else None  # 编译文件目录
        mkdir(self.server_dir) if not exists(self.server_dir) else None  # 服务端编译文件目录
        mkdir(self.temp) if not exists(self.temp) else None  # 服务端编缓存文件目录

    def init_conf(self) -> str:
        """
        初始化配置命令
        :return:
        """
        if not settings.DEBUG:
            self.cmd += "-w "

        # 组合命令
        if exists(self.icon):
            self.cmd += '--icon="{icon}" '.format(icon=self.icon)
        if exists(self.dist_path) and exists(self.temp):
            self.cmd += '--distpath="{0}" --workpath="{1}" --specpath="{2}" '.format(
                self.dist_path, self.temp, self.temp)
        if self.name:
            self.cmd += '--name="{0}" '.format(self.name)
        if exists(self.make_file):
            self.cmd += '"{make_client}"'.format(make_client=self.make_file)
            return self.cmd
        else:
            self.cmd = ""
            return ""

    def make(self):
        """
        编译
        :return:
        """
        if not self.cmd:
            logger.error("文件不存在：%s" % self.make_file)
            return None

        logger.info("执行命令: \n%s" % self.cmd)
        logger.info("开始编译...")
        # 执行命令
        msg_ = self.execute.execute(self.cmd)
        logger.debug(msg_)

        if "INFO: Building EXE from EXE-00.toc completed successfully." in msg_:
            logger.info("编译成功...")

        # 删除缓存文件
        logger.info("开始清理缓存文件...")
        if exists(self.temp):
            shutil.rmtree(self.temp)
            logger.info("缓存清除成功...")
        else:
            logger.info("清除临时文件失败，文件不存在：%s" % self.temp)

    def main2(self):
        """
        获取命令
        :return:
        """
        self.init_dir()
        self.init_conf()
        print(self.cmd)

    def main(self):
        """
        开始编译
        :return:
        """
        start_time = time.time()
        self.init_dir()
        self.init_conf()
        self.make()
        end_time = time.time()
        logger.info("耗时: %s 秒" % (int(end_time - start_time)))


if __name__ == '__main__':
    make = MakeServer()
    make.main()
