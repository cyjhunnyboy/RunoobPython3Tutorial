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
    x = {"a", "b", "c"}
    y = {"c", "d", "e"}
    z = {"f", "g", "c"}

    print("执行intersection()方法前集合x为：", x)
    print("执行intersection()方法前集合y为：", y)
    print("执行intersection()方法前集合z为：", z)
    # 计算多个集合的交集
    result = x.intersection(y, z)
    print("执行intersection()方法后集合x为：", x)
    print("执行intersection()方法后集合y为：", y)
    print("执行intersection()方法后集合z为：", z)
    print("集合x,y,z的交集为：", result)
