# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 将时间戳转换为指定格式日期
    给定一个时间戳，将其转换为指定格式的时间。
    注意时区的设置。
'''
import time

if __name__ == "__main__":
    # 获得当前时间时间戳
    now = int(time.time())
    # 转换为其他日期格式,如："%Y-%m-%d %H:%M:%S"
    timeArray = time.localtime(now)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(otherStyleTime)
