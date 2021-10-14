# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 集合
        集合内置方法完整列表
            add()：为集合添加元素
            clear()：移除集合中的所有元素
            copy()：拷贝一个集合
            difference()：返回多个集合的差集
            difference_update()：移除集合中的元素，该元素在指定的集合也存在
            discard()：删除集合中指定的元素
            intersection()：返回集合的交集
            intersection_update()：返回集合的交集
            isdisjoint()：判断两个集合是否包含相同的元素，如果没有返回True，否则返回False
            issubset()：判断指定集合是否为该方法参数集合的子集
            issuperset()：判断该方法的参数集合是否为指定集合的子集
            isdisjoint()：判断两个集合是否包含相同的元素，如果没有返回True，否则返回False
            issubset(): 判断指定集合是否为该方法参数集合的子集
            issuperset(): 判断该方法的参数集合是否为指定集合的父集
            pop()：随机移除元素
            remove()：移除指定元素
            symmetric_difference()：返回两个集合中不重复的元素集合
            symmetric_difference_update()：移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中
            union()：返回两个集合的并集
            update()：给集合添加元素

            Python Set add()方法
                描述：
                    add()方法用于给集合添加元素，如果添加的元素在集合中已存在，则不执行任何操作
                语法：
                    set.add(elmnt)
                    参数：
                        elmnt -- 必需，要添加的元素
                返回值：
                    无
"""
if __name__ == "__main__":
    fruits = {"apple", "banana", "cherry"}
    print(fruits)

    # 通过add(x)方法添加元素
    fruits.add("orange")
    print(fruits)

    # 如果添加已存在的元素，则不执行添加操作
    fruits.add("apple")
    print(fruits)
