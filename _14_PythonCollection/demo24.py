# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 集合
        集合内置方法
            Python Set symmetric_difference()方法
                描述：
                    symmetric_difference()方法返回两个集合中不重复的元素集合，即会移除两个集合中都存在的元素。
                语法：
                    set.symmetric_difference(set)
                    参数：
                        set -- 集合
                返回值：
                    返回一个新集合。
"""
if __name__ == "__main__":
    x = {"apple", "banana", "cherry"}
    y = {"google", "runoob", "apple"}

    # 返回两个集合中不重复的元素集合
    z = x.symmetric_difference(y)

    print(z)
