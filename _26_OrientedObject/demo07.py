# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 面向对象
多继承
   Python同样有限的支持多继承形式。
  多继承的类定义形如下：
    class DerivedClassName(Base1, Base2, Base3):
        <statement-1>
        .
        .
        .
        <statement-N>
    需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，
    Python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。
'''


# 类定义
class People:
    """People类"""

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
        print("{0:s}说：我{1:d}岁了。".format(self.name, self.age))


# 单继承示例
class Student(People):
    """Student类，继承People类"""

    # 定义类的基本属性
    grade = ""

    # 定义类的构造方法
    def __init__(self, name, age, wight, grade):
        # 调用父类的构造方法
        People.__init__(self, name=name, age=age, weight=wight)
        self.grade = grade

    # 覆写父类的方法
    def speak(self):
        print("{0:s}说：我{1:d}岁了，我在读{2:s}年级。".format(self.name, self.age, self.grade))


# 另一个类，多重继承之前的准备
class Speaker:
    """Speaker类"""

    # 定义类的基本属性
    topic = ""
    name = ""

    # 定义类的构造方法
    def __init__(self, name, topic):
        self.name = name
        self.topic = topic

    # 定义类的普通方法
    def speak(self):
        print("我叫{0:s}，我是一个演说家，我演讲的主题是：{1:s}".format(self.name, self.topic))


# 多重继承
class Sample(Speaker, Student):
    """Sample类，继承Speaker、Student类"""

    # 定义类的基本属性
    age = ""

    # 定义类的构造方法
    def __init__(self, name, age, weight, grade, topic):
        Student.__init__(self, name, age, weight, grade)
        Speaker.__init__(self, name, topic)


if __name__ == "__main__":
    test = Sample("Tim", 25, 80, 4, "Python")
    # 方法名同，默认调用的是在括号中排前地父类的方法
    test.speak()
