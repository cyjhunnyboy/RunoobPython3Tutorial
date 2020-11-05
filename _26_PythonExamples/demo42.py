# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python list 常用操作
    2、list 负数索引
'''
if __name__ == "__main__":
    li = ["a", "b", "mpilgrim", "z", "example"]
    print(li)
    print("-----------")

    # 负数索引
    # 列表负数索引是从下标-1开始，到列表长度-len(list)
    print(li[-1])
    print(li[-3])
    print(li[-len(li)])
    print("-----------")

    # 列表切片
    print(li[1:3])
    print(li[1:-1])
    print(li[0:3])
