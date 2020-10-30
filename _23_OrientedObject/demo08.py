# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 面向对象
方法重写
    如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法

    super()函数是用于调用父类(超类)的一个方法
'''


# 定义父类
class Parent:

    def my_method(self):
        print("调用父类的方法！")


class Child(Parent):

    def my_method(self):
        print("调用子类的方法！")


if __name__ == "__main__":
    # 子类实例
    child = Child()
    # 子类调用重写的方法
    child.my_method()
    # 用子类对象调用父类已被覆盖的方法
    super(Child, child).my_method()
