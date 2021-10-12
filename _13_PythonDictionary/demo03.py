# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字典
        修改字典
            向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对
"""
if __name__ == "__main__":
    dict_1 = {"Name": "Runoob", "Age": 7, "Class": "First"}

    # 更新 Age
    dict_1["Age"] = 8

    # 添加信息
    dict_1["School"] = "菜鸟教程"

    print("dict_1['Age']: ", dict_1["Age"])
    print("dict_1['School']: ", dict_1["School"])
