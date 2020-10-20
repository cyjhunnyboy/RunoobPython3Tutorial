# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 字典keys()方法
描述：
    Python字典keys()方法以列表返回一个字典所有的键。
语法：
    dict.keys()
    参数
        NA。
返回值：
    返回一个字典所有的键。
'''
if __name__ == "__main__":
    dict_a = {"Name": "Runoob", "Age": 7}
    print("字典所有的键为：%s" % dict_a.keys())
    print("字典所有的键为：%s" % list(dict_a.keys()))

    print("===================")

    # 遍历字典所有的键，并获取键-值
    for key in dict_a.keys():
        print(key, ":\t", dict_a[key])

    print("===================")

    # 获取字典所有的键并把键转换为列表，遍历列表获取键-值
    for key in list(dict_a.keys()):
        print(key, ":\t", dict_a[key])
