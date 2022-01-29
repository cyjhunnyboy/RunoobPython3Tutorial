# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
time.asctime([tupletime])
接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
"""
import time

localtime = time.localtime()
print("time.asctime(t): %s " % time.asctime(localtime))
