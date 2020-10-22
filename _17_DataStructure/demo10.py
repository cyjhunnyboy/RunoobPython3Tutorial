# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 数据结构
字典
    另一个非常有用的Python内建数据类型是字典。
    序列是以连续的整数为索引，与此不同的是，字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值。
    理解字典的最佳方式是把它看做无序的键=>值对集合。在同一个字典之内，关键字必须是互不相同。
    一对大括号创建一个空的字典：{}

    遍历技巧
        在字典中遍历时，关键字和对应的值可以使用items()方法同时解读出来
'''
if __name__ == "__main__":
    knights = {"gallahad": "the pure", "robin": "the brave"}
    for k, v in knights.items():
        print(k, v)

    print("=====================")

    # 在序列中遍历时，索引位置和对应值可以使用enumerate()函数同时得到
    dict_1 = ["tic", "tac", "toe"]
    for i, v in enumerate(dict_1):
        print(i, v)

    print("=====================")

    # 同时遍历两个或更多的序列，可以使用zip()组合
    questions = ["name", "quest", "favorite color"]
    answers = ["lancelot", "the holy grail", "blue"]
    for q, a in zip(questions, answers):
        print("What is your {0}?  It is {1}.".format(q, a))

    print("=====================")

    # 要反向遍历一个序列，首先指定这个序列，然后调用reversed()函数
    for i in reversed(range(1, 10, 2)):
        print(i)

    print("=====================")

    # 要按顺序遍历一个序列，使用sorted()函数返回一个已排序的序列，并不修改原值
    basket = ["apple", "orange", "apple", "pear", "orange", "banana"]
    for f in sorted(set(basket)):
        print(f)
