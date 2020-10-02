# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
集合
集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。

可以用大括号({})创建集合。注意：如果要创建一个空集合，你必须用 set() 而不是 {} ；后者创建一个空的字典，下一节我们会介绍这个数据结构。

以下是一个简单的演示
"""
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)   # 删除重复的
print('orange' in basket)
print('crabgrass' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)    # a - b
print(a | b)    # 在 a 或 b 中的字母
print(a & b)    # 在 a 和 b 中都有的字母
print(a ^ b)    # 在 a 或 b 中的字母，但不同时在 a 和 b 中

# 集合也支持推导式
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
