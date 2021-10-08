# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数字(Number)
        Python3 atan2()函数
            描述：
                atan2()返回x的反正切弧度值
            语法：
                import math
                math.atan2(y, x)
                参数：
                    x -- 一个数值
                    y -- 一个数值
            返回值：
                返回给定的X及Y坐标值的反正切值

        注意：atan2()是不能直接访问的，需要导入math模块，然后通过math静态对象调用该方法。
"""
import math

if __name__ == "__main__":
    print("atan2(-0.50,-0.50)：", math.atan2(-0.50, -0.50))
    print("atan2(0.50,0.50)：", math.atan2(0.50, 0.50))
    print("atan2(5,5)：", math.atan2(5, 5))
    print("atan2(-10,10)：", math.atan2(-10, 10))
    print("atan2(10,20)：", math.atan2(10, 20))
