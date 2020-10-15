# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
    Python3基本数据类型
        Python中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
        在Python中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
        等号（=）用来给变量赋值。
        等号（=）运算符左边是一个变量名，等号（=）运算符右边是存储在变量中的值。

    多个变量赋值
        Python允许你同时为多个变量赋值。
        创建一个整型对象，值为 1，从后向前赋值，三个变量被赋予相同的数值
        a = b = c = 1

    标准数据类型
        Python3中有六个标准的数据类型：
            Number（数字）
            String（字符串）
            List（列表）
            Tuple（元组）
            Set（集合）
            Dictionary（字典）
        Python3的六个标准数据类型中：
            不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
            可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
'''
if __name__ == "__main__":
    # 整型变量
    counter = 100
    # 浮点型变量
    miles = 1000.0
    # 字符串
    name = "runoob"

    print(counter)
    print(miles)
    print(name)

    # 创建一个整型对象，值为1
    # 从后向前赋值，三个变量被赋予相同的数值
    a = b = c = 1

    print("a = ", a)
    print("b = ", b)
    print("c = ", c)

    # 也可以为多个对象指定多个变量
    d, e, f = 1, 2, "runoob"

    print("d = ", d)
    print("e = ", e)
    print("f = ", f)
