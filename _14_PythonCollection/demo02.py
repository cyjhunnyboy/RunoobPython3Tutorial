# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 集合
        集合（set）是一个无序不重复元素的序列。
        可以使用大括号{}或者set()函数创建集合。

        注意：创建一个空集合必须用set()而不是{}，因为{}是用来创建一个空字典

        创建集合格式：
            parame = {value01,value02,...}
            或者
            set(value)

        类似列表推导式，同样集合支持集合推导式(Set comprehension)
"""
if __name__ == "__main__":
    a = {x for x in "abracadabra" if x not in "abc"}
    print(a)
