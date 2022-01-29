# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 获取几天前的时间
    计算几天前并转换为指定格式。
'''
import time
import datetime

if __name__ == "__main__":
    # 先获得时间数组格式的日期
    threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days=3))
    # 转换为时间戳
    timeStamp = int(time.mktime(threeDayAgo.timetuple()))
    # 转换为其他字符串格式
    otherStyleTime = threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")
    print(otherStyleTime)
