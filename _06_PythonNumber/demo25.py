# -*- coding: UTF-8 -*-
# author: chen_yong_jun
"""
Python3 asin()函数
描述：asin()返回x的反正弦弧度值
语法：
import math
math.asin(x)
注意：asin()是不能直接访问的，需要导入math模块，然后通过math静态对象调用该方法。
参数：x -- -1到1之间的数值。如果x是大于1，会产生一个错误
返回值：返回x的反正弦弧度值
"""
import math

print("asin(0.64) : ",  math.asin(0.64))
print("asin(0) : ",  math.asin(0))
print("asin(-1) : ",  math.asin(-1))
print("asin(1) : ",  math.asin(1))

