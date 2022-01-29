# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 计算字典值之和
    给定一个字典，然后计算它们所有数字值的和。
'''


def returnSum(dict):
    sum = 0
    for i in dict:
        sum = sum + dict[i]

    return sum


if __name__ == "__main__":
    dict = {'a': 100, 'b': 200, 'c': 300}
    print("Sum：", returnSum(dict))
