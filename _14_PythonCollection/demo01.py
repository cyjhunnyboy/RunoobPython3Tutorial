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
"""
if __name__ == "__main__":
    basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
    # 这里演示的是去重功能
    print(basket)

    # 快速判断元素是否在集合内
    print("orange" in basket)
    print("crabgrass" in basket)

    # 下面展示两个集合间的运算
    a = set("abracadabra")
    b = set("alacazam")
    print(a)
    print(b)
    # 差集，集合a中包，集合b中不包含的含元素
    print(a - b)
    # 并集，集合a或b中包含的所有元素
    print(a | b)
    # 交集，集合a和b中都包含了的元素
    print(a & b)
    # 不同时包含于a和b的元素
    print(a ^ b)
