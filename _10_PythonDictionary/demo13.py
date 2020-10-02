# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
Python3 字典 in 操作符
描述
Python 字典 in 操作符用于判断键是否存在于字典中，如果键在字典dict里返回true，否则返回false。
语法
in 操作符语法：
key in dict
参数
key -- 要在字典中查找的键。
"""
dict_a = {'Name': 'Runoob', 'Age': 7}

# 检测键 Age 是否存在
if 'Age' in dict_a:
    print("键 Age 存在")
else:
    print("键 Age 不存在")

# 检测键 Sex 是否存在
if 'Sex' in dict_a:
    print("键 Sex 存在")
else:
    print("键 Sex 不存在")
