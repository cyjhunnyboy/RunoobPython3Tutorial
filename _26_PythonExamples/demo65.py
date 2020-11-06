# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 将列表中的指定位置的两个元素对调
    定义一个列表，并将列表中的指定位置的两个元素对调。

    例如，对调第一个和第三个元素：
        对调前: List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
        对调后: [19, 65, 23, 90]
'''


def swapPositions(list, pos1, pos2):
    """将列表中的指定位置的两个元素对调"""

    get = list[pos1], list[pos2]

    list[pos2], list[pos1] = get

    return list


if __name__ == "__main__":
    List = [23, 65, 19, 90]
    pos1, pos2 = 1, 3

    # 列表索引是从下标0开始的，所以需要减1
    print(swapPositions(List, pos1 - 1, pos2 - 1))
