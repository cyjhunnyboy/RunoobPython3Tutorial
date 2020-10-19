# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 元组
    Python的元组与列表类似，不同之处在于元组的元素不能修改。
    元组使用小括号，列表使用方括号。
    元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
    创建元组：
        tup1 = ()

    元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用
    元组与字符串类似，下标索引从0开始，可以进行截取，组合等
'''
if __name__ == "__main__":
    # 创建空元组
    tuple_1 = ()
    print(type(tuple_1))
    print(tuple_1)

    tuple_2 = ("Google", "Runoob", 1997, 2000)
    print(type(tuple_2))
    print(tuple_2)

    tuple_3 = (1, 2, 3, 4, 5)
    print(type(tuple_3))
    print(tuple_3)

    # 不需要括号也可以
    tuple_4 = 'a', 'b', 'c', 'd'
    print(type(tuple_4))
    print(tuple_4)
