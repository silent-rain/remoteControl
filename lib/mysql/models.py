# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Boolean
from lib.mysql.orm import Base, session

"""
数据库 表
# self.headers_title_us = ["Id", "out_net", "in_net", "host_name", "system", "cpu", "memory", "disk",
        #                          "graphics", "video", "voice", "boot_time", "version", "group", "position", "note"]
"""


class OnlineInfo(Base):
    # 主键自增的int类型的id主键
    id = Column(Integer, primary_key=True, autoincrement=True)
    out_net = Column(String(100), unique=True)
    in_net = Column(String(100), nullable=True, default="")
    host_name = Column(String(255), nullable=True, default="")
    system = Column(String(60), nullable=True, default="")
    cpu = Column(String(60), nullable=True, default="")
    memory = Column(String(60), nullable=True, default="")
    disk = Column(String(60), nullable=True, default="")
    graphics = Column(String(60), nullable=True, default="")
    video = Column(Boolean, nullable=True, default=False)  # 摄像头是否存在
    voice = Column(Boolean, nullable=True, default=False)  # 麦克风是否存在
    boot_time = Column(String(60), nullable=True, default="")
    version = Column(String(60), nullable=True, default="")
    group = Column(String(60), nullable=True, default="在线主机")
    position = Column(String(60), nullable=True, default="")
    note = Column(String(60), nullable=True, default="")

    # 表名
    __tablename__ = "online_info"
