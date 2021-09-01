# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 基本数据类型
        Dictionary（字典）
            另外，字典类型也有一些内置的函数，例如clear()、keys()、values()等。

            注意：
            1、字典是一种映射类型，它的元素是键值对。
            2、字典的关键字必须为不可变类型，且不能重复。
            3、创建空字典使用{}。
"""
if __name__ == "__main__":

    # 构造函数dict()可以直接从键值对序列中构建字典
    dict_b = dict([("Runoob", 1), ("Google", 2), ("Taobao", 3)])
    print(dict_b)

    dict_c = {x: x ** 2 for x in (2, 4, 6)}
    print(dict_c)

    dict_d = dict(Runoob=1, Google=2, Taobao=3)
    print(dict_d)
