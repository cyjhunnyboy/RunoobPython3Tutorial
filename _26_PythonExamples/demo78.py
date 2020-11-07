# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 计算列表元素之和
    定义一个数字列表，并计算列表元素之和。
    例如：
        输入: [12, 15, 3, 10] 输出: 40
'''

if __name__ == "__main__":
    #  使用while()循环
    total = 0
    ele = 0

    list1 = [11, 5, 17, 18, 23]

    while (ele < len(list1)):
        total = total + list1[ele]
        ele += 1

    print("列表元素之和为：", total)
