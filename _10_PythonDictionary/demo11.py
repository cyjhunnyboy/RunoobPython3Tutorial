# -*- coding: UTF-8 -*-
# author: chenyongjun
"""
描述
Python 字典 fromkeys() 函数用于创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值。
语法
fromkeys()方法语法：
dict.fromkeys(seq[, value])
参数
seq -- 字典键值列表。
value -- 可选参数, 设置键序列（seq）的值
"""

seq = ('name', 'age', 'sex')

dict_a = dict.fromkeys(seq)
print("新的字典为 : %s" % str(dict_a))

dict_a = dict.fromkeys(seq, 10)
print("新的字典为 : %s" % str(dict_a))
