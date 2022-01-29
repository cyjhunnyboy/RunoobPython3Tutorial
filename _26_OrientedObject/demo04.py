# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 面向对象
self
    self代表类的实例，而非类
    类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是self

    从执行结果可以很明显的看出，self代表的是类的实例，代表当前对象的地址，而self.class则指向类

    self不是Python关键字，我们把他换成runoob也是可以正常执行的
'''


class Test:

    def print_test(runoob):
        print(runoob)
        print(runoob.__class__)


if __name__ == "__main__":
    t = Test()
    t.print_test()
