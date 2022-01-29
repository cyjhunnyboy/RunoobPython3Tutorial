# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 错误和异常
抛出异常
    Python使用raise语句抛出一个指定的异常。
    raise语法格式如下：
        raise [Exception [, args [, traceback]]]
'''
if __name__ == "__main__":
    x = 10
    if x > 5:
        # 如果x大于5就触发异常
        raise Exception("x不能大于5，x的值为：{}".format(x))
