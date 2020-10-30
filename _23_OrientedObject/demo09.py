# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 面向对象
类属性与方法
    类的私有属性
        __private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。
        在类内部的方法中使用时 self.__private_attrs。
    类的方法
        在类的内部，使用def关键字来定义一个方法，与一般函数定义不同，
        类方法必须包含参数self，且为第一个参数，self代表的是类的实例。
    类的私有方法
        __private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，
        不能在类的外部调用。self.__private_methods。
'''


class JustCounter:
    # 私有变量
    __secretCount = 0
    # 公开变量
    publicCount = 0

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


if __name__ == "__main__":
    counter = JustCounter()
    counter.count()
    counter.count()
    print(counter.publicCount)
    # 报错，实例不能访问私有变量
    # AttributeError: 'JustCounter' object
    # has no attribute '__secretCount'
    print(counter.__secretCount)
