# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数字(Number)
        Python3 max() 函数
            描述：
                max()方法返回给定参数的最大值，参数可以为序列
            语法：
                max(x, y, z, ....)
                参数：
                    x -- 数值表达式。
                    y -- 数值表达式。
                    z -- 数值表达式。
            返回值：
                返回给定参数的最大值
"""
if __name__ == "__main__":
    print("max(80, 100, 1000)：", max(80, 100, 1000))
    print("max(-20, 100, 400)：", max(-20, 100, 400))
    print("max(-80, -20, -10)：", max(-80, -20, -10))
    print("max(0, 100, -400)：", max(0, 100, -400))
