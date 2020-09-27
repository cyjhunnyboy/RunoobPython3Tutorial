# -*- coding: UTF-8 -*-
# author: chen_yong_jun

"""
Python列表脚本操作符
列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表
"""
print(len([1, 2, 3]))   # 长度
print([1, 2, 3] + [4, 5, 6])    # 组合
print(['Hi!'] * 4)      # 重复
print(3 in [1, 2, 3])   # 元素是否存在于列表中
for x in [1, 2, 3]:     # 迭代
    print(x, end=" ")
