# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 函数
        参数
            以下是调用函数时可使用的正式参数类型：
            1、必需参数
            2、关键字参数
            3、默认参数
            4、不定长参数
        不定长参数
            声明函数时，参数中星号*可以单独出现
                def f(a,b,*,c):
                    return a+b+c
            如果单独出现星号*后的参数必须用关键字传入
"""


def f(a, b, *, c):
    return a + b + c


if __name__ == "__main__":
    # 如果单独出现星号*后的参数必须用关键字传入
    # 报错
    # TypeError: f() takes 2 positional arguments but 3 were given
    # print(f(1, 2, 3))

    # 正常
    print(f(1, 2, c=3))
