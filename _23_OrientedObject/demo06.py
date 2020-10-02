# -*- coding: UTF-8 -*-
# author: chenyongjun


# 类定义
class People:

    # 定义基本属性
    name = ""
    age = 0

    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    def speak(self):
        print("%s 说：我 %d 岁。" % (self.name, self.age))


# 单继承示例
class Student(People):

    grade = ""

    def __init__(self, name, age, weight, grade):
        # 调用父类的构造函数
        People.__init__(self, name, age, weight)
        self.grade = grade

    # 重写父类的方法
    def speak(self):
        print("{0:s} 说：我 {1:d} 岁了，我在读 {2:d} 年级。".format(self.name, self.age, self.grade))


student = Student("ken", 10, 60, 3)
student.speak()
