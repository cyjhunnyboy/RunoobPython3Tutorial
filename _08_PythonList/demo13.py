# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
Python3 List count()方法
描述
count() 方法用于统计某个元素在列表中出现的次数。

语法
count()方法语法：

list.count(obj)
参数
obj -- 列表中统计的对象。
返回值
返回元素在列表中出现的次数。
"""

aList = [123, 'Google', 'Runoob', 'Taobao', 123]

print("123 元素个数 : ", aList.count(123))
print("Runoob 元素个数 : ", aList.count('Runoob'))
