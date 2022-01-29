# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 将列表中的头尾两个元素对调
    定义一个列表，并将列表中的头尾两个元素对调。
'''


def swap_list(new_list):
    """将列表中的头尾两个元素对调"""

    get = new_list[-1], new_list[0]
    new_list[0], new_list[-1] = get

    return new_list


if __name__ == "__main__":
    new_list = [1, 2, 3, 4, 5, 6]
    print(swap_list(new_list))
