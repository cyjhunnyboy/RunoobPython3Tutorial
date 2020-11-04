# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python if 语句
    使用内嵌if语句判断数字是正数、负数或零
'''


def assure(num):
    """判断数字是正数、负数或零"""

    # 判断该数字是正数、负数或零
    if num >= 0:
        if num == 0:
            print("零")
        else:
            print("正数")
    else:
        print("负数")


if __name__ == "__main__":
    # 用户输入数字
    num = float(input("请输入一个数字："))

    # 判断该数字是正数、负数或零
    assure(num)
