# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数字(Number)
        Python3 sin()函数
            描述：
                sin()返回的x弧度的正弦值
            语法：
                import math
                math.sin(x)
                参数：
                    x -- 一个数值
            返回值：
                返回的x弧度的正弦值，数值在-1到1之间

        注意：sin()是不能直接访问的，需要导入math模块，然后通过math静态对象调用该方法。
"""
import math

if __name__ == "__main__":
    print("sin(3)：", math.sin(3))
    print("sin(-3)：", math.sin(-3))
    print("sin(0)：", math.sin(0))
    print("sin(math.pi)：", math.sin(math.pi))
    print("sin(math.pi/2)：", math.sin(math.pi / 2))
