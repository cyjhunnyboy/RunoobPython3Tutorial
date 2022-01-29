# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 计算圆的面积
    圆的面积公式为：S = PI*r*r，公式中r为圆的半径
'''


def findArea(r):
    '''定义一个方法来计算圆的面积'''

    PI = 3.142
    return PI * r * r


if __name__ == "__main__":
    # 调用方法
    print("圆的面积为：%.6f" % findArea(5))
