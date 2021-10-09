# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 列表
        嵌套列表
            使用嵌套列表即在列表里创建其它列表
"""
if __name__ == "__main__":
    a = ['a', 'b', 'c']
    n = [1, 2, 3]
    x = [a, n]
    print(x)
    print(x[0])
    print(x[0][1])
