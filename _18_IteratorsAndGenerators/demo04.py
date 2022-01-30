# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 迭代器与生成器
        创建一个迭代器
            把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__()与__next__()
            如果你已经了解的面向对象编程，就知道类都有一个构造函数，Python的构造函数为__init__(), 它会在对象初始化的时候执行
            __iter__()方法返回一个特殊的迭代器对象， 这个迭代器对象实现了__next__()方法并通过StopIteration异常标识迭代的完成
            __next__()方法（Python2里是next()）会返回下一个迭代器对象
"""


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
