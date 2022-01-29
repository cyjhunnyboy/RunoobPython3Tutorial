# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 函数
global和nonlocal关键字
    当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
'''
num = 1


def func():
    # 需要使用global关键字声明
    global num
    print(num)
    num = 123
    print(num)


if __name__ == "__main__":
    func()
    print(num)
