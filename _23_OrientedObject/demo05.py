# -*- coding: UTF-8 -*-
# author: chenyongjun


# 类定义
class People:

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
        print("{0:s} 说：我 {1:d} 岁, 体重 {2:d} 公斤".format(self.name, self.age, self.__weight))


if __name__ == "__main__":
    # 实例化类
    people = People("John", 20, 45)
    people.speak()
