# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 集合
        集合内置方法
            Python Set isdisjoint()方法
                描述：
                    isdisjoint()方法用于判断两个集合是否包含相同的元素，如果没有返回True，否则返回False。
                语法：
                    set.isdisjoint(set)
                    参数：
                        set -- 必需，要比较的集合
                返回值：
                    返回布尔值，如果不包含返回True，否则返回False。
"""
if __name__ == "__main__":
    x = {"apple", "banana", "cherry"}
    y = {"google", "runoob", "apple"}

    z = x.isdisjoint(y)

    print(z)
