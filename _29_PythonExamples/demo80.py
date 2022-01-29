# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 计算列表元素之积
    定义一个数字列表，并计算列表元素之积。
    例如：
        输入 : list1 = [1, 2, 3]
        输出 : 6
        计算：1 * 2 * 3
'''


def multiplyList(lst):
    """计算列表元素之积"""

    result = 1
    for i in lst:
        result = result * i
    return result


if __name__ == "__main__":
    list1 = [1, 2, 3]
    list2 = [3, 2, 4]
    print(multiplyList(list1))
    print(multiplyList(list2))
