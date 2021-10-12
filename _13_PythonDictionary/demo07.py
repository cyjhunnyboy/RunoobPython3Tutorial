# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字典
        字典内置函数&方法
            Python字典包含了以下内置函数
                len(dict)：计算字典元素个数，即键的总数
                str(dict)：输出字典，以可打印的字符串表示
                type(variable)：返回输入的变量类型，如果变量是字典就返回字典类型
"""
if __name__ == "__main__":
    # len(dict)计算字典元素个数，即键的总数。
    dict_a = {"Name": "Runoob", "Age": 7, "Class": "First"}
    print("dict_a字段长度是：", len(dict_a))

    # str(dict)输出字典，以可打印的字符串表示。
    print("dict_a字典是：", str(dict_a))

    # type(variable)返回输入的变量类型，如果变量是字典就返回字典类型。
    print("dict_a字典类型是：", type(dict_a))
