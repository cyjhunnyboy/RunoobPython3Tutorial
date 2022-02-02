# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数据结构
        集合
            集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
            可以用大括号({})创建集合。
            注意：如果要创建一个空集合，你必须用set()而不是{}；后者创建一个空的字典。
"""
if __name__ == "__main__":
    basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
    # 删除重复的元素
    print(basket)

    # 检测成员
    print("orange" in basket)
    print("crabgrass" in basket)

    # 以下演示了两个集合的操作
    a = set("abracadabra")
    b = set("alacazam")
    # a中唯一的字母
    print(a)
    # 差集，在a中的字母，但不在b中
    print(a - b)
    # 并集，在a或b中的字母
    print(a | b)
    # 交集，在a和b中都有的字母
    print(a & b)
    # 在a或b中的字母，但不同时在a和b中
    print(a ^ b)

    # 集合也支持推导式
    a = {x for x in "abracadabra" if x not in "abc"}
    print(a)
