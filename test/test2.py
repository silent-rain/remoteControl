"""
.*add_ui\((.*)(\(.*)\)(.*)

self.$1= $1$2  $3


ini
.*(C.*\]).*?(".*"),.*
$1\[$2\]
"""

headers_title_us = ["Id", "out_net", "in_net", "host_name", "system", "cpu", "memory", "disk",
                    "video", "voice", "boot_time", "version", "group", "position", "note"]


# out_net = headers_title_us[1]
# note = headers_title_us[-1]
# group = headers_title_us[-3]
# print(out_net)
# print(note)
# print(group)

# self.headers_title = [
#     _translate("DisplayInfoUI", "Id"),
#     # _translate("DisplayInfoUI", "外网"),
#     _translate("DisplayInfoUI", "主机信息"),
#     _translate("DisplayInfoUI", "内网"),
#     _translate("DisplayInfoUI", "计算机"),
#     _translate("DisplayInfoUI", "操作系统"),
#     _translate("DisplayInfoUI", "处理器"),
#     _translate("DisplayInfoUI", "内存"),
#     _translate("DisplayInfoUI", "硬盘容量"),
#     _translate("DisplayInfoUI", "视频"),
#     _translate("DisplayInfoUI", "语音"),
#     _translate("DisplayInfoUI", "开机时间"),
#     _translate("DisplayInfoUI", "服务版本"),
#     _translate("DisplayInfoUI", "分组"),
#     _translate("DisplayInfoUI", "区域"),
#     _translate("DisplayInfoUI", "备注"),
# ]
# self.headers_title = [
#     _translate("DisplayInfoUI", "Id"),
#     _translate("DisplayInfoUI", "主机信息"),
#     _translate("DisplayInfoUI", "备注"),
# ]
# self.header_width = [90, 100]
# print(len(headers_title_us))
# hide_column = headers_title_us[2:-1]
# print(hide_column)
# print(len(hide_column))

# print("/465GB/149GB".strip("/"))
# info = {'Id': '', 'version': '', 'note': '', 'host_name': 'DESKTOP-ONE', 'system': 'Windows-10-10.0.18362-SP0/AMD64', 'boot_time': '2020-05-10 11:43:04', 'cpu': 'Intel(R) Core(TM) i7-4700HQ CPU @ 2.40GHz*4*8', 'disk': 'TOSHIBA MQ01ABF050*465GB/INTEL SSDSA2M160G2LE*149GB', 'memory': '8GB*1600MHz/4GB*1600MHz', 'graphics': True, 'video': True, 'voice': False}
# print(len(info))

class Test(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
            return cls._instance

    def __init__(self):
        if not hasattr(self, "_instance_flag"):
            self._instance_flag = True
        else:
            return
        print("1111111111")


    def main(self):
        print(self._instance_flag)

if __name__ == '__main__':
    aaa = Test()
    print(aaa._instance_flag)
