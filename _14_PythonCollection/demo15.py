# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 集合
        集合内置方法
            Python Set difference_update()方法
                描述：
                    difference_update() 方法用于移除两个集合中都存在的元素。
                    difference_update() 方法与difference()方法的区别在于difference()方法返回一个移除相同元素的新集合，
                    而difference_update()方法是直接在原来的集合中移除元素，没有返回值。
                语法：
                    set.difference_update(set)
                    参数：
                        set -- 必需，用于计算差集的集合
                返回值：
                    无
"""
if __name__ == "__main__":
    fruits_1 = {"apple", "banana", "cherry"}
    fruits_2 = {"google", "microsoft", "apple"}

    # 移除两个集合都包含的元素
    fruits_1.difference_update(fruits_2)

    print("集合fruits_1为：", fruits_1)
    print("集合fruits_2为：", fruits_2)
