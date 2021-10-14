# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 集合
        集合内置方法
            Python Set copy()方法
            描述：
                copy()方法用于拷贝一个集合
            语法：
                set.copy()
                参数：
                    无
            返回值：
                无
"""
if __name__ == "__main__":
    fruits = {"apple", "banana", "cherry"}

    # 拷贝一个集合
    copy = fruits.copy()

    print("集合fruits为：", fruits)
    print("集合fruits的id值为：", id(fruits))
    print("集合copy为：", copy)
    print("集合copy的id值为：", id(copy))
