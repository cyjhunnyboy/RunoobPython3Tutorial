# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 获取几天前的时间
    计算几天前并转换为指定格式。
'''
import time
import datetime

if __name__ == "__main__":
    # 给定时间戳
    timeStamp = 1557502800
    dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
    threeDayAgo = dateArray - datetime.timedelta(days=3)
    print(threeDayAgo)
