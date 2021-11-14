# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 集合
        集合内置方法
            Python Set intersection()方法
                描述：
                    intersection()方法用于返回两个或更多集合中都包含的元素，即交集.
                语法：
                    set.intersection(set1, set2 ... etc)
                    参数：
                        set1 -- 必需，要查找相同元素的集合
                        set2 -- 可选，其他要查找相同元素的集合，可以多个，多个使用逗号 , 隔开
                返回值：
                    返回一个新集合
"""
if __name__ == "__main__":
    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}

    print("执行intersection()方法前集合x为：", x)
    print("执行intersection()方法前集合y为：", y)
    # 返回一个新集合，该集合的元素既包含在集合x又包含在集合y中
    z = x.intersection(y)
    print("执行intersection()方法后集合x为：", x)
    print("执行intersection()方法后集合y为：", y)
    print("集合x,y的交集为：", z)
