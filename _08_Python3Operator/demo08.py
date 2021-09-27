# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 运算符
        Python身份运算符
            is与==区别：is用于判断两个变量引用对象是否为同一个， ==用于判断引用变量的值是否相等。
"""
if __name__ == "__main__":
    a = [1, 2, 3]
    b = a
    print(b is a)
    print(b == a)
    b = a[:]
    print(b is a)
    print(b == a)
