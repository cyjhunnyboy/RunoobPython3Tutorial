# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python list 常用操作
    3、list 增加元素
'''
if __name__ == "__main__":
    li = ["a", "b", "mpilgrim", "z", "example"]
    print(li)
    print("---------------")

    li.append("new")
    print(li)
    print("---------------")

    li.insert(2, "apple")
    print(li)
    print("---------------")

    li.extend(["two", "elements"])
    print(li)
