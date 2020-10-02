# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
Python3 集合
集合（set）是一个无序不重复元素的序列。

可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
"""
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)   # 这里演示的是去重功能
print('orange' in basket)  # 快速判断元素是否在集合内
print('crabgrass' in basket)  # 快速判断元素是否在集合内
# 下面展示两个集合间的运算.
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)    # 集合a中包，集合b中不包含的含元素
print(a | b)    # 集合a或b中包含的所有元素
print(a & b)    # 集合a和b中都包含了的元素
print(a ^ b)    # 不同时包含于a和b的元素
