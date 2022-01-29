# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 enumerate() 函数
描述：
    enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
语法：
    enumerate(sequence, [start=0])
    参数：
        sequence -- 一个序列、迭代器或其他支持迭代对象
        start -- 下标起始位置
返回值：
    返回 enumerate(枚举) 对象
'''
if __name__ == "__main__":
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    print(list(enumerate(seasons)))
    print(list(enumerate(seasons, start=1)))

    # 普通for循环
    i = 0
    seq = ['one', 'two', 'three']
    for element in seq:
        print(i, seq[i])
        i += 1
    print("=================")

    # for 循环使用 enumerate
    seq = ['one', 'two', 'three']
    for i, element in enumerate(seq):
        print(i, element)
