# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 循环语句
        Python中的循环语句有for和while

        range()函数
            如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列
"""
if __name__ == "__main__":
    for i in range(5):
        print(i, end=" ")
    print("\n")

    # 也可以使用range指定区间的值
    for i in range(5, 9):
        print(i, end=" ")
    print("\n")

    # 也可以使range以指定数字开始并指定不同的增量
    # 甚至可以是负数，有时这也叫做'步长'
    for i in range(0, 10, 3):
        print(i, end=" ")
    print("\n")

    # 负数
    for i in range(-10, -100, -30):
        print(i, end=" ")
    print("\n")

    # 可以结合range()和len()函数以遍历一个序列的索引
    a = ["Google", "Baidu", "Runoob", "Taobao", "QQ"]
    for i in range(len(a)):
        print(i, a[i])
    print("\n")

    # 还可以使用range()函数来创建一个列表
    list_1 = list(range(5))
    print(list_1)
