# -*- coding: UTF-8 -*-
# author: chenyongjun
"""
time.localtime([secs]
接收时间辍（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）。
"""
import time

print("localtime(1455508609.34375): ", time.localtime(1455508609.34375))
print("localtime(): ", time.localtime())
