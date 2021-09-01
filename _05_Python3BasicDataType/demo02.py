# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 基本数据类型
        1、多个变量赋值
            Python允许你同时为多个变量赋值。
            创建一个整型对象，值为1，从后向前赋值，三个变量被赋予相同的数值
            a = b = c = 1
"""
if __name__ == "__main__":
    # 创建一个整型对象，值为1
    # 从后向前赋值，三个变量被赋予相同的数值
    a = b = c = 1

    print("a = ", a)
    print("b = ", b)
    print("c = ", c)

    # 也可以为多个对象指定多个变量
    d, e, f = 1, 2, "runoob"

    print("d = ", d)
    print("e = ", e)
    print("f = ", f)
