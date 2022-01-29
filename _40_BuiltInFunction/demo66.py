# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python map() 函数
描述：
    map() 会根据提供的函数对指定序列做映射
    第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表
语法：
    map(function, iterable, ...)
    参数：
        function -- 函数
        iterable -- 一个或多个序列
返回值：
    Python 2.x 返回列表
    Python 3.x 返回迭代器
'''


# 计算平方数
def square(x):
    return x ** 2


if __name__ == "__main__":
    # 计算列表各个元素的平方
    square_1 = map(square, [1, 2, 3, 4, 5])
    for s in square_1:
        print(s)
    print("==========")

    # 使用 lambda 匿名函数
    square_2 = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
    for s in square_2:
        print(s)
    print("==========")

    # 提供了两个列表，对相同位置的列表数据进行相加
    sum_1 = map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
    for s in sum_1:
        print(s)
