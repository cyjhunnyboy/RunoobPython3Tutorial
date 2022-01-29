# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python abs()函数
描述：
    函数返回数字的绝对值。
语法：
    abs( x )
    参数：
        x -- 数值表达式，可以是整数，浮点数，复数。
返回值：
    函数返回 x（数字）的绝对值，如果参数是一个复数，则返回它的大小。
'''
if __name__ == "__main__":
    print("abs(-40)：", abs(-40))
    print("abs(100.10)：", abs(100.10))
    print("abs(3 + 0.5j)：", abs(3 + 4.0j))
