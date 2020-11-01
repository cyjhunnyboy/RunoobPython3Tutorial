# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 错误和异常
定义清理行为
    try语句还有另外一个可选的子句，它定义了无论在任何情况下都会执行的清理行为。

    如果一个异常在try子句里（或者在except和else子句里）被抛出，
    而又没有任何的except把它截住，那么这个异常会在finally子句执行后被抛出。
'''


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        print(e)
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


if __name__ == "__main__":
    divide(2, 1)
    divide(2, 0)
    divide("2", "1")
