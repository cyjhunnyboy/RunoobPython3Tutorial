# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 字典items()方法
描述：
    Python字典items()方法以列表返回可遍历的(键, 值)元组数组。
语法：
    dict.items()
    参数
        NA。
返回值：
    返回可遍历的(键, 值)元组数组
'''
if __name__ == "__main__":
    dict_a = {"Name": "Runoob", "Age": 7}

    print("Value： %s" % dict_a.items())

    for key, value in dict_a.items():
        print(key, ":\t", value)
