# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 sorted() 函数
描述：
    sorted() 函数对所有可迭代的对象进行排序操作
    sort 与 sorted 区别：
        1、sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作
        2、list 的 sort 方法返回的是对已经存在的列表进行操作，
           而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
语法：
    sorted(iterable, key=None, reverse=False)
    参数说明：
        1、iterable -- 可迭代对象
        2、key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，
          指定可迭代对象中的一个元素来进行排序
        3、reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）
返回值：
    返回重新排序的列表
'''
if __name__ == "__main__":
    # 默认为升序
    print(sorted([5, 2, 3, 1, 4]))

    # list 的 list.sort() 方法。这个方法会修改原始的 list（返回值为None）
    # 通常这个方法不如sorted()方便-如果你不需要原始的 list，list.sort()方法效率会稍微高一些
    a = [5, 2, 3, 1, 4]
    a.sort()
    print(a)

    # 区别在于list.sort() 方法只为 list 定义。而 sorted() 函数可以接收任何的 iterable
    print(sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}))

    # 利用key进行倒序排序
    example_list = [5, 0, 6, 1, 2, 7, 3, 4]
    result_list = sorted(example_list, key=lambda x: x * -1)
    print(result_list)

    # 进行反向排序，也通过传入第三个参数 reverse=True
    print(sorted(example_list, reverse=True))

    # sorted 的应用，也可以通过 key 的值来进行数组/字典的排序
    array = [{"age": 20, "name": "a"}, {"age": 25, "name": "b"}, {"age": 10, "name": "c"}]
    array = sorted(array, key=lambda x: x["age"])
    print(array)

    # 多列排序
    # 先按照成绩降序排序，相同成绩的按照名字升序排序
    dict1 = [{'name': 'alice', 'score': 38}, {'name': 'bob', 'score': 18}, {'name': 'darl', 'score': 28},
             {'name': 'christ', 'score': 28}]
    dict2 = sorted(dict1, key=lambda x: (-x['score'], x['name']))
    print(dict2)
