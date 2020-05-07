import re

title = "在线主机(0)"

find = re.compile(r'(.*?)\(')  # 正则对象
title = find.findall(title)[0]
print(title)

"""
            远程控制 v1.0
    本软件主要使用Python基于Qt5进行编程.
    本软件使用于学习软件开发.
    请不要触犯法律,否则后果自负,一切与原作者无关.
    Pythton: v3.7
    Qt: v5.13
    目前还在开发中......
"""