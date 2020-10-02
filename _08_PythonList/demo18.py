# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
Python3 List remove()方法
描述
remove() 函数用于移除列表中某个值的第一个匹配项。

语法
remove()方法语法：

list.remove(obj)
参数
obj -- 列表中要移除的对象。
返回值
该方法没有返回值但是会移除两种中的某个值的第一个匹配项。
"""
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list1.remove('Taobao')
print("列表现在为 : ", list1)
list1.remove('Baidu')
print("列表现在为 : ", list1)
