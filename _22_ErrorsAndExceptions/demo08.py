# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 错误和异常
抛出异常
    Python使用raise语句抛出一个指定的异常。
    raise语法格式如下：
        raise [Exception [, args [, traceback]]]

    raise唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是Exception的子类）。
    如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的raise语句就可以再次把它抛出。
'''
if __name__ == "__main__":
    try:
        raise NameError("HiThere")
    except NameError:
        print("An exception flew by!")
        raise
