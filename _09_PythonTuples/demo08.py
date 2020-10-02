# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
元组内置函数
Python元组包含了以下内置函数
"""
# len(tuple) 计算元组元素个数。
tuple1 = ('Google', 'Runoob', 'Taobao')
print(len(tuple1))

# max(tuple) 返回元组中元素最大值。
tuple2 = ('5', '4', '8')
print(max(tuple2))

# min(tuple) 返回元组中元素最小值。
print(min(tuple2))

# tuple(seq) 将列表转换为元组。
list1 = ['Google', 'Taobao', 'Runoob', 'Baidu']
tuple1 = tuple(list1)
print(tuple1)




