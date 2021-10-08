# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数字(Number)
        Python3 radians()函数
            描述：
                radians()方法将角度转换为弧度
            语法：
                import math
                math.radians(x)
                参数：
                    x -- 一个数值
            返回值：
                返回一个角度的弧度值

        注意：radians()是不能直接访问的，需要导入math模块，然后通过math静态对象调用该方法。
"""
import math

if __name__ == "__main__":
    print("radians(3)：", math.radians(3))
    print("radians(-3)：", math.radians(-3))
    print("radians(0)：", math.radians(0))
    print("radians(math.pi)：", math.radians(math.pi))
    print("radians(math.pi/2)：", math.radians(math.pi / 2))
    print("radians(math.pi/4)：", math.radians(math.pi / 4))
