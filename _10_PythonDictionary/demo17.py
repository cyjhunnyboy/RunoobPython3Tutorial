# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
Python3 字典 update() 方法
描述
Python 字典 update() 函数把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里。

语法
update() 方法语法：

dict.update(dict2)
参数
dict2 -- 添加到指定字典dict里的字典。
返回值
该方法没有任何返回值。
"""

dict1 = {'Name': 'Runoob', 'Age': 7}
dict2 = {'Sex': 'female'}

dict1.update(dict2)
print("更新字典 dict1 : ", dict1)
