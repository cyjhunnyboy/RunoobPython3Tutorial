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
'''
import sys

if __name__ == "__main__":
    # try语句中判断文件是否可以打开，如果打开文件时正常的
    # 没有发生异常则执行else部分的语句，读取文件内容
    for arg in sys.argv[1:]:
        try:
            f = open(arg, "r")
        except IOError:
            print("cannot open", arg)
        else:
            print(arg, "has", len(f.readlines()), "lines")
            f.close()
