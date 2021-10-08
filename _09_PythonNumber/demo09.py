# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数字(Number)
        Python3 exp() 函数
            描述：
                exp()方法返回x的指数，e^x
            语法：
                import math
                math.exp(x)
                参数：
                    x -- 数值表达式
            返回值：
                返回x的指数，e^x

            注：exp()是不能直接访问的，需要导入math模块，通过静态对象调用该方法
"""
# 导入math模块
import math

if __name__ == "__main__":
    print("math.exp(-45.17)：", math.exp(-45.17))
    print("math.exp(100.12)：", math.exp(100.12))
    print("math.exp(100.72)：", math.exp(100.72))
    print("math.exp(math.pi)：", math.exp(math.pi))
