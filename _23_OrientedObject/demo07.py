# -*- coding: UTF-8 -*-
# author: chenyongjun


# 类定义
class People:

    # 定义类的基本属性
    name = ""
    age = 0

    # 定义类的私有属性，私有属性在类外部无法直接进行访问
    __weight = ""

    # 定义类的构造方法
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    # 定义类的普通方法
    def speak(self):
        print("{0:s} 说：我 {1:d} 岁了。".format(self.name, self.age))


# 单继承示例
class Student(People):

    # 定义类的基本属性
    grade = ""

    # 定义类的构造方法
    def __init__(self, name, age, wight, grade):
        # 调用父类的构造方法
        People.__init__(self, name=name, age=age, weight=wight)
        self.grade = grade

    # 覆写父类的方法
    def speak(self):
        print("{0:s} 说：我 {1:d} 岁了，我在读 {2:s} 年级。".format(self.name, self.age, self.grade))


# 定义Speaker类
class Speaker:

    # 定义类的基本属性
    topic = ""
    name = ""

    # 定义类的构造方法
    def __init__(self, name, topic):
        self.name = name
        self.topic = topic

    # 定义类的普通方法
    def speak(self):
        print("我叫{0:s}， 我是一个演说家，我演讲的主题是：{1:s}".format(self.name, self.topic))


# 多重继承
class Sample(Speaker, Student):
    age = ""

    def __init__(self, name, age, weight, grade, topic):
        Student.__init__(self, name, age, weight, grade)
        Speaker.__init__(self, name, topic)


test = Sample("Tim", 25, 80, 4, "Python")
# 方法名同，默认调用的是在括号中排前地父类的方法
test.speak()
