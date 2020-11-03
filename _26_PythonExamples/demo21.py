# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 质数判断
    一个大于1的自然数，除了1和它本身外，不能被其他自然数（质数）整除（2, 3, 5, 7等），
    换句话说就是该数除了1和它本身以外不再有其他的因数
'''


def prime(num):
    """用于检测用户输入的数字是否为质数"""

    # 质数大于1
    if num > 1:
        # 查看因子
        for i in range(2, num):
            if (num % i) == 0:
                print("{0}不是质数".format(num))
                print("{0}乘以{1}是{2}".format(i, num // i, num))
                break
            else:
                print("{0}是质数".format(num))
    # 如果输入的数字小于或等于1，不是质数
    else:
        print("{0}不是质数".format(num))


if __name__ == "__main__":
    # 用户输入数字
    num = int(input("请输入一个数字："))
    # 调用判断质数的方法
    prime(num)
