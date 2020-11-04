# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 阿姆斯特朗数
    如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。例如1^3 + 5^3 + 3^3 = 153。
    1000以内的阿姆斯特朗数：1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。
'''


def narcissistic(num):
    """检测用户输入的数字是否为阿姆斯特朗数"""

    # 初始化变量 sum
    sum = 0
    # 指数
    n = len(str(num))

    # 检测
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        temp //= 10

    # 输出结果
    if num == sum:
        print("{0}是阿姆斯特朗数".format(num))
    else:
        print("{0}不是阿姆斯特朗数".format(num))


if __name__ == "__main__":
    # 获取用户输入的数字
    num = int(input("请输入一个数字："))

    # 检测用户输入的数字是否为阿姆斯特朗数
    narcissistic(num)
