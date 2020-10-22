# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 数据结构
del 语句
    使用del语句可以从一个列表中依索引而不是值来删除一个元素。
    这与使用pop()返回一个值不同。可以用del语句从列表中删除一个切割，
    或清空整个列表（我们以前介绍的方法是给该切割赋一个空列表）
'''
if __name__ == "__main__":
    a = [-1, 1, 66.25, 333, 333, 1234.5]

    del a[0]
    print(a)

    del a[2:4]
    print(a)

    del a[:]
    print(a)

    # del删除实体变量
    del a
