# -*- coding: utf-8 -*-

import os
import re
import platform

if platform.system() == "Windows":
    ipconfig = os.popen("chcp 65001&&ipconfig").read()
    res = re.findall('IPv4 Address.*?: (.*?)\n.*?Subnet Mask.*?: (.*?)\n', ipconfig)
else:
    ifconfig = os.popen("ifconfig").read()
    res = re.findall('inet (.*?)  netmask (.*?) ', ifconfig)

ip, netmask = res[0]


def get_ip_addrs(ip, netmask):
    print("IP:", ip)
    print("掩码:", netmask)
    # ip、netmask十进制转换二进制
    ips = [bin(int(i))[2:].zfill(8) for i in ip.split(".")]
    masks = [bin(int(i))[2:].zfill(8) for i in netmask.split(".")]

    # 根据ip地址和掩码地址计算网络号
    network_name = [[], [], [], []]
    for index, (i, m) in enumerate(zip(ips, masks)):
        for ip_i, mask_m in zip(i, m):
            network_name[index].append(str(int(ip_i) & int(mask_m)))

    # 网络号二进制转换十进制
    network_name = [str(int('0b' + ''.join(i), base=2)) for i in network_name]
    print("网络号:", ".".join(network_name))

    # 计算主机号
    host_number = "".join(masks)
    host_number = 32 - host_number.index('0')
    print("主机号:", host_number)

    # 计算主机数
    addr_count = 2 ** host_number - 2
    print("主机数:", addr_count)
    print("广播地址:", ".".join(network_name[:-1]) + "." + str(addr_count + 1))

    # 根据网络号和主机数确定子网ip
    ip_addrs = [network_name[:-1] + [str(i)] for i in range(int(network_name[-1]) + 1, addr_count + 1)]
    ip_addrs = [".".join(i) for i in ip_addrs]
    print("可用地址:", ip_addrs[0], "~", ip_addrs[-1])
    return ip_addrs


ip_addrs = get_ip_addrs(ip, netmask)

