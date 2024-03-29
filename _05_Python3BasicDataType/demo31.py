# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python数据类型转换
        Python set()函数
            描述：
                set()函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等
            语法：
                class set([iterable])
                参数：
                    iterable -- 可迭代对象对象
            返回值：
                返回新的集合对象
"""
if __name__ == "__main__":
    x = set("runoob")
    y = set("google")
    # 重复的被删除
    print(x, y)
    # 交集
    print(x & y)
    # 并集
    print(x | y)
    # 差集
    print(x - y)
