# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 将时间戳转换为指定格式日期
    给定一个时间戳，将其转换为指定格式的时间。
    注意时区的设置。
'''
import datetime

if __name__ == "__main__":
    # 获得当前时间
    now = datetime.datetime.now()
    # 转换为指定的格式
    otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    print(otherStyleTime)
