# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 阶乘实例
    整数的阶乘（英语：factorial）是所有小于及等于该数的正整数的积，0的阶乘为1。即：n!=1×2×3×...×n。
'''


def factorial(num):
    """计算阶乘"""

    # 初始值为1
    factorial = 1

    # 查看数字是负数，0或正数
    if num < 0:
        print("抱歉，负数没有阶乘！")
    elif num == 0:
        print("0的阶乘为1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print("{0}的阶乘为{1}".format(num, factorial))


if __name__ == "__main__":
    # 获取用户输入的数字
    num = int(input("请输入一个数字: "))
    # 调用计算阶乘的方法
    factorial(num)
