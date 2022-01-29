# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 翻转列表
    定义一个列表，并将它翻转。
    例如，对调第一个和第三个元素：
        翻转前 : list = [10, 11, 12, 13, 14, 15]
        翻转后 : [15, 14, 13, 12, 11, 10]
'''


def Reverse(lst):
    """翻转列表"""

    new_lst = lst[::-1]
    return new_lst


if __name__ == "__main__":
    lst = [10, 11, 12, 13, 14, 15]
    print(Reverse(lst))
