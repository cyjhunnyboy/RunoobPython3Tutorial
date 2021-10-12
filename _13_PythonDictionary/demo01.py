# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字典
        字典是另一种可变容器模型，且可存储任意类型对象。
        字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号{}中
            格式如下所示:
            d = {key1 : value1, key2 : value2 }
        键必须是唯一的，但值则不必。
        值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
"""
if __name__ == "__main__":
    # 一个简单的字典实例
    tinydict = {"name": "runoob", "likes": 123, "url": "www.runoob.com"}
    print(tinydict)

    # 也可如此创建字典
    dict_1 = {"abc": 456}
    dict_2 = {"abc": 123, 98.6: 37}
    print(dict_1)
    print(dict_2)
