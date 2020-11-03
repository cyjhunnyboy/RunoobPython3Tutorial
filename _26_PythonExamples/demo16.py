# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 判断字符串是否为数字
    创建自定义函数is_number()方法来判断字符串是否为数字
'''
import unicodedata


def is_number(s):
    """is_number()方法来判断字符串是否为数字"""

    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        unicodedata.numeric(s)
        return True
    except(TypeError, ValueError):
        pass

    return False


if __name__ == "__main__":
    # 测试字符串和数字
    print(is_number("foo"))
    print(is_number("1"))
    print(is_number("1.3"))
    print(is_number("-1.37"))
    print(is_number("1e3"))
    print("============")

    # 测试Unicode
    # 阿拉伯语5
    print(is_number("٥"))
    # 泰语2
    print(is_number("๒"))
    # 中文数字
    print(is_number("四"))
    # 版权号
    print(is_number("©"))
