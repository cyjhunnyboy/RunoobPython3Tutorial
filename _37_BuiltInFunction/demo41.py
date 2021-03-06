# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python iter() 函数
描述：
    iter() 函数用来生成迭代器
语法：
    iter(object[, sentinel])
    参数：
        object -- 支持迭代的集合对象
        sentinel -- 如果传递了第二个参数，则参数 object 必须是一个可调用的对象（如，函数），
        此时，iter 创建了一个迭代器对象，每次调用这个迭代器对象的__next__()方法时，都会调用 object
返回值：
    迭代器对象
'''
if __name__ == "__main__":
    list_1 = [1, 2, 3, 4, 5, 6]
    for i in iter(list_1):
        print(i)
