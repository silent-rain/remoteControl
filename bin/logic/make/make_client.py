# -*- coding: utf-8 -*-
import sys
from os import mkdir
from os.path import dirname, abspath, exists
import shutil
import time

BASE_PATH = abspath(dirname(dirname(dirname(dirname(__file__)))))
sys.path.append(BASE_PATH)
# print(BASE_PATH)

from lib import settings
from lib.command import SubprocessExecute
from lib.logger import logger
from lib.settings import MAKE_OPTIONS

"""
编译模块
客户端编译
"""


class MakeClient(object):
    def __init__(self):
        self.execute = SubprocessExecute()

    @staticmethod
    def init_dir():
        """
        初始化编译目录
        :return:
        """
        # 编译
        mkdir(MAKE_OPTIONS["release_dir"]) if not exists(MAKE_OPTIONS["release_dir"]) else None  # 编译文件目录
        mkdir(MAKE_OPTIONS["client_dir"]) if not exists(MAKE_OPTIONS["client_dir"]) else None  # 客户端编译文件目录
        mkdir(MAKE_OPTIONS["client_temp"]) if not exists(MAKE_OPTIONS["client_temp"]) else None  # 缓存文件目录
        # mkdir(MAKE_OPTIONS["server_dir"]) if not exists(MAKE_OPTIONS["server_dir"]) else None  # 服务端编译文件目录

    @staticmethod
    def init_conf() -> str:
        """
        初始化配置命令
        :return:
        """
        cmd = "PyInstaller -F -y --clean "
        icon = settings.MAKE_OPTIONS["client_icon"]
        make_file = settings.MAKE_OPTIONS["client_file"]
        temp = settings.MAKE_OPTIONS["client_temp"]
        dist_path = settings.MAKE_OPTIONS["client_dist_path"]
        name = settings.MAKE_OPTIONS["client_name"]

        if not settings.DEBUG:
            cmd += "-w "

        # 组合命令
        if exists(icon):
            cmd += '--icon="{icon}" '.format(icon=icon)
        if exists(dist_path) and exists(temp):
            cmd += '--distpath="{0}" --workpath="{1}" --specpath="{2}" '.format(dist_path, temp, temp)
        if name:
            cmd += '--name="{0}" '.format(name)
        if exists(make_file):
            cmd += '"{make_client}"'.format(make_client=make_file)
            return cmd
        else:
            return ""

    def make(self):
        """
        编译
        :return:
        """
        cmd = self.init_conf()
        if not cmd:
            logger.error("文件不存在：%s" % settings.MAKE_OPTIONS["client_name"])
            return None

        logger.info("执行命令: %s" % cmd)
        # 执行命令
        msg_ = self.execute.execute(cmd)
        logger.debug(msg_)

        if "INFO: Building EXE from EXE-00.toc completed successfully." in msg_:
            logger.info("客户端编译成功...")

        # 删除缓存文件
        logger.info("开始清理缓存文件...")
        if exists(settings.MAKE_OPTIONS["client_temp"]):
            shutil.rmtree(settings.MAKE_OPTIONS["client_temp"])
            logger.info("客户端缓存清除成功...")
        else:
            logger.info("清除临时文件失败，文件不存在：%s" % settings.MAKE_OPTIONS["client_temp"])

    def main(self):
        start_time = time.time()
        self.init_dir()
        cmd = self.init_conf()
        print(cmd)
        # self.make()
        end_time = time.time()
        logger.info("耗时: %s 秒" % (int(end_time - start_time)))


if __name__ == '__main__':
    make = MakeClient()
    make.main()
