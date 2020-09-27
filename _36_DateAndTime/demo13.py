# -*- coding: UTF-8 -*-
# author: chen_yong_jun
"""
time.sleep(secs)
推迟调用线程的运行，secs指秒数。
"""
import time

print("Start : %s" % time.ctime())
time.sleep(5)
print("End : %s" % time.ctime())
