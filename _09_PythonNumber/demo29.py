# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数字(Number)

        Python3 hypot()函数
            描述：
                hypot()返回欧几里德范数sqrt(x*x+y*y)
            语法：
                import math
                math.hypot(x,y)
                参数：
                    x -- 一个数值
                    y -- 一个数值
            返回值：
                返回欧几里德范数sqrt(x*x+y*y)

        注意：hypot()是不能直接访问的，需要导入math模块，然后通过math静态对象调用该方法。
"""
import math

if __name__ == "__main__":
    print("hypot(3, 2)：", math.hypot(3, 2))
    print("hypot(-3, 3)：", math.hypot(-3, 3))
    print("hypot(0, 2)：", math.hypot(0, 2))
