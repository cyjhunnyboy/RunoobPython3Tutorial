# -*- coding: UTF-8 -*-
# author: chenyongjun


class Site:

    def __init__(self, name, url):
        self.name = name
        self.__url = url

    def who(self):
        print("name: ", self.name)
        print("url: ", self.__url)

    def __foo(self):    # 私有方法
        print("这是私有方法")

    def foo(self):  # 公共方法
        print("这是公共方法")
        self.__foo()


site = Site("菜鸟教程", "www.runoob.com")
site.who()    # 正常输出
site.foo()    # 正常输出
# site.__foo()  # 报错
