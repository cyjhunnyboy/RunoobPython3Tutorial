# -*- coding: UTF-8 -*-
# author: chen_yong_jun

"""
Python3 List extend()方法
描述
extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。

语法
extend()方法语法：

list.extend(seq)
参数
seq -- 元素列表。
返回值
该方法没有返回值，但会在已存在的列表中添加新的列表内容。
"""
list1 = ['Google', 'Runoob', 'Taobao']
list2 = list(range(5))  # 创建 0-4 的列表
list1.extend(list2)  # 扩展列表
print("扩展后的列表：", list1)
