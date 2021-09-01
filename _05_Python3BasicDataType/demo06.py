# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 基本数据类型
        1、Number（数字）
            isinstance和type区别就是:
                type()不会认为子类是一种父类类型。
                isinstance()会认为子类是一种父类类型。
                注意：在Python2中是没有布尔型的，它用数字0表示False，用1表示True。
                到Python3中，把True和False定义成关键字了，但它们的值还是1和0，它们可以和数字相加。
"""


class A:
    pass


class B(A):
    pass


if __name__ == "__main__":
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
