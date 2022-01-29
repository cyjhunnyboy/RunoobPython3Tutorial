# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python any() 函数
描述：
    any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，
    如果有一个为 True，则返回 True，元素除了是 0、空、FALSE 外都算 TRUE
    函数等价于：
        def any(iterable):
            for element in iterable:
                if element:
                    return True
            return False
语法：
    any(iterable)
    参数：
        iterable -- 元组或列表。
返回值：
    如果都为空、0、false，则返回false，如果不都为空、0、false，则返回true
'''
if __name__ == "__main__":
    # 列表list，元素都不为空或0
    print(any(['a', 'b', 'c', 'd']))
    # 列表list，存在一个为空的元素
    print(any(['a', 'b', '', 'd']))
    # 列表list,元素全为0,'',false
    print(any([0, '', False]))
    # 空列表
    print(any([]))

    # 元组tuple，元素都不为空或0
    print(any(('a', 'b', 'c', 'd')))
    # 元组tuple，存在一个为空的元素
    print(any(('a', 'b', '', 'd')))
    # 元组tuple，元素全为0,'',false
    print(any((0, '', False)))
    # 空元组
    print(any(()))
