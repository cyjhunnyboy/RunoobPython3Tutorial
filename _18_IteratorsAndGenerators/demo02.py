# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 迭代器与生成器
        迭代器
            迭代是Python最强大的功能之一，是访问集合元素的一种方式。
            迭代器是一个可以记住遍历的位置的对象。
            迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
            迭代器有两个基本的方法：iter()和next()。
            字符串，列表或元组对象都可用于创建迭代器
"""
if __name__ == "__main__":
    num_list = [1, 2, 3, 4]
    # 创建迭代器对象
    list_iter = iter(num_list)
    # 迭代器对象可以使用常规for语句进行遍历
    for x in list_iter:
        print(x, end=" ")
