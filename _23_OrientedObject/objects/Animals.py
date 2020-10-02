# -*- coding: UTF-8 -*-
# author: chenyongjun


class Animals(object):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def print_animal(self):
        print("The animal name is: {0:s}".format(self.name))

    def print_class(self):
        print(self)


class Cats(Animals):

    def __init__(self, name, food):
        Animals.__init__(self, name)
        self.__food = food

    def print_animal(self):
        print("The animal name is {0:s}, it like to eat {1:s}".format(self.name, self.__food))

    def print_class(self):
        print(self)


if __name__ == "__main__":
    cat = Cats("Prosperous wealth", "bone")
    cat.print_animal()
    cat.print_class()

    animal = Animals("Dog")
    animal.print_animal()
    animal.print_class()
