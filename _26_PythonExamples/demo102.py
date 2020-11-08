# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 将时间戳转换为指定格式日期
    给定一个时间戳，将其转换为指定格式的时间。
    注意时区的设置。
'''
import time

if __name__ == "__main__":
    # 指定时间戳
    timeStamp = 1557502800
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(otherStyleTime)
