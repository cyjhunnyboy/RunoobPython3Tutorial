# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 集合
        集合内置方法
            Python Set clear()方法
                描述：
                    clear()方法用于移除集合中的所有元素
                语法：
                    set.clear()
                    参数：
                        无
                返回值：
                    无
"""
if __name__ == "__main__":
    fruits = {"apple", "banana", "cherry"}
    print(fruits)

    # 移除fruits集合中的所有元素
    fruits.clear()
    print(fruits)
