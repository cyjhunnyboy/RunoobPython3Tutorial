# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 字典copy()方法
描述：
    Python字典copy()函数返回一个字典的浅复制
语法：
    dict.copy()
    参数：
        NA
返回值：
    返回一个字典的浅复制
'''
if __name__ == "__main__":
    # 直接赋值和copy的区别
    dict1 = {"user": "runoob", "num": [1, 2, 3]}

    # 浅拷贝: 引用对象
    dict2 = dict1
    # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
    dict3 = dict1.copy()

    # 修改data数据
    dict1["user"] = "root"
    dict1["num"].remove(1)

    # 输出结果
    print(dict1)
    print(dict2)
    print(dict3)
