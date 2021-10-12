# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 元组
        Python的元组与列表类似，不同之处在于元组的元素不能修改。
        元组使用小括号()，列表使用方括号[]。
        元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

        元组元素位于小括号中(...)
        tuple = ("Google", "Runoob", "Taobao")
        元组中元素使用逗号分割
"""
if __name__ == "__main__":
    tuple_1 = ("Google", "Runoob", 1997, 2000)
    print(type(tuple_1))
    print(tuple_1)

    tuple_2 = (1, 2, 3, 4, 5)
    print(type(tuple_2))
    print(tuple_2)

    # 不需要括号也可以
    tuple_3 = "a", "b", "c", "d"
    print(tuple_3)
    print(tuple_3)
