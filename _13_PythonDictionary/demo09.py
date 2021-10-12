# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字典
        字典内置方法
            Python3 字典copy()方法
                描述：
                    Python字典copy()函数返回一个字典的浅复制
                语法：
                    dict.copy()
                    参数：
                        NA
                返回值：
                    返回一个字典的浅复制
"""
if __name__ == "__main__":
    dict_1 = {"Name": "Runoob", "Age": 7, "Class": "First"}

    dict_2 = dict_1.copy()
    print("原字典为：", dict_1)
    print("新复制的字典为：", dict_2)

    print("原字典id为：", id(dict_1))
    print("新复制的字段id为：", id(dict_2))
