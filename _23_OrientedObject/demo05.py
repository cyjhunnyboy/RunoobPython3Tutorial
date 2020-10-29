# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 面向对象
类的方法
    在类的内部，使用def关键字来定义一个方法，与一般函数定义不同，
    类方法必须包含参数self, 且为第一个参数，self代表的是类的实例。
'''


# 类定义
class People:
    """People类"""

    # 定义基本属性
    name = ""
    age = ""

    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    # 定义类的方法
    def speak(self):
        print("{0:s}说：我{1:d}岁, 体重{2:d}公斤。".format(self.name, self.age, self.__weight))


if __name__ == "__main__":
    # 实例化类
    people = People("John", 20, 45)
    people.speak()
