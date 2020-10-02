# -*- coding: UTF-8 -*-
# author: chenyongjun
"""
time.strftime(fmt[,tupletime])
接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。
"""
import time

struct_time = time.strptime("30 Nov 00", "%d %b %y")
print("返回元组: ", struct_time)
