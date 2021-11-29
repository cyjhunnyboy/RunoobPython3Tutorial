# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 集合
        集合内置方法
            Python Set symmetric_difference_update()方法
                描述：
                    symmetric_difference_update()方法移除当前集合中在另一个指定集合相同的元素，
                    并将另外一个指定集合中不同的元素插入到当前集合中。
                语法：
                    set.symmetric_difference_update(set)
                    参数：
                        set -- 要检测的集合
                返回值：
                    无
"""
if __name__ == "__main__":
    x = {"apple", "banana", "cherry"}
    y = {"google", "runoob", "apple"}

    # 移除当前集合中在另外一个指定集合相同的元素，
    # 并将另外一个指定集合中不同的元素插入到当前集合中
    x.symmetric_difference_update(y)

    print(x)
    print(y)
