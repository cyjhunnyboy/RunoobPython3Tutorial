# -*- coding: UTF-8 -*-
# author: chen_yong_jun

"""
Python3 List sort()方法
描述
sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。

语法
sort()方法语法：

list.sort(cmp=None, key=None, reverse=False)
参数

cmp -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序。
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
"""
aList = ['Google', 'Runoob', 'Taobao', 'Facebook']

aList.sort()
print("List : ", aList)

# 列表
vowels = ['e', 'a', 'u', 'o', 'i']
# 降序
vowels.sort(reverse=True)
# 输出结果
print('降序输出:', vowels)


# 获取列表的第二个元素
def take_second(elem):
    return elem[1]


# 列表
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# 指定第二个元素排序
random.sort(key=take_second)

# 输出类别
print('排序列表：', random)
