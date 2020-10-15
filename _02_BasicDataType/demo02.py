# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Number（数字）
    Python3支持 int、float、bool、complex（复数）。
    在Python3里，只有一种整数类型int，表示为长整型，没有Python2中的Long。
    像大多数语言一样，数值类型的赋值和计算都是很直观的。
    内置的type()函数可以用来查询变量所指的对象类型。

isinstance和type区别就是:
    type()不会认为子类是一种父类类型。
    isinstance()会认为子类是一种父类类型。
    注意：在Python2中是没有布尔型的，它用数字0表示False，用1表示True。
    到Python3中，把True和False定义成关键字了，但它们的值还是1和0，它们可以和数字相加。

注意：
    1、Python可以同时为多个变量赋值，如a, b = 1, 2。
    2、一个变量可以通过赋值指向不同类型的对象。
    3、数值的除法包含两个运算符：/返回一个浮点数，//返回一个整数。
    4、在混合计算时，Python会把整型转换成为浮点数。
'''


class A:
    pass


class B(A):
    pass


if __name__ == "__main__":
    a, b, c, d = 20, 5.5, True, 4 + 3j
    print(type(a), type(b), type(c), type(d))

    a = 111
    print(isinstance(a, int))

    # return True
    print(isinstance(A(), A))
    # return True
    print(isinstance(B(), A))
    # return True
    print(type(A()) == A)
    # return False
    print(type(B()) == A)

    # 当你指定一个值时，Number对象就会被创建：
    # del语句删除一些对象引用
    # 语法：del var1[,var2[,var3[....,varN]]]
    var1 = 1
    var2 = 10

    # 使用del语句删除单个或多个对象
    del var1, var2

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
