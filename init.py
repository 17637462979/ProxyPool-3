"""
初始化

Date:       2018/04/29
"""

from models.models import *


def create_tables():
    """
    数据库初始化
    :return:
    """
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    create_tables()
