# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 列表
        删除列表元素
            可以使用del语句来删除列表的的元素
"""
if __name__ == "__main__":
    list_b = ["Google", "Runoob", 1997, 2000]
    print("原始列表：", list_b)
    del list_b[2]
    print("删除第三个元素：", list_b)
