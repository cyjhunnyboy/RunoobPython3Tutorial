# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 迭代器与生成器
迭代器
    迭代是Python最强大的功能之一，是访问集合元素的一种方式。
    迭代器是一个可以记住遍历的位置的对象。
    迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
    迭代器有两个基本的方法：iter()和next()。
    字符串，列表或元组对象都可用于创建迭代器
创建一个迭代器
    把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__()与__next__()
    如果你已经了解的面向对象编程，就知道类都有一个构造函数，Python的构造函数为__init__(), 它会在对象初始化的时候执行
    __iter__()方法返回一个特殊的迭代器对象， 这个迭代器对象实现了__next__()方法并通过StopIteration异常标识迭代的完成
    __next__()方法（Python2里是next()）会返回下一个迭代器对象
'''


class MyNumbers:
    """创建一个返回数字的迭代器，初始值为1，逐步递增1"""

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


if __name__ == "__main__":
    myClass = MyNumbers()
    myIter = iter(myClass)
    print(next(myIter))
    print(next(myIter))
    print(next(myIter))
    print(next(myIter))
    print(next(myIter))
