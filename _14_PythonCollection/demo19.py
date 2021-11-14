# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 集合
        集合内置方法
            Python Set intersection_update()方法
                描述：
                    intersection_update()方法用于获取两个或更多集合中都重叠的元素，即计算交集。
                    intersection_update()方法不同于intersection()方法，因为intersection()方法是返回一个新的集合，
                    而intersection_update()方法是在原始的集合上移除不重叠的元素。
                语法：
                    set.intersection_update(set1, set2 ... etc)
                    参数：
                        set1 -- 必需，要查找相同元素的集合
                        set2 -- 可选，其他要查找相同元素的集合，可以多个，多个使用逗号 , 隔开
                返回值：
                    无
"""
if __name__ == "__main__":
    # y集合不包含banana和cherry，被移除
    x = {"apple", "banana", "cherry"}
    y = {"google", "runoob", "apple"}

    print("执行intersection_update()方法前x集合为：", x)
    print("执行intersection_update()方法前y集合为：", y)
    # 移除x集合中不存在于y集合中的元素
    x.intersection_update(y)
    print("执行intersection_update()方法后x集合为：", x)
    print("执行intersection_update()方法后y集合为：", y)
