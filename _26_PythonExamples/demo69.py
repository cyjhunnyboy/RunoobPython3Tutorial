# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 判断元素是否在列表中存在
    定义一个列表，并判断元素是否在列表中。
'''
if __name__ == "__main__":
    test_list = [1, 6, 3, 5, 3, 4]

    print("查看4是否在列表中(使用循环)：")
    for i in test_list:
        if (i == 4):
            print("存在")

    print("查看4是否在列表中(使用in关键字)：")
    if (4 in test_list):
        print("存在")
