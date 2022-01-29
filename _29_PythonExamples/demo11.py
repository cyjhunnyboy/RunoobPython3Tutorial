# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 交换变量
    通过用户输入两个变量，并相互交换
    创建临时变量temp，并将x的值存储在temp变量中，接着将y值赋给x，最后将temp赋值给y变量
'''

if __name__ == "__main__":
    # 用户输入
    x = input("输入x值：")
    y = input("输入y值：")

    # 创建临时变量，并交换
    temp = x
    x = y
    y = temp

    # 输出交互后x，y值
    print("交换后x的值为：{}".format(x))
    print("交换后y的值为：{}".format(y))
