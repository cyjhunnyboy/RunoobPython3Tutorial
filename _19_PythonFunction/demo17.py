# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 函数
        强制位置参数
            Python3.8新增了一个函数形参语法/用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。
            在以下的例子中，形参a和b必须使用指定位置参数，c或d可以是位置形参或关键字形参，而e或f要求为关键字形参
            def f(a, b, /, c, d, *, e, f):
                print(a, b, c, d, e, f)
"""


def fi(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


if __name__ == "__main__":
    # 以下使用方法是正确的
    fi(10, 20, 30, d=40, e=50, f=60)
