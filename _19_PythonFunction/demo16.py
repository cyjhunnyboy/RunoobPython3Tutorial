# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 函数
        return语句
            return [表达式]：语句用于退出函数，选择性地向调用方返回一个表达式。
                不带参数值的return语句返回None。之前的例子都没有示范如何返回数值
"""


# 可写函数说明
def sums(arg1, arg2):
    # 返回2个参数的和"
    total = arg1 + arg2
    print("函数内：", total)
    return total


if __name__ == "__main__":
    # 调用sum函数
    totals = sums(10, 20)
    print("函数外：", totals)
