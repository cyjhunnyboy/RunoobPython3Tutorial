# -*- coding: UTF-8 -*-
# author: chenyongjun
"""
time.mktime(tupletime)
接受时间元组并返回时间辍（1970纪元后经过的浮点秒数）。
参数：t -- 结构化的时间或者完整的9位元组元素
返回值：返回用秒数来表示时间的浮点数
"""
import time

t = (2016, 2, 17, 17, 3, 38, 1, 48, 0)
secs = time.mktime(t)
print("time.mktime(t) : %f" % secs)
print("asctime(localtime(secs)): %s" % time.asctime(time.localtime(secs)))
print("time.strftime(format, time.localtime(secs)): %s" % \
      time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(secs)))
