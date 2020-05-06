from psutil import net_if_addrs
import sys
from sys import platform

FILTER_LIST = [
    # Windows
    "VMware",  # vmware虚拟机
    "Loopback",  # 内循环

    # linux
    "vmnet",
    "lo",
    "docker",
    "xdroid",  # 安卓虚拟机
]


def filter_card(card):
    """
    过滤 网卡
    :param card:
    :return:
    """
    for filter_ in FILTER_LIST:
        if filter_.upper() in card.upper():
            return True


def filter_field_window():
    for name, value in net_if_addrs().items():
        if filter_card(name):
            continue
        for sni_caddr in value:
            if "AF_LINK" == sni_caddr[0].name:
                mac = sni_caddr[1]
                print(mac)
            if "AF_INET" == sni_caddr[0].name:
                address = sni_caddr[1]
                netmask = sni_caddr[2]
                # print(name, mac, address, netmask)
                # print(mac_uuid)
                # if mac == mac_uuid:
                #     name_card_address[name] = [address, mac, netmask]


def filter_field_linux():
    name_card_address = {}
    for card, value in net_if_addrs().items():
        if filter_card(card):
            continue
        name_card_address_sub = {}
        print(card, value)
        for sni_caddr in value:
            # print(dir(sni_caddr))
            # print(dir(sni_caddr))
            # print(sni_caddr.address)
            # print(sni_caddr.netmask)
            # print(sni_caddr.family.name, sni_caddr.family.value)
            if "AF_INET" == sni_caddr.family.name:
                # print(sni_caddr[1])
                # print(sni_caddr[2])
                name_card_address_sub["AF_INET"] = {
                    "address": sni_caddr.address,
                    "netmask": sni_caddr.netmask,
                }
            if "AF_INET6" == sni_caddr.family.name:
                name_card_address_sub["AF_INET6"] = {
                    "address": sni_caddr.address,
                    "netmask": sni_caddr.netmask,
                }
        name_card_address[card] = name_card_address_sub
    return name_card_address


def get_public_ip():
    """
    获取网卡名称、mac和ip地址
    """
    if 'linux'.upper() in platform.upper():
        return filter_field_linux()
    elif 'window'.upper() in platform.upper():
        return filter_field_window()
    else:
        return {}


if __name__ == '__main__':
    print(get_public_ip())
