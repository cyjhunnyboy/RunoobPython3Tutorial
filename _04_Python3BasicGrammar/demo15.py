# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
    Python3 基础语法
        1、Print输出
            print默认输出是换行的，如果要实现不换行需要在变量末尾加上end=""：
'''
if __name__ == "__main__":
    x = "a"
    y = "b"
    # 换行输出
    print(x)
    print(y)

    print('---------')

    # 不换行输出
    print(x, end=" ")
    print(y, end=" ")
    print()
