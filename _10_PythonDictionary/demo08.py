# -*- coding: UTF-8 -*-
# author: chenyongjun
"""
Python 字典 clear() 函数用于删除字典内所有元素。
语法：
dict.clear()
"""
dict_a = {'Name': 'Zara', 'Age': 7}

print("字典长度 : %d" % len(dict_a))
dict_a.clear()
print("字典删除后长度 : %d" % len(dict_a))


