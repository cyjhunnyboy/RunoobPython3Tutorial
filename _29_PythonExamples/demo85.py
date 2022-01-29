# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 判断字符串长度
    给定一个字符串，然后判断该字符串的长度。
'''


def findLen(str):
    """使用循环计算字符串的长度"""

    counter = 0
    while str[counter:]:
        counter += 1
    return counter


if __name__ == "__main__":
    str = "runoob"
    print(len(str))

    print(findLen(str))
