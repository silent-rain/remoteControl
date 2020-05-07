# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String
from lib.mysql.orm import Base


class OnlineInfo(Base):
    # 主键自增的int类型的id主键
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 定义不能为空的唯一的姓名字段
    ip = Column(String(10), unique=True, nullable=True)
    s_age = Column(Integer, default=18)

    # 表名
    __tablename__ = "online_info"

