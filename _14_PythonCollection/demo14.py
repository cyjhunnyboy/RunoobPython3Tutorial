# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 集合
        集合内置方法
            Python Set difference()方法
                描述：
                    difference()方法用于返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中
                语法：
                    set.difference(set)
                    参数：
                        set -- 必需，用于计算差集的集合
                返回值：
                    返回一个新的集合
"""
if __name__ == "__main__":
    fruits_1 = {"apple", "banana", "cherry"}
    fruits_2 = {"google", "microsoft", "apple"}

    # 返回一个集合，元素包含在集合x，但不在集合y。
    fruits_3 = fruits_1.difference(fruits_2)

    print("集合fruits_1为：", fruits_1)
    print("集合fruits_2为：", fruits_2)
    print("集合fruits_3为：", fruits_3)
