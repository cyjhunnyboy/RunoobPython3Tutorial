# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数字(Number)
        Python3 cos()函数
            描述：
                cos()返回x的弧度的余弦值
            语法：
                import math
                math.cos(x)
                参数：
                    x -- 一个数值
            返回值：
                返回x的弧度的余弦值，-1到 1之间

        注意：cos()是不能直接访问的，需要导入math模块，然后通过math静态对象调用该方法。
"""
import math

if __name__ == "__main__":
    print("cos(3)：", math.cos(3))
    print("cos(-3)：", math.cos(-3))
    print("cos(0)：", math.cos(0))
    print("cos(math.pi)：", math.cos(math.pi))
    print("cos(2*math.pi)：", math.cos(2 * math.pi))
