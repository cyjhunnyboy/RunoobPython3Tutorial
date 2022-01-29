# -*- coding: UTF-8 -*-
# author: chenyongjun


class Description(object):

    def __get__(self, instance, owner):
        print("self in Description: %s" % self)
        print(self, instance, owner)


class Test:
    x = Description()

    def print_test(self):
        print("self in Test: %s" % self)


if __name__ == "__main__":
    test = Test()
    test.print_test()
    Test.x
