# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 最大公约数算法
'''


def hcf(x, y):
    """该函数返回两个数的最大公约数"""

    # 获取最小值
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i

    return hcf


if __name__ == "__main__":
    # 用户输入两个数字
    num1 = int(input("输入第一个数字： "))
    num2 = int(input("输入第二个数字："))

    # 两个数的最大公约数
    divisor = hcf(num1, num2)

    print("{0}和{1}的最大公约数为：{2}".format(num1, num2, divisor))
