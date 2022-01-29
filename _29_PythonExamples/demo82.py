# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 查找列表中最大元素
    定义一个数字列表，并查找列表中的最大元素。
    例如：
        输入 : list1 = [10, 20, 4]
        输出 : 20
'''
if __name__ == "__main__":
    list1 = [10, 20, 4, 45, 99]
    list1.sort()
    print("最大元素为：", list1[-1])

    print("==============")
    list2 = [10, 20, 1, 45, 99]
    print("最大元素为：", max(list2))
