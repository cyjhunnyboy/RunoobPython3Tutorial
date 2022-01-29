# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 模块
dir() 函数
    内置的函数dir()可以找到模块内定义的所有名称。以一个字符串列表的形式返回
'''
import _18_PythonModules.tool.fibonacci as fibo, sys

if __name__ == "__main__":
    # 函数dir()可以找到模块内定义的所有名称
    print(dir(fibo))
