# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字典
        字典内置方法
            Python3 字典keys()方法
                描述：
                    Python字典keys()方法以列表返回一个字典所有的键。
                    Python3字典keys()方法返回一个视图对象。
                    dict.keys()、dict.values()和dict.items()返回的都是视图对象(view objects)。
                        提供了字典实体的动态视图，这就意味着字典改变，视图也会跟着变化。
                    视图对象不是列表，不支持索引，可以使用list()来转换为列表。
                    我们不能对视图对象进行任何的修改，因为字典的视图对象都是只读的。
                    注意：Python2.x是直接返回列表
                语法：
                    dict.keys()
                    参数
                        NA。
                返回值：
                    返回一个字典所有的键。
                    返回一个视图对象。
"""
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
