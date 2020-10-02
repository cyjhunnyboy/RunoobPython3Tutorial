# -*- coding: UTF-8 -*-
# author: chenyongjun


# 定义父类
class Parent:

    def my_method(self):
        print("调用父类的方法！")


class Child(Parent):

    def my_method(self):
        print("调用子类的方法！")


# 子类实例
child = Child()
# 子类调用重写的方法
child.my_method()
# 用子类对象调用父类已被覆盖的方法
super(Child, child).my_method()
