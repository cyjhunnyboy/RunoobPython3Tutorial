# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 运算符
        Python成员运算符
            除了以上的一些运算符之外，Python还支持成员运算符，测试实例中包含了一系列的成员，包括字符串，列表或元组。
            in：如果在指定的序列中找到值返回True，否则返回False。实例：x在y序列中, 如果x在y序列中返回True
            not in：如果在指定的序列中没有找到值返回True，否则返回False。实例：x不在y序列中, 如果x不在y序列中返回True
"""
if __name__ == "__main__":
    a = 10
    b = 20
    tiny_list = [1, 2, 3, 4, 5]

    if a in tiny_list:
        print("1-变量a在给定的列表中tiny_list中")
    else:
        print("1-变量a不在给定的列表中tiny_list中")

    if b not in tiny_list:
        print("2-变量b不在给定的列表中tiny_list中")
    else:
        print("2-变量b在给定的列表中tiny_list中")

    # 修改变量a的值
    a = 2
    if a in tiny_list:
        print("3-变量a在给定的列表中tiny_list中")
    else:
        print("3-变量a不在给定的列表中tiny_list中")
