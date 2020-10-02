# -*- coding: UTF-8 -*-
# author: chenyongjun
import time

"""
获取格式化的时间
你可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime()
"""
localtime = time.asctime(time.localtime(time.time()))
print("本地时间为：", localtime)
