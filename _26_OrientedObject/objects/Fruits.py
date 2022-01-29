# -*- coding: UTF-8 -*-
# author: chenyongjun


class Fruit(object):

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def print_fruit(self):
        print("The fruit is: {0:s}".format(self.__name))

    def print_class(self):
        print(self)
        print(self.__class__)


if __name__ == "__main__":
    fruit = Fruit("Banana")
    fruit.print_fruit()
    fruit.print_class()
