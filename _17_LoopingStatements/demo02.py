# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 循环语句
        Python中的循环语句有for和while
        while循环
            Python中while语句的一般形式：
            while 判断条件(condition)：
                执行语句(statements)……

        同样需要注意冒号和缩进。另外，在Python中没有do..while循环
"""
if __name__ == "__main__":
    # 计算1到100的总和
    n = 100
    sums = 0
    counter = 1
    while counter <= n:
        sums = sums + counter
        counter += 1

    print("1到%d之和为：%d" % (n, sums))
