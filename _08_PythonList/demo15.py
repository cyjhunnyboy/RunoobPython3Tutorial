# -*- coding: UTF-8 -*-
# author: chen_yong_jun

"""
Python3 List index()方法

描述
index() 函数用于从列表中找出某个值第一个匹配项的索引位置。

语法
index()方法语法：

list.index(obj)
参数
obj -- 查找的对象。
返回值
该方法返回查找对象的索引位置，如果没有找到对象则抛出异常。
"""

list1 = ['Google', 'Runoob', 'Taobao']
print('Runoob 索引值为', list1.index('Runoob'))
print('Taobao 索引值为', list1.index('Taobao'))
