# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数字(Number)
        Python3 min() 函数
            描述：
                min()方法返回给定参数的最小值，参数可以为序列
            语法：
                min(x, y, z, ....)
                参数：
                    x -- 数值表达式。
                    y -- 数值表达式。
                    z -- 数值表达式。
            返回值：
                返回给定参数的最小值
"""
if __name__ == "__main__":
    print("min(80, 100, 1000)：", min(80, 100, 1000))
    print("min(-20, 100, 400)：", min(-20, 100, 400))
    print("min(-80, -20, -10)：", min(-80, -20, -10))
    print("min(0, 100, -400)：", min(0, 100, -400))
