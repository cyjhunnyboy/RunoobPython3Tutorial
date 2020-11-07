# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 计算列表元素之和
    定义一个数字列表，并计算列表元素之和。
    例如：
        输入: [12, 15, 3, 10] 输出: 40
'''

if __name__ == "__main__":
    total = 0

    list1 = [11, 5, 17, 18, 23]

    for ele in range(0, len(list1)):
        total = total + list1[ele]

    print("列表元素之和为：", total)
