# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 计算三角形的面积
    通过用户输入三角形三边长度，并计算三角形的面积
'''


def findArea(a, b, c):
    """通过三边长计算三角形面积"""

    # 计算半周长
    s = (a + b + c) / 2

    # 计算面积
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    return area


if __name__ == "__main__":
    a = float(input("输入三角形第一边长："))
    b = float(input("输入三角形第二边长："))
    c = float(input("输入三角形第三边长："))

    print("三角形面积为：%0.2f" % findArea(a, b, c))
