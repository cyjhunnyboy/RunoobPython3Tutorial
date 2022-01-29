# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 判断奇数偶数
    判断一个数字是否为奇数或偶数，如果是偶数除以2余数为0，如果余数为1则为奇数。
'''


def assure(num):
    """判断一个数字是否为奇数或偶数"""

    yushu = num % 2
    if yushu >= 0:
        if yushu == 0:
            print("{0}是偶数".format(num))
        else:
            print("{0}是奇数".format(num))


if __name__ == "__main__":
    num = int(input("请输入一个数字："))

    # 判断一个数字是否为奇数或偶数
    assure(num)
