# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 模块
dir() 函数
    内置的函数dir()可以找到模块内定义的所有名称。以一个字符串列表的形式返回
    如果没有给定参数，那么 dir() 函数会罗列出当前定义的所有名称
'''
import _18_PythonModules.tool.fibonacci as fibonacci

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    fibo = fibonacci.fib
    # 建立一个新的变量a
    a = 5
    # 得到一个当前模块中定义的属性列表
    print(dir())
