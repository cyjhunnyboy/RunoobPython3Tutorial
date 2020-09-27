# -*- coding: UTF-8 -*-
# author: chen_yong_jun
"""
Python3 floor() 函数
描述：floor(x) 返回数字的下舍整数，小于或等于 x
语法：import math math.floor(x)
     注：floor()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法
参数：x -- 数值表达式
返回值：返回小于或等于 x 的整数
"""
import math

print("math.floor(-45.17) : ", math.floor(-45.17))
print("math.floor(100.12) : ", math.floor(100.12))
print("math.floor(100.72) : ", math.floor(100.72))
print("math.floor(math.pi) : ", math.floor(math.pi))
