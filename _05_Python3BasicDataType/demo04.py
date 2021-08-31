# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
    Python3 基本数据类型
        1、Number（数字）
            Python3支持 int、float、bool、complex（复数）。
            在Python3里，只有一种整数类型int，表示为长整型，没有Python2中的Long。
            像大多数语言一样，数值类型的赋值和计算都是很直观的。
            内置的type()函数可以用来查询变量所指的对象类型。
'''
if __name__ == "__main__":
    a, b, c, d = 20, 5.5, True, 4 + 3j
    print(type(a), type(b), type(c), type(d))
