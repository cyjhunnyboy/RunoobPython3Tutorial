# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字典
        直接赋值、浅拷贝和深度拷贝解析
            1、直接赋值：其实就是对象的引用（别名）。
            2、浅拷贝（copy）：拷贝父对象，不会拷贝对象的内部的子对象。
            3、深拷贝（deepcopy）：copy模块的deepcopy方法，完全拷贝了父对象及其子对象。
"""
if __name__ == "__main__":
    #字典浅拷贝实例
    dict_1 = {"user": "runoob", "num": [1, 2, 3]}

    dict_2 = dict_1.copy()

    print(dict_1)
    print(dict_2)

    dict_1["user"] = "root"
    dict_1["num"].append(4)

    print(dict_1)
    print(dict_2)
    print("dict_1的id值是：", id(dict_1))
    print("dict_2的id值是：", id(dict_2))
    print("dict_1['num']的id值是：", id(dict_1["num"]))
    print("dict_2['num']的id值是：", id(dict_2["num"]))
