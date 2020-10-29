# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 错误和异常
try/except...else 语句
    try/except语句还有一个可选的else子句，如果使用这个子句，那么必须放在所有的except子句之后。
    else子句将在try子句没有发生任何异常的时候执行。
    语法格式如下：
        try:
            执行代码
        except:
            发生异常时执行的代码
        else:
            没有异常时执行的代码

    使用else子句比把所有的语句都放在try子句里面要好，这样可以避免一些意想不到，
    而except又无法捕获的异常

    异常处理并不仅仅处理那些直接发生在try子句中的异常，
    而且还能处理子句中调用的函数（甚至间接调用的函数）里抛出的异常
'''


def this_fails():
    x = 1 / 0
    print("The result of divide is: ", x)


if __name__ == "__main__":
    try:
        this_fails()
    except ZeroDivisionError as err:
        print('Handling run-time error: ', err)
