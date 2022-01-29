# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python list 常用操作
    5、list 删除元素
'''
if __name__ == "__main__":
    li = ["a", "b", "new", "mpilgrim", "z", "example", "new", "two", "elements"]
    print(li)

    # list.remove(x)删除元素
    li.remove("z")
    print(li)

    # remove(x)删除x首次出现的一个值
    li.remove("new")
    print(li)

    # list.pop()删除最后一个元素，并返回删除元素的值
    element = li.pop()
    print(element)
    print(li)

    # list.pop(index)根据索引x删除对应元素，并返回该元素值
    element = li.pop(0)
    print(element)
    print(li)

    # remove(x)若x不存在，则报ValueError错误
    # ValueError: list.remove(x): x not in list
    li.remove("c")
