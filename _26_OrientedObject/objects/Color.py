# -*- coding: UTF-8 -*-
# author: chenyongjun


class Color(object):

    def __init__(self, name, color):
        self.__name = name
        self.__color = color

    def color(self, a):
        print("executing the foo(%s, %s)" % (self, a))
        print("self: ", self)

    @classmethod
    def class_color(cls, a):
        print("executing the class_foo(%s, %s)" % (cls, a))
        print("cls: ", cls)

    @staticmethod
    def static_color(a):
        print("executing static_foo(%s)" % a)


class Red(Color):
    pass


if __name__ == "__main__":
    x = Color("Jack", "red")
    print(x.color)
    print(x.class_color)
    print(x.static_color)

    # color可通过实例a调用，类对像Color直接调用会参数错误
    x.color(3)
    # 但color如下方式可以使用正常，显式的传递实例参数x
    Color.color(x, 3)

    # class_color通过类对象或对象实例调用
    x.class_color(3)
    Color.class_color(3)

    # static_color通过类对象或对象实例调用
    x.static_color(3)
    Color.static_color(3)

    y = Red("John", "red")
    # 继承与覆盖普通类函数是一样的
    y.color(3)
    y.class_color(3)
    y.static_color(3)

    Red.color(y, 3)
    Red.class_color(3)
    Red.static_color(3)
