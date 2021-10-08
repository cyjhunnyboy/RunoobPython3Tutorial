# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数字(Number)
        Python 数字运算
            Python解释器可以作为一个简单的计算器，您可以在解释器里输入一个表达式，它将输出表达式的值。
            表达式的语法很直白： +, -, *和/, 和其它语言（如Pascal或C）里一样。

            注意：在不同的机器上浮点运算的结果可能会不一样
            在整数除法中，除法/总是返回一个浮点数，如果只想得到整数的结果，丢弃可能的分数部分，可以使用运算符//
"""
if __name__ == "__main__":
    # 整数除法返回浮点型
    d = 17 / 3
    print(d)

    # 整数除法返回向下取整后的结果
    e = 17 // 3
    print(e)

    # ％操作符返回除法的余数
    f = 17 % 3
    print(f)

    # //得到的并不一定是整数类型的数，它与分母分子的数据类型有关系
    print(7 // 2)
    print(7.0 // 2)
    print(7 // 2.0)

    # 等号 = 用于给变量赋值。赋值之后，除了下一个提示符，解释器不会显示任何结果
    width = 20
    height = 5 * 9
    print(width * height)

    # Python 可以使用 ** 操作来进行幂运算
    # 5的平方
    g = 5 ** 2
    print(g)

    # 尝试访问一个未定义的变量
    # NameError: name 'n' is not defined
    # print(n)

    # 不同类型的数混合运算时会将整数转换为浮点数
    print(3 * 3.75 / 1.5)
    print(7.0 / 2)

    # 在交互模式中，最后被输出的表达式结果被赋值给变量
    tax = 12.5 / 100
    price = 100.50
    print(tax * price)
