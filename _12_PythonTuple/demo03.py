# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 元组
        元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用
"""
if __name__ == "__main__":
    # 不加 逗号，类型为整型
    tuple_1 = (50)
    print(type(tuple_1))
    print(tuple_1)

    # 加上逗号，类型为元组
    tuple_2 = (60,)
    print(type(tuple_2))
    print(tuple_2)
