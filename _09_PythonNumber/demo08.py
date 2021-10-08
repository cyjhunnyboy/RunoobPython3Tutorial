# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数字(Number)
        Python3 ceil() 函数
            描述：
                ceil(x)函数返回一个大于或等于x的的最小整数, 返回数字的上入整数，如math.ceil(4.1)返回5
            语法：
                import math
                math.ceil(x)
                参数：
                    x -- 数值表达式
            返回值：
                函数返回返回一个大于或等于x的的最小整数

            注：ceil()是不能直接访问的，需要导入math模块，通过静态对象调用该方法
"""
# 导入math模块
import math

if __name__ == "__main__":
    print("math.ceil(-45.17)：", math.ceil(-45.17))
    print("math.ceil(100.12)：", math.ceil(100.12))
    print("math.ceil(100.72)：", math.ceil(100.72))
    print("math.pi：", math.pi)
    print("math.ceil(math.pi)：", math.ceil(math.pi))
