# -*- coding: utf-8 -*-
import os
import subprocess
import platform


def install_command(package):
    """
    安装命令组合
    :param package: 安装包
    :return: 返回完整安装命令
    """
    cmd_ = "pacman -S --noconfirm {0}".format(package)
    return cmd_


def subprocess_execute(cmd, cwd=None):
    """
    执行命令返回结果
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

    # stderr = res.stderr
    # res_info = ""
    # platform_sys = platform.system()
    # if platform_sys == "Windows":
    #     if stderr:
    #         res_info = stderr.read().decode("gbk")
    #     else:
    #         stdout = res.stdout
    #         res_info = stdout.read().decode("gbk")
    # elif platform_sys == "Linux":
    #     if stderr:
    #         res_info = stderr.read().decode("utf-8")
    #     else:
    #         stdout = res.stdout
    #         res_info = stdout.read().decode("utf-8")
    # else:
    #     print("无法确认操作系统！")
    # # print(res_info)
    # return res_info


base_path = os.path.expanduser('~')
cmd_str = "cd .."
cmd_list = cmd_str.split(" ")
print(cmd_list)
if cmd_list[1] == "..":
    path = os.path.dirname(base_path)
# print(cmd_list[1])
# print(base_path)
# print(path)
# print(subprocess_execute("cd .."))
print(subprocess_execute('cd', path))
