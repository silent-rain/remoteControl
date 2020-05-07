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
print(len(headers_title_us))
hide_column = headers_title_us[2:-1]
print(hide_column)
print(len(hide_column))