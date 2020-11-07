# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 计算列表元素之和
    定义一个数字列表，并计算列表元素之和。
    例如：
        输入: [12, 15, 3, 10] 输出: 40
'''


def sumOfList(lst, size):
    """使用递归方式计算列表的和"""

    if (size == 0):
        return 0
    else:
        return lst[size - 1] + sumOfList(lst, size - 1)


if __name__ == "__main__":
    #  使用递归
    lst = [11, 5, 17, 18, 23]

    total = sumOfList(lst, len(lst))
    print("列表元素之和为：", total)
