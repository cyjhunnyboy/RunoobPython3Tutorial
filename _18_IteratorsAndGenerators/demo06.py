# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 迭代器与生成器
        生成器
            1、在Python中，使用了yield的函数被称为生成器（generator）。
            2、跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
            3、在调用生成器运行的过程中，每次遇到yield时函数会暂停并保存当前所有的运行信息，
               返回yield的值, 并在下一次执行next()方法时从当前位置继续运行。
            4、调用一个生成器函数，返回的是一个迭代器对象。
"""
import sys


def fibonacci(n):
    """生成器函数 - 斐波那契"""
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


if __name__ == "__main__":
    # f是一个迭代器，由生成器返回生成
    f = fibonacci(10)

    while True:
        try:
            print(next(f), end=" ")
        except StopIteration:
            sys.exit()
