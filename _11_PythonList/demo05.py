# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 列表
        Python列表脚本操作符
            列表对+和*的操作符与字符串相似。+号用于组合列表，*号用于重复列表
"""
if __name__ == "__main__":
    # 长度
    print(len([1, 2, 3]))
    # 组合
    print([1, 2, 3] + [4, 5, 6])
    # 重复
    print(["Hi!"] * 4)
    # 元素是否存在于列表中
    print(3 in [1, 2, 3])
    # 迭代
    for x in [1, 2, 3]:
        print(x, end=" ")
