# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 元组
        删除元组
            元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
"""
if __name__ == "__main__":
    tuple_1 = ("Google", "Runoob", 1997, 2000)
    print(tuple_1)

    del tuple_1
    # NameError: name 'tuple_1' is not defined
    print("删除后的元组tuple_1：", tuple_1)
