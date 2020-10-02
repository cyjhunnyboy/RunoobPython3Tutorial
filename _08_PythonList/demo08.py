# -*- coding: UTF-8 -*-
# author: chenyongjun
"""
Python列表函数&方法
Python包含以下函数:
序号	    函数
1	    len(list) 列表元素个数
2	    max(list) 返回列表元素最大值
3	    min(list) 返回列表元素最小值
4	    list(seq) 将元组转换为列表
"""
"""
Python3 List len()方法
描述
len() 方法返回列表元素个数。

语法
len()方法语法：

len(list)
参数
list -- 要计算元素个数的列表。
返回值
返回列表元素个数。
"""

list1 = ['Google', 'Runoob', 'Taobao']
print(len(list1))
list2 = list(range(5))  # 创建一个 0-4 的列表
print(len(list2))
