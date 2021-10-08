# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数字(Number)
        Python3 atan()函数
            描述：
                atan()返回x的反正切弧度值
            语法：
                import math
                math.atan(x)
                参数：
                    x -- 一个数值
            返回值：
                返回x的反正切弧度值

        注意：atan()是不能直接访问的，需要导入math模块，然后通过math静态对象调用该方法。
"""
import math

if __name__ == "__main__":
    print("atan(0.64)：", math.atan(0.64))
    print("atan(0)：", math.atan(0))
    print("atan(10)：", math.atan(10))
    print("atan(-1)：", math.atan(-1))
    print("atan(1)：", math.atan(1))
