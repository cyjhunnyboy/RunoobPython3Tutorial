# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 字典values()方法
描述：
    Python字典values()方法返回一个迭代器，可以使用list()来转换为列表，列表为字典中的所有值。
语法：
    dict.values()
    参数
        NA。
返回值：
    返回迭代器。
'''
if __name__ == "__main__":
    dict_a = {"Name": "Zara", "Age": 7, "Sex": "female"}

    print("字典所有值为：", list(dict_a.values()))

    # 遍历字典所有值转换后的列表
    for value in list(dict_a.values()):
        print(value, end=" ")
