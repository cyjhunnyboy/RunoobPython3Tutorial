# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 判断元素是否在列表中存在
    定义一个列表，并判断元素是否在列表中。
'''
if __name__ == "__main__":
    # 初始化列表
    test_list_set = [1, 6, 3, 5, 3, 4]
    test_list_bisect = [1, 6, 3, 5, 3, 4]

    print("查看4是否在列表中(使用set()+in)：")
    test_list_set = set(test_list_set)
    if 4 in test_list_set:
        print("存在")

    print("查看4是否在列表中(使用count())：")
    if test_list_bisect.count(4) > 0:
        print("存在")
