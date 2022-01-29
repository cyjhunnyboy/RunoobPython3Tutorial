# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 面向对象
继承
    Python同样支持类的继承，如果一种语言不支持继承，类就没有什么意义。
    派生类的定义如下所示:
    class DerivedClassName(BaseClassName1):
        <statement-1>
        .
        .
        .
        <statement-N>
    BaseClassName（示例中的基类名）必须与派生类定义在一个作用域内。除了类，
    还可以用表达式，基类定义在另一个模块中时这一点非常有用:
    class DerivedClassName(modname.BaseClassName):
'''


# 类定义
class People:
    """People类"""

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

    # 定义类的普通方法
    def speak(self):
        print("%s说：我%d岁。" % (self.name, self.age))


# 单继承示例
class Student(People):
    """Student类，继承People类"""

    # 定义基本属性
    grade = ""

    # 定义构造方法
    def __init__(self, name, age, weight, grade):
        # 调用父类的构造函数
        People.__init__(self, name, age, weight)
        self.grade = grade

    # 重写父类的方法
    def speak(self):
        print("{0:s}说：我{1:d}岁了，我在读{2:d}年级。".format(self.name, self.age, self.grade))


if __name__ == "__main__":
    # 实例化类
    student = Student("ken", 10, 60, 3)
    student.speak()
