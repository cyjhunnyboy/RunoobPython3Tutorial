# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数字(Number)
        Python3 log10() 函数
            描述：
                log10()方法返回以10为基数的x对数，x>0
            语法：
                import math
                math.log10(x)
                参数：
                    x -- 数值表达式
            返回值：
                返回以10为基数的x对数，x>0

            注：log10()是不能直接访问的，需要导入math模块，通过静态对象调用该方法
"""
import math

if __name__ == "__main__":
    print("math.log10(100.12)：", math.log10(100.12))
    print("math.log10(100.72)：", math.log10(100.72))
    print("math.log10(119)：", math.log10(119))
    print("math.log10(math.pi)：", math.log10(math.pi))
