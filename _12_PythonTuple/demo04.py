# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 元组
        元组与字符串类似，下标索引从0开始，可以进行截取，组合等
        tup1 = ("Google", "Runoob", 1997, 2000, 26.8, 0)
        正向索引：      0       1      2       3       4     5
                    Google  Runoob  1997    2000    26.8    0
        反向索引：      -6      -5     -4     -3       -2    -1
"""
if __name__ == "__main__":
    # 创建元组
    tuple_1 = ("Google", "Runoob", 1997, 2000, 26.8, 0)

    # 正向索引访问元组
    print(tuple_1[0])
    print(tuple_1[1])
    print(tuple_1[2])
    print(tuple_1[3])
    print(tuple_1[4])
    print(tuple_1[5])

    print("===================")

    # 反向索引访问元组
    print(tuple_1[-1])
    print(tuple_1[-2])
    print(tuple_1[-3])
    print(tuple_1[-4])
    print(tuple_1[-5])
    print(tuple_1[-6])
