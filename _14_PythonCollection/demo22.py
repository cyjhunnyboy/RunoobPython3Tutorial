# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 集合
        集合内置方法
            Python Set pop()方法
                描述：
                    pop()方法用于随机移除一个元素。
                语法：
                    set.pop()
                    参数：
                        无。
                返回值：
                    返回移除的元素。
"""
if __name__ == "__main__":
    fruits = {"apple", "banana", "cherry"}

    x = fruits.pop()

    print("随机移除的元素是：", x)
    print("输出fruits集合为：", fruits)
