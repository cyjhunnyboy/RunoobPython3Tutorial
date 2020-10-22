# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 模块
__name__属性
    一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，
    模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。

    说明： 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
    说明：__name__ 与 __main__ 底下是双下划线， _ _ 是这样去掉中间的那个空格。
'''
from _18_PythonModules.tool.fibonacci import *

if __name__ == "__main__":
    # python using_name.py
    print("程序自身在运行")
    fib(1000)
else:
    # import using_name
    print("我来自另一模块")
    print(fib2(100))
