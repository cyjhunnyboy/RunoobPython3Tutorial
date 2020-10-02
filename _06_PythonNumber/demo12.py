# -*- coding: UTF-8 -*-
# author: chenyongjun
"""
Python3 log() 函数
描述：log() 方法返回x的自然对数，x > 0
语法：import math math.log(x)
     注：log()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法
参数：x -- 数值表达式
返回值：返回x的自然对数，x>0
"""
import math

print("math.log(100.12) : ", math.log(100.12))
print("math.log(100.72) : ", math.log(100.72))
print("math.log(math.pi) : ", math.log(math.pi))
