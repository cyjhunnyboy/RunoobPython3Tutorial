# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 基本数据类型
        1、List（列表）
            与Python字符串不一样的是，列表中的元素是可以改变的
"""
if __name__ == "__main__":
    # 与Python字符串不一样的是，列表中的元素是可以改变的：
    a = [1, 2, 3, 4, 5, 6]
    a[0] = 9
    a[2:5] = [13, 14, 15]
    print(a)
    # 将对应的元素值设置为[]
    a[2:5] = []
    print(a)
