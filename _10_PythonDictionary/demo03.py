# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 字典
    修改字典，向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对
'''
if __name__ == "__main__":
    dict_c = {"Name": "Runoob", "Age": 7, "Class": "First"}
    # 更新 Age
    dict_c["Age"] = 8
    # 添加信息
    dict_c["School"] = "菜鸟教程"

    print("dict['Age']: ", dict_c["Age"])
    print("dict['School']: ", dict_c["School"])
