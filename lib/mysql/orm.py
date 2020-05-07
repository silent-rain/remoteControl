# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from lib.settings import DB_URL

"""
MySQL 数据库 ORM
"""

# 连接数据库格式
# mysql+pymysql://用户名:密码@数据库地址:端口/数据库?charset=utf8
# db_url = "mysql+pymysql://{username}:{password}@{host}:{port}/{db_name}?charset=utf8".format(
#     username=MYSQL_DB["username"],
#     password=MYSQL_DB["password"],
#     host=MYSQL_DB["host"],
#     port=MYSQL_DB["port"],
#     db_name=MYSQL_DB["db_name"],
# )
# db_url = "sqlite:///data.db"


# 创建引擎
engine = create_engine(DB_URL)

# 模型与数据库表进行关联的基类，模型必须继承于Base
Base = declarative_base(bind=engine)

# 创建session会话
DbSession = sessionmaker(bind=engine)
session = DbSession()


def create_db():
    # 映射模型对应的表
    Base.metadata.create_all()


def drop_db():
    # 删除模型对应的表
    Base.metadata.drop_all()
