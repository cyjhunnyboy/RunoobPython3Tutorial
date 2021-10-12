# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 元组
        关于元组是不可变的
            所谓元组的不可变指的是元组所指向的内存中的内容不可变
"""
if __name__ == "__main__":
    tuple_1 = ('r', 'u', 'n', 'o', 'o', 'b')
    # 不支持修改元素
    # TypeError: 'tuple' object does not support item assignment
    # tuple_1[0] = 'g'

    # 查看内存地址
    print(id(tuple_1))

    tuple_1 = (1, 2, 3)
    # 内存地址不一样了
    print(id(tuple_1))
