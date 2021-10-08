# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数字(Number)
        Python3 log() 函数
            描述：
                log()方法返回x的自然对数，x>0
            语法：
                import math
                math.log(x)
                参数：
                    x -- 数值表达式
            返回值：
                返回x的自然对数，x>0

            注：log()是不能直接访问的，需要导入math模块，通过静态对象调用该方法
"""
import math

if __name__ == "__main__":
    print("math.log(100.12)：", math.log(100.12))
    print("math.log(100.72)：", math.log(100.72))
    print("math.log(math.pi)：", math.log(math.pi))
