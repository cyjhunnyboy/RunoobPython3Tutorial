# -*- coding: UTF-8 -*-
# author: chenyongjun
import time

"""
time.clock()
用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。
返回值：
该函数有两个功能，
在第一次调用的时候，返回的是程序运行的实际时间；
以第二次之后的调用，返回的是自第一次调用后,到这次调用的时间间隔
在win32系统下，这个函数返回的是真实时间（wall time），而在Unix/Linux下返回的是CPU时间
"""


def procedure():
    time.sleep(2.5)


# time.clock
t0 = time.clock()
procedure()
print(time.clock() - t0)

# time.time
t0 = time.time()
procedure()
print(time.time() - t0)
