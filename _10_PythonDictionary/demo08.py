# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 字典clear()方法
    Python字典clear()函数用于删除字典内所有元素。
语法：
    dict.clear()
    参数：
        NA
返回值：
    该函数没有任何返回值
'''
if __name__ == "__main__":
    dict_a = {"Name": "Zara", "Age": 7}

    print("字典长度：%d" % len(dict_a))
    dict_a.clear()
    print("字典删除后长度：%d" % len(dict_a))
