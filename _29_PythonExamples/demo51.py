# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python list 常用操作
    11、list 过滤
'''
if __name__ == "__main__":
    li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
    print(li)

    print([elem for elem in li if len(elem) > 1])
    print([elem for elem in li if elem != "b"])
    print([elem for elem in li if li.count(elem) == 1])
    print(li)
