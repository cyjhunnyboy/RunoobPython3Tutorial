# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python list 常用操作
    9、list 的映射解析
'''
if __name__ == "__main__":
    li1 = [1, 9, 8, 4]
    print(li1)

    li2 = [elem * 2 for elem in li1]
    print(li2)
    print(li1)
