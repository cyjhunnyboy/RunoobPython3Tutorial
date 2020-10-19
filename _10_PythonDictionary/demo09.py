# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 字典copy()方法
描述：
    Python字典copy()函数返回一个字典的浅复制
语法：
    dict.copy()
    参数：
        NA
返回值：
    返回一个字典的浅复制
'''
if __name__ == "__main__":
    dict1 = {"Name": "Runoob", "Age": 7, "Class": "First"}
    dict2 = dict1.copy()
    print("原字典为：", dict1)
    print("新复制的字典为：", dict2)
    print("原字典id为：", id(dict1))
    print("新复制的字段id为：", id(dict2))
