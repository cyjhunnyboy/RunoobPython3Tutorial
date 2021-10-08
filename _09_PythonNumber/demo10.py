# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数字(Number)
        Python3 fabs() 函数
            描述：
                fabs()方法返回数字的绝对值，如math.fabs(-10)返回10.0
                abs()是内置函数。fabs()函数在math模块中定义
                fabs()函数只对浮点型跟整型数值有效。abs()还可以运用在复数中
            语法：
                import math
                math.fabs(x)
                参数：
                    x -- 数值表达式
            返回值：
                返回数字的绝对值

            注：fabs()是不能直接访问的，需要导入math模块，通过静态对象调用该方法
"""
# 导入math模块
import math

if __name__ == "__main__":
    print("math.fabs(-45.17)：", math.fabs(-45.17))
    print("math.fabs(100.12)：", math.fabs(100.12))
    print("math.fabs(100.72)：", math.fabs(100.72))
    print("math.fabs(math.pi)：", math.fabs(math.pi))
