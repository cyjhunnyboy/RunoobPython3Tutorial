# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python __import__() 函数
描述：
    __import__() 函数用于动态加载类和函数
    如果一个模块经常变化就可以使用 __import__() 来动态载入
语法：
    __import__(name[, globals[, locals[, fromlist[, level]]]])
    参数说明：
        name -- 模块名
返回值：
    返回元组列表
'''
import os

__import__("a")  # 导入 a.py 模块
