# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字典
        字典内置方法
            Python3 字典items()方法
                描述：
                    Python字典items()方法以列表返回可遍历的(键, 值)元组数组。
                    Python字典items()方法以列表返回视图对象，是一个可遍历的key/value对。
                    dict.keys()、dict.values()和dict.items()返回的都是视图对象(view objects)。
                        提供了字典实体的动态视图，这就意味着字典改变，视图也会跟着变化。
                    视图对象不是列表，不支持索引，可以使用list()来转换为列表。
                    我们不能对视图对象进行任何的修改，因为字典的视图对象都是只读的。
                语法：
                    dict.items()
                    参数
                        NA。
                返回值：
                    返回可遍历的(键, 值)元组数组
                    返回可视图对象。
"""
if __name__ == "__main__":
    dict_a = {"Name": "Runoob", "Age": 7}

    print("Value： %s" % dict_a.items())

    # 遍历例子
    for key, value in dict_a.items():
        print(key, ":\t", value)

    # 将字典的key和value组成一个新的列表
    d = {1: "a", 2: "b", 3: "c"}
    result = []
    for k, v in d.items():
        result.append(k)
        result.append(v)
    print(result)