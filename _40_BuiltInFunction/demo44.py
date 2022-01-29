# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 tuple 函数
描述：
    tuple 函数将可迭代系列（如列表）转换为元组
语法：
    tuple( iterable )
    参数：
        iterable -- 要转换为元组的可迭代序列
返回值：
    返回元组
'''
if __name__ == "__main__":
    list1 = ["Google", "Taobao", "Runoob", "Baidu"]
    tuple1 = tuple(list1)
    print(tuple1)

    # tuple() 可以将字符串，列表，字典，集合转化为元组
    a = "www"
    b = tuple(a)
    print(b)

    # # 将字段转换为元组时，只保留键！
    a = {"www": 123, "aaa": 234}
    b = tuple(a)
    print(b)

    a = set("abcd")
    print(a)
    b = tuple(a)
    print(b)
