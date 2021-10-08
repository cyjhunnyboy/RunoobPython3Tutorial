# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数字(Number)
        Python3 tan()函数
            描述：
                tan()返回x弧度的正切值
            语法：
                import math
                math.tan(x)
                参数：
                    x -- 一个数值
            返回值：
                返回x弧度的正切值，数值在-1到1之间

        注意：tan()是不能直接访问的，需要导入math模块，然后通过math静态对象调用该方法。
"""
import math

if __name__ == "__main__":
    print("(tan(3)：", math.tan(3))
    print("tan(-3)：", math.tan(-3))
    print("tan(0)：", math.tan(0))
    print("tan(math.pi)：", math.tan(math.pi))
    print("tan(math.pi/2)：", math.tan(math.pi / 2))
    print("tan(math.pi/4)：", math.tan(math.pi / 4))
