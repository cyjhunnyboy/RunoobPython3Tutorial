# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
修改元组
元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
"""
tup_b = (12, 34.56)
tup_c = ('abc', 'xyz')
# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup_d = tup_b + tup_c
print(tup_d)
