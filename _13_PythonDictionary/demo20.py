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
    dishes = {"eggs": 2, "sausage": 1, "bacon": 1, "spam": 500}

    keys = dishes.keys()
    print(keys)
    values = dishes.values()
    print(values)
    print("================")

    # 迭代
    n = 0
    for val in values:
        n += val
    print(n)
    print("================")

    # keys和values以相同顺序（插入顺序）进行迭代
    # 使用list()转换为列表
    print(list(keys))
    print(list(values))
    print("================")

    # 视图对象是动态的，受字典变化的影响，以下删除了字典的key，视图对象转为列表后也跟着变化
    del dishes["eggs"]
    del dishes["sausage"]
    print(list(keys))
