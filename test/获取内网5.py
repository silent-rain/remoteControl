# -*- coding: utf-8 -*-
from socket import socket, AF_INET, SOCK_DGRAM, error
from psutil import net_if_addrs

FILTER_LIST = [
    # Windows
    "VMware",  # vmware虚拟机
    "Loopback",  # 内循环
    "VirtualBox Host-Only Network",
    "VirtualBox",

    # linux
    "vmnet",
    "lo",
    "docker",
    "xdroid",  # 安卓虚拟机
]


class LocalIp(object):
    def __init__(self):
        self.in_net = ""

    @staticmethod
    def get_local_ip() -> str:
        """
        Returns the actual ip of the local machine.
        This code figures out what source address would be used if some traffic
        were to be sent out to some well known address on the Internet. In this
        case, a Google DNS server is used, but the specific address does not
        matter much.  No traffic is actually sent.
        """
        try:
            csock = socket(AF_INET, SOCK_DGRAM)
            csock.connect(('8.8.8.8', 80))
            addr, port = csock.getsockname()
            csock.close()
            return addr
        except error:
            return "127.0.0.1"

    @staticmethod
    def get_card_address() -> dict:
        name_card_address = {}
        for card, value in net_if_addrs().items():
            # if filter_card(card):
            #     continue
            name_card_address_sub = {}
            # print(card, value)
            for sni_caddr in value:
                if "AF_INET" == sni_caddr.family.name:
                    # print(dir(sni_caddr))
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
        # print(name_card_address)
        return name_card_address

    def main(self) -> str:
        card_address = self.get_card_address()
        for card in card_address:
            # print(card_address[card])
            ip = self.get_local_ip()
            if ip in card_address[card]["AF_INET"]["address"]:
                # print(card_address[card])
                ipv4 = ip + "/" + card_address[card]["AF_INET"]["netmask"]
                self.in_net = ipv4
                return ipv4
            else:
                return ""

    def get_data(self):
        """
        返回最终结果
        :return:
        """
        return self.in_net


if __name__ == '__main__':
    app = LocalIp()
    app.main()
