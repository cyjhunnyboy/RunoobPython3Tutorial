# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 最小公倍数算法
'''


def lcm(x, y):
    """该函数返回两个数的最小公倍数"""

    #  获取最大的数
    if x > y:
        greater = x
    else:
        greater = y

    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm


if __name__ == "__main__":
    # 获取用户输入
    num1 = int(input("输入第一个数字: "))
    num2 = int(input("输入第二个数字: "))

    # 两个数的最小公倍数
    multiple = lcm(num1, num2)

    print("{0}和{1}的最小公倍数为：{2}".format(num1, num2, multiple))
