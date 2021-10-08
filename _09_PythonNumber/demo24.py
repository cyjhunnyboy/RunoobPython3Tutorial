# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数字(Number)
        三角函数
            Python包括以下三角函数
                acos(x)：返回x的反余弦弧度值。
                asin(x)：返回x的反正弦弧度值。
                atan(x)：返回x的反正切弧度值。
                atan2(y,x)：返回给定的X及Y坐标值的反正切值。
                cos(x)：返回x的弧度的余弦值。
                hypot(x,y)：返回欧几里德范数sqrt(x*x+y*y)。
                sin(x)：返回的x弧度的正弦值。
                tan(x)：返回x弧度的正切值。
                degrees(x)：将弧度转换为角度，如degrees(math.pi/2)，返回90.0
                radians(x)：将角度转换为弧度

        Python3 acos() 函数
            描述：
                acos()返回x的反余弦弧度值
            语法：
                import math
                math.acos(x)
                参数：
                    x -- -1到1之间的数值。如果x是大于1，会产生一个错误
            返回值：
                返回x的反余弦弧度值

        注意：acos()是不能直接访问的，需要导入math模块，然后通过math静态对象调用该方法。
"""
import math

if __name__ == "__main__":
    print("acos(0.64)：", math.acos(0.64))
    print("acos(0)：", math.acos(0))
    print("acos(-1)：", math.acos(-1))
    print("acos(1)：", math.acos(1))
