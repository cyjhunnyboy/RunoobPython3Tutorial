# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python id() 函数
描述：
    id() 函数返回对象的唯一标识符，标识符是一个整数
    CPython 中 id() 函数用于获取对象的内存地址
语法：
    id([object])
    参数说明：
        object -- 对象
返回值：
    返回对象的内存地址
'''
if __name__ == "__main__":
    a = "runoob"
    print(id(a))
    b = 1
    print(id(b))
