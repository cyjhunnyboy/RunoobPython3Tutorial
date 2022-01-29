# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python frozenset() 函数
描述：
    frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素
语法：
    class frozenset([iterable])
    参数：
        iterable -- 可迭代的对象，比如列表、字典、元组等等
返回值：
    返回新的 frozenset 对象，如果不提供任何参数，默认会生成空集合

为什么需要冻结的集合（即不可变的集合）呢？因为在集合的关系中，有集合的中的元素是另一个集合的情况，但是普通集合（set）本身是可变的，
那么它的实例就不能放在另一个集合中（set中的元素必须是不可变类型）。所以，frozenset提供了不可变的集合的功能，
当集合不可变时，它就满足了作为集合中的元素的要求，就可以放在另一个集合中了
'''
if __name__ == "__main__":
    # 生成一个新的不可变集合
    a = frozenset(range(10))
    print(a)

    b = frozenset('runoob')
    print(b)
