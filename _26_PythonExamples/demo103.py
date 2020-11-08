# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 将时间戳转换为指定格式日期
    给定一个时间戳，将其转换为指定格式的时间。
    注意时区的设置。
'''
import datetime

if __name__ == "__main__":
    # 指定时间戳
    timeStamp = 1557502800
    dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
    otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
    print(otherStyleTime)
