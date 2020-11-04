# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 获取昨天日期
'''
# 引入 datetime 模块
import datetime


def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday


if __name__ == "__main__":
    # 输出
    print(getYesterday())
