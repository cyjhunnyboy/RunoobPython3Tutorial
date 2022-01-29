# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 函数
global和nonlocal关键字
    当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
    如果要修改嵌套作用域（enclosing作用域，外层非全局作用域）中的变量则需要nonlocal关键字了
'''


def outer():
    num = 10

    def inner():
        # nonlocal关键字声明
        nonlocal num
        print(num)
        num = 100
        print(num)

    inner()
    print(num)


if __name__ == "__main__":
    outer()
