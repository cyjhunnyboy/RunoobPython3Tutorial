# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 计算n个自然数的立方和
    计算公式 1*1*1 + 2*2*2 + 3*3*3 + 4*4*4 + …….+ n*n*n
    实现要求：
        输入：n = 5
        输出：225
        公式：1*1*1 + 2*2*2 + 3*3*3 + 4*4*4 + 5*5*5 = 225
        .....
'''


def sumOfSeries(n):
    """定义立方和的函数"""

    sum = 0
    for i in range(1, n + 1):
        sum += i * i * i

    return sum


if __name__ == "__main__":
    num = int(input("请输入一个正数："))
    print("{0}的立方和结果是：{1}".format(num, sumOfSeries(num)))
