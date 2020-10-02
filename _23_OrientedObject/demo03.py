# -*- coding: UTF-8 -*-
# author: chenyongjun


class Test:

    def print_test(self):
        print(self)
        print(self.__class__)


if __name__ == "__main__":
    t = Test()
    t.print_test()
