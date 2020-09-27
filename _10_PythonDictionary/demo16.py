# -*- coding: UTF-8 -*-
# author: chen_yong_jun

"""
Python3 字典 setdefault() 方法
描述
Python 字典 setdefault() 方法和get()方法类似, 如果键不已经存在于字典中，将会添加键并将值设为默认值。

语法
setdefault()方法语法：

dict.setdefault(key, default=None)
参数
key -- 查找的键值。
default -- 键不存在时，设置的默认键值。
返回值
如果 key 在 字典中，返回对应的值。如果不在字典中，则插入 key 及设置的默认值 default，并返回 default ，default 默认值为 None
"""
dict1 = {'Name': 'Runoob', 'Age': 7}

print("Age 键的值为 : %s" % dict1.setdefault('Age', None))
print("Sex 键的值为 : %s" % dict1.setdefault('Sex', None))
print("新字典为：", dict1)
