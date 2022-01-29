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


class Site:

    def __init__(self, name, url):
        # public
        self.name = name
        # private
        self.__url = url

    def who(self):
        print("name: ", self.name)
        print("url: ", self.__url)

    # 私有方法
    def __foo(self):
        print("这是私有方法")

    # 公共方法
    def foo(self):
        print("这是公共方法")
        self.__foo()


if __name__ == "__main__":
    site = Site("菜鸟教程", "www.runoob.com")
    # 正常输出
    site.who()
    # 正常输出
    site.foo()
    # 报错
    # AttributeError: 'Site' object
    # has no attribute '__foo'
    site.__foo()
