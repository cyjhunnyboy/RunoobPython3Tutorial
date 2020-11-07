# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 计算元素在列表中出现的次数
    定义一个列表，并计算某个元素在列表中出现的次数。
    例如：
        输入 : lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
        x = 10
        输出 : 3
'''


def countX(lst, x):
    """使用count方法计算x在列表中出现的次数"""

    return lst.count(x)


if __name__ == "__main__":
    lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
    x = 8
    print(countX(lst, x))
