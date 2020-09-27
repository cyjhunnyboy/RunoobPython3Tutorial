# -*- coding: UTF-8 -*-
# author: chen_yong_jun
"""
Python3 shuffle() 函数
描述：shuffle() 方法将序列的所有元素随机排序
语法：
import random
random.shuffle(lst)
注意：shuffle()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。
参数：lst -- 列表
返回值：返回 None
"""
import random

list1 = [20, 16, 10, 5]
random.shuffle(list1)
print("随机排序列表 : ", list1)

random.shuffle(list1)
print("随机排序列表 : ", list1)
