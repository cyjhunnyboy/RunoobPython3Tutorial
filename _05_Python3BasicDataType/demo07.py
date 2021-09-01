# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 基本数据类型
        1、Number（数字）

            注意：
                1、Python可以同时为多个变量赋值，如a, b = 1, 2。
                2、一个变量可以通过赋值指向不同类型的对象。
                3、数值的除法包含两个运算符：/返回一个浮点数，//返回一个整数。
                4、在混合计算时，Python会把整型转换成为浮点数。
"""
if __name__ == "__main__":
    # 数值运算
    # 加法
    a = 5 + 4
    # 减法
    b = 4.3 - 2
    # 乘法
    c = 3 * 7
    # 除法，得到一个浮点数
    d = 2 / 4
    # 除法，得到一个整数
    e = 2 // 4
    # 取余
    f = 17 % 3
    # 乘方
    g = 2 ** 5

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
