# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python数据类型转换
        Python frozenset()函数
            描述：
                frozenset()返回一个冻结的集合，冻结后集合不能再添加或删除任何元素
            语法：
                class frozenset([iterable])
                参数：
                    iterable -- 可迭代的对象，比如列表、字典、元组等等
            返回值：
                返回新的 frozenset 对象，如果不提供任何参数，默认会生成空集合
"""
if __name__ == "__main__":
    # 生成一个新的不可变集合
    a = frozenset(range(10))
    print(a)
    # 创建不可变集合
    b = frozenset('runoob')
    print(b)
