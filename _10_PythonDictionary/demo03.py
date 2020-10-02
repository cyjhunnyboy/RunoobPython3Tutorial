# -*- coding: UTF-8 -*-
# author: chenyongjun
"""
修改字典
向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对
"""
dict_c = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
dict_c['Age'] = 8  # 更新 Age
dict_c['School'] = "菜鸟教程"  # 添加信息
print("dict['Age']: ", dict_c['Age'])
print("dict['School']: ", dict_c['School'])
