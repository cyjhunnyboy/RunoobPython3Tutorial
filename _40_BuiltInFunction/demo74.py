# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python hash() 函数
描述：
    hash() 用于获取取一个对象（字符串或者数值等）的哈希值
语法：
    hash(object)
    参数：
        object -- 对象
返回值：
    返回对象的哈希值
'''
if __name__ == "__main__":
    # 字符串
    print(hash('test'))
    # 数字
    print(hash(1))
    # 集合
    print(hash(str([1, 2, 3])))
    # 字典
    print(hash(str(sorted({'1': 1}))))
