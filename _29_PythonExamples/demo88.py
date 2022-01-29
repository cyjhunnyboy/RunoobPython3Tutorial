# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 字符串翻转
    给定一个字符串，然后将其翻转，逆序输出。
'''
# reduce + lambda 反转法
from functools import reduce

if __name__ == "__main__":
    str = "Runoob"
    print(str[::-1])
    print(''.join(reversed(str)))
    print(reduce(lambda x, y: y + x, str))
