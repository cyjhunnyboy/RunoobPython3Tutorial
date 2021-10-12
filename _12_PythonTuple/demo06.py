# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 元组
        修改元组
            元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
"""
if __name__ == "__main__":
    tup_b = (12, 34.56)
    tup_c = ("abc", "xyz")

    # 以下修改元组元素操作是非法的
    # TypeError: 'tuple' object does not support item assignment
    # tup_b[0] = 100

    # 创建一个新的元组
    tup_d = tup_b + tup_c
    print(tup_d)
