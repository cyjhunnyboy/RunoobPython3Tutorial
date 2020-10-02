# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
Python3 字典 get() 方法
描述
Python 字典 get() 函数返回指定键的值，如果值不在字典中返回默认值。
语法
get()方法语法：
dict.get(key, default=None)
参数
key -- 字典中要查找的键。
default -- 如果指定键的值不存在时，返回该默认值值。
返回值
返回指定键的值，如果值不在字典中返回默认值 None。
"""
dict_a = {'Name': 'Runoob', 'Age': 27}

print("Age 值为 : %s" % dict_a.get('Age'))
print("Sex 值为 : %s" % dict_a.get('Sex', "NA"))

