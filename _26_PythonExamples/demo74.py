# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 复制列表
    定义一个列表，并将该列表元素复制到另外一个列表上。
'''


def clone_runoob(li1):
    """定义一个列表，并将该列表元素复制到另外一个列表上"""

    # 使用list()方法
    li_copy = list(li1)
    return li_copy


if __name__ == "__main__":
    li1 = [4, 8, 2, 10, 15, 18]
    li2 = clone_runoob(li1)
    print("原始列表：", li1)
    print("复制后列表：", li2)
