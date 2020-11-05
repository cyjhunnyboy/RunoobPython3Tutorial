# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python fabs() 与 abs() 区别
    Python 中 fabs(x) 方法返回 x 的绝对值。虽然类似于 abs() 函数，但是两个函数之间存在以下差异：
    abs() 是一个内置函数，而 fabs() 在 math 模块中定义的
    fabs() 函数只适用于 float 和 integer 类型，而 abs() 也适用于复数。
'''
import math

if __name__ == "__main__":
    a = -1
    b = -1.3232
    c = b
    d = 1 + 1.0j
    e = 3 + 4.0j
    print("a的绝对值是：", abs(a))
    print("b的绝对值是：", abs(b))
    print("c的绝对值是：", math.fabs(c))
    print("d的的绝对值是：", abs(d))
    print("e的绝对值是：", abs(e))
    # TypeError: can't convert complex to float
    # fabs 无法将复数转换为浮点型
    print("e的绝对值是：", math.fabs(e))
