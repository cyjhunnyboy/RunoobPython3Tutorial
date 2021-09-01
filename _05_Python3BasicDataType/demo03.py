# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 基本数据类型
        1、标准数据类型
            Python3中有六个标准的数据类型：
                Number（数字）
                String（字符串）
                List（列表）
                Tuple（元组）
                Set（集合）
                Dictionary（字典）
            Python3的六个标准数据类型中：
                不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
                可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
"""
if __name__ == "__main__":
    # 数字
    num = 150
    print(num)

    # 字符串
    name = "John Doe"
    print(name)

    # 列表
    numList = [1, 2, 3, 4, 5]
    print(numList)

    # 元组
    numTuple = (1, 2, 3, 4, 5)
    print(numTuple)

    # 集合
    sites = {"Google", "Taobao", "Baidu", "Runoob", "Facebook", "Zhihu"}
    print(sites)

    # 字典
    tinyDict = {"name": "runoob", "code": 1, "site": "www.runoob.com"}
    print(tinyDict)
