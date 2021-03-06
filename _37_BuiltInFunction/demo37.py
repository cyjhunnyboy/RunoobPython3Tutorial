# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python super() 函数
描述：
    super() 函数是用于调用父类(超类)的一个方法
    super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题
    MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表
语法：
    super(type[, object-or-type])
    参数：
        type -- 类
        object-or-type -- 类，一般是 self

    Python3.x 和 Python2.x 的一个区别是: Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx
'''


class Parent:

    def add(self, x):
        y = x + 1
        print(y)


class Child(Parent):

    def add(self, x):
        # super(Child, self).add(x)
        super().add(x)


if __name__ == "__main__":
    child = Child()
    # 结果为3
    child.add(2)
