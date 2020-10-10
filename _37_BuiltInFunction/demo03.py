# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python dict() 函数
描述：
    dict() 函数用于创建一个字典
语法：
    class dict(**kwarg)
    class dict(mapping, **kwarg)
    class dict(iterable, **kwarg)
    参数说明：
        **kwargs -- 关键字
        mapping -- 元素的容器。
        iterable -- 可迭代对象。
返回值：
    返回一个字典
'''
if __name__ == "__main__":
    # 创建空字典
    dict1 = dict()
    print(dict1)

    # 传入关键字
    dict2 = dict(a='a', b='b', t='t')
    print(dict2)

    # 映射函数方式来构造字典
    dict3 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
    print(dict3)

    # 可迭代对象方式来构造字典
    dict3 = dict([('one', 1), ('two', 2), ('three', 3)])
    print(dict3)
