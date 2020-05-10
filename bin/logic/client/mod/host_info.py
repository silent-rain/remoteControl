# -*- coding: utf-8 -*-
import asyncio
import platform
import pynvml
import aiohttp
import psutil
from datetime import datetime
from aiohttp.client_exceptions import ClientConnectorError
from pyaudio import PyAudio, paInt16
from wmi import WMI
from socket import socket, AF_INET, SOCK_DGRAM, error
from lxml import etree
from psutil import net_if_addrs
from cv2 import VideoCapture


class LocalIp(object):
    def __init__(self):
        """
        获取内网 address，netmask
        """
        self.headers_title = {}

    @staticmethod
    def get_local_ip() -> str:
        """
        返回本地计算机的实际ip
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
        """
        获取所有网卡信息
        :return:
        """
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

    def parse_address(self) -> None:
        """
        解析实际网卡
        :return:
        """
        card_address = self.get_card_address()
        for card in card_address:
            # print(card_address[card])
            ip = self.get_local_ip()
            if ip in card_address[card]["AF_INET"]["address"]:
                # print(card_address[card])
                ipv4 = ip + "/" + card_address[card]["AF_INET"]["netmask"]
                self.headers_title["in_net"] = ipv4

    def get_data(self) -> dict:
        """
        返回最终结果
        :return:
        """
        return self.headers_title

    def main(self) -> None:
        """
        主接口
        :return:
        """
        self.parse_address()


class PublicIp(object):
    def __init__(self):
        """
        获取公网 address
        """
        self.headers_title = {}

    async def fetch_async2(self, url) -> None:
        async with aiohttp.ClientSession() as session:  # 协程嵌套，只需要处理最外层协程即可fetch_async
            headers = {
                'Connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/67.0.3396.10 Safari/537.36'
            }
            async with session.get(url, headers=headers) as resp:
                if resp.status == 200:
                    html = await resp.text()  # 因为这里使用到了await关键字，实现异步，所有他上面的函数体需要声明为异步async
                    # print(html)
                    html_emt = etree.HTML(html)
                    code_list: list = html_emt.xpath('//div[@id="result"]//code/text()')
                    # print(code_list)
                    if code_list:
                        self.headers_title["out_net"] = code_list[0]
                        self.headers_title["position"] = code_list[1]

    def get_data(self) -> dict:
        """
        返回最终结果
        :return:
        """
        return self.headers_title

    def main(self) -> None:
        """
        主接口
        :return:
        """
        try:
            tasks = [self.fetch_async2('https://ip.cn')]
            event_loop = asyncio.get_event_loop()
            event_loop.run_until_complete(asyncio.gather(*tasks))
            event_loop.close()
        except ClientConnectorError:
            pass


class ComputerInfo(object):
    def __init__(self):
        """
        获取计算机基础信息
        """
        self.headers_title = {}
        self.wmi = WMI()

    def get_hostname(self) -> None:
        """
        获取本机电脑名
        :return:
        """
        # host_name = getfqdn(gethostname())
        # self.headers_title["host_name"] = host_name

        self.headers_title["host_name"] = platform.node()

    def get_system(self) -> None:
        """
        获取系统信息
        操作系统
        系统位数

        platform.platform()        #获取操作系统名称及版本号，'Linux-3.13.0-46-generic-i686-with-Deepin-2014.2-trusty'
        platform.version()         #获取操作系统版本号，'#76-Ubuntu SMP Thu Feb 26 18:52:49 UTC 2015'
        platform.architecture()    #获取操作系统的位数，('32bit', 'ELF')
        platform.machine()         #计算机类型，'i686'
        platform.node()            #计算机的网络名称，'XF654'
        platform.processor()       #计算机处理器信息，''i686'
        platform.uname()           #包含上面所有的信息汇总，('Linux', 'XF654', '3.13.0-46-generic',
        :return:
        """
        system = platform.platform() + "/" + platform.machine()
        self.headers_title["system"] = system

    def get_boot_time(self) -> None:
        """
        获取系统的开机时间
        :return:
        """
        boot_time = datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")  # 转换成自然时间格式
        self.headers_title["boot_time"] = boot_time

    def get_cpu_info_win(self) -> bool:
        """
        获取cpu信息
        内核
        线程
        :return:
        """
        cpu_obj = self.wmi.Win32_Processor()
        if not cpu_obj:
            return False
        self.headers_title["cpu"] = cpu_obj[0].Name + "*{}*{}".format(psutil.cpu_count(logical=False),
                                                                      psutil.cpu_count())
        return True

    @staticmethod
    def calculate(speed: int) -> str:
        t = 1024 * 1024 * 1024 * 1024  # TB/s
        g = 1024 * 1024 * 1024  # GB/s
        m = 1024 * 1024  # MB/s
        k = 1024  # KB/s

        if speed > t:
            return str("%d" % (speed / t)) + "TB"
        elif speed > g:
            return str("%d" % (speed / g)) + "GB"
        elif speed > m:
            return str("%d" % (speed / m)) + "MB"
        elif speed > k:
            return str("%d" % (speed / k)) + "KB"
        else:
            return str("%d" % speed) + "B"

    def get_disk_win(self) -> None:
        """
        获取硬盘容量
        :return:
        """
        size = ""
        for disk in self.wmi.Win32_DiskDrive():
            size = size + "/" + "{}*{}".format(disk.Caption, self.calculate(int(disk.Size)))
        self.headers_title["disk"] = size.strip("/")

    def get_memory_win(self) -> None:
        mems = ""
        for mem in self.wmi.Win32_PhysicalMemory():
            mems += "/" + "{}*{}MHz".format(self.calculate(int(mem.Capacity)), mem.ConfiguredClockSpeed)
            self.headers_title["memory"] = mems.strip("/")

    def get_graphics(self) -> None:
        """
        gpu是否存在
        :return:
        """
        pynvml.nvmlInit()
        # handle = pynvml.nvmlDeviceGetHandleByIndex(0)  # 0表示第一块显卡
        # meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle)
        # print(meminfo.total / 1024 ** 2)  # 第二块显卡总的显存大小
        # print(meminfo.used / 1024 ** 2)  # 这里是字节bytes，所以要想得到以兆M为单位就需要除以1024**2
        # print(meminfo.free / 1024 ** 2)  # 第二块显卡剩余显存大小
        # print(pynvml.nvmlDeviceGetCount())  # 显示有几块GPU
        if int(pynvml.nvmlDeviceGetCount()):
            self.headers_title["graphics"] = True
        else:
            self.headers_title["graphics"] = False

    def get_video(self) -> None:
        """
        是否存在摄像头
        :return:
        """
        # 定义摄像头对象，其参数0表示第一个摄像头
        camera = VideoCapture(0)
        # 读取视频流
        ret, _ = camera.read()
        if not ret:
            # print("打开摄像头失败")
            self.headers_title["video"] = False
        else:
            self.headers_title["video"] = True

    def get_voice(self) -> None:
        chunk = 512
        format_ = paInt16
        channels = 1
        rate = 48000
        p = PyAudio()
        try:
            p.open(format=format_,
                   channels=channels,
                   rate=rate,
                   input=True,
                   frames_per_buffer=chunk)
            self.headers_title["voice"] = True
        except OSError:
            self.headers_title["voice"] = False

    def get_data(self) -> dict:
        """
        返回最终结果
        :return:
        """
        return self.headers_title

    def main(self) -> None:
        """
        主接口
        :return:
        """
        self.get_hostname()
        self.get_system()
        self.get_boot_time()
        self.get_cpu_info_win()
        self.get_disk_win()
        self.get_memory_win()
        self.get_graphics()
        self.get_video()
        self.get_voice()


class HostInfo(object):
    def __init__(self):
        self.local_ip = LocalIp()
        self.public_ip = PublicIp()
        self.computer_info = ComputerInfo()

        self.headers_title_dict = {
            "Id": "",
            "version": "",
            "note": "",
            "group": "",
        }
        self.headers_title_us = ["Id", "out_net", "in_net", "host_name", "system", "cpu", "memory", "disk",
                                 "graphics", "video", "voice", "boot_time", "version", "group", "position", "note"]

        self.headers_title = []
        self.load_list = []

    def load(self) -> None:
        self.load_list.append(self.local_ip)
        self.load_list.append(self.public_ip)
        self.load_list.append(self.computer_info)

    def show(self) -> None:
        for item in self.load_list:
            item.main()
            item_dict = item.get_data()
            self.headers_title_dict.update(item_dict)

        for item in self.headers_title_us:
            self.headers_title.append(self.headers_title_dict.get(item, ""))

    def main(self):
        self.load()
        self.show()


if __name__ == '__main__':
    app = HostInfo()
    app.main()
    print(app.headers_title_dict)
    print(len(app.headers_title_dict))
