# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 合并字典
    给定一个字典，然后计算它们所有数字值的和。
'''


def Merge(dict1, dict2):
    """使用update() 方法，第二个参数合并第一个参数"""

    return (dict2.update(dict1))


if __name__ == "__main__":
    # 两个字典
    dict1 = {'a': 10, 'b': 8}
    dict2 = {'d': 6, 'c': 4}

    # 返回None
    print(Merge(dict1, dict2))

    # dict2合并了dict1
    print(dict2)
