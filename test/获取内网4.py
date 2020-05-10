# -*- coding:utf-8 -*-
import datetime
import os
import socket
from psutil import net_if_addrs
import uuid
import configparser


def get_host_info():
    # 获取主机名
    hostname = socket.gethostname()

    # 获取本机所有网卡的mac地址
    address_list = []
    for k, v in net_if_addrs().items():
        for item in v:
            address = item[1]
            if "-" in address and len(address) == 17:
                address_list.append(address)
    macs = " + ".join(address_list)

    mac = uuid.UUID(int=uuid.getnode()).hex[-12:].upper()
    mac = "-".join([mac[e:e + 2] for e in range(0, 11, 2)])

    print(hostname + "_" + mac + "_")


get_host_info()