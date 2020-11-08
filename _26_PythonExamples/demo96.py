# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 合并字典
    给定一个字典，然后计算它们所有数字值的和。
'''


def merge(dict1, dict2):
    """使用**，函数将参数以字典的形式导入"""

    res = {**dict1, **dict2}
    return res


if __name__ == "__main__":
    # 两个字典
    dict1 = {'a': 10, 'b': 8}
    dict2 = {'d': 6, 'c': 4}

    dict3 = merge(dict1, dict2)
    print(dict3)
