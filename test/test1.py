import re

title = "在线主机(0)"

find = re.compile(r'(.*?)\(')  # 正则对象
title = find.findall(title)[0]
print(title)
