# -*- coding: UTF-8 -*-
# author: chenyongjun
"""
还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式
s.update( x )
"""
thisset = {"Google", "Runoob", "Taobao"}
thisset.update({1, 3})
print(thisset)
thisset.update([1, 4], [5, 6])
print(thisset)
