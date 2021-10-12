# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 元组
        元组运算符
            与字符串一样，元组之间可以使用+号和*号进行运算。
            这就意味着他们可以组合和复制，运算后会生成一个新的元组
"""
if __name__ == "__main__":
    # 计算元素个数
    print(len((1, 2, 3)))

    # 连接
    print((1, 2, 3) + (4, 5, 6))

    # 复制
    print(('Hi!',) * 4)
    # 元素是否存在

    print(3 in (1, 2, 3))

    # 迭代
    for x in (1, 2, 3):
        print(x, end=" ")
