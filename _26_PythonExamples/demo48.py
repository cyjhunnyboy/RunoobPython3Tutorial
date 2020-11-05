# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python list 常用操作
    8、list 分割字符串
        split与join正好相反, 它将一个字符串分割成多元素list
        注意, 分隔符(";") 被完全去掉了, 它没有在返回的list中的任意元素中出现。
        split接受一个可选的第二个参数, 它是要分割的次数。
'''
if __name__ == "__main__":
    li = ["server=mpilgrim", "uid=sa", "database=master", "pwd=secret"]
    print(li)

    s = ";".join(li)
    print(s)
    print(li)

    s.split(";")
    print(s)

    s.split(";", 1)
    print(s)
