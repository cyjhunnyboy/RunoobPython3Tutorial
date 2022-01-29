# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python list 常用操作
    4、list 搜索
'''
if __name__ == "__main__":
    li = ["a", "b", "mpilgrim", "z", "example", "new", "two", "elements"]
    print(li)

    # list搜索
    print(li.index("example"))
    print(li.index("new"))

    print("c" in li)

    # list.index(x) 查找x是否在列表中，若存在，则返回索引位置
    # 若查找元素不存在，则报ValueError错误
    # ValueError: 'c' is not in list
    print(li.index("c"))
