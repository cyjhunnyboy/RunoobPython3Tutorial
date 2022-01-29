# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python type() 函数
描述：
    type() 函数如果你只有第一个参数则返回对象的类型，三个参数返回新的类型对象
    isinstance() 与 type() 区别：
        type() 不会认为子类是一种父类类型，不考虑继承关系
        isinstance() 会认为子类是一种父类类型，考虑继承关系

    如果要判断两个类型是否相同推荐使用 isinstance()

语法：
    type(object)
    type(name, bases, dict)
    参数：
        name -- 类的名称
        bases -- 基类的元组
        dict -- 字典，类内定义的命名空间变量
返回值：
    一个参数返回对象类型, 三个参数，返回新的类型对象
'''


class X(object):
    a = 1


class A:
    pass


class B(A):
    pass


if __name__ == "__main__":
    # 一个参数实例
    print(type(1))
    print(type("runoob"))
    print(type([2]))
    print(type({0: "zero"}))

    # 判断类型是否相等
    x = 1
    print(type(x) == int)

    # 三个参数
    # 产生一个新的类型 X
    X = type('X', (object,), dict(a=1))
    print(X)

    # type() 与 isinstance()区别
    # returns True
    print(isinstance(A(), A))
    # returns True
    print(type(A()) == A)
    # returns True
    print(isinstance(B(), A))
    # returns False
    print(type(B()) == A)
