# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 交换变量
    通过用户输入两个变量，并相互交换
    不创建临时变量，用一个非常优雅的方式来交换变量：
    x,y = y,x
'''

if __name__ == "__main__":
    # 用户输入
    x = input("输入x值：")
    y = input("输入y值：")

    # 不使用临时变量
    x, y = y, x

    # 输出交互后x，y值
    print("交换后x的值为：{}".format(x))
    print("交换后y的值为：{}".format(y))
