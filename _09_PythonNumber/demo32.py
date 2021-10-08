# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数字(Number)
        Python3 degrees()函数
            描述：
                degrees()将弧度转换为角度
            语法：
                import math
                math.degrees(x)
                参数：
                    x -- 一个数值
            返回值：
                返回一个角度值

        注意：degrees()是不能直接访问的，需要导入math模块，然后通过math静态对象调用该方法。
"""
import math

if __name__ == "__main__":
    print("degrees(3)：", math.degrees(3))
    print("degrees(-3)：", math.degrees(-3))
    print("degrees(0)：", math.degrees(0))
    print("degrees(math.pi)：", math.degrees(math.pi))
    print("degrees(math.pi/2)：", math.degrees(math.pi / 2))
    print("degrees(math.pi/4)：", math.degrees(math.pi / 4))
