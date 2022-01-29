# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python getattr() 函数
描述：
    getattr() 函数用于返回一个对象属性值
语法：
    getattr(object, name[, default])
    参数：
        object -- 对象
        name -- 字符串，对象属性
        default -- 默认返回值，如果不提供该参数，在没有对应属性时，将触发 AttributeError
返回值：
    返回对象属性值
'''


class A(object):
    bar = 1


if __name__ == "__main__":
    # 获取属性 bar 值
    a = A()
    print(getattr(a, "bar"))
    # 属性 bar2 不存在，触发异常
    # AttributeError: 'A' object has no attribute 'bar2'
    # print(getattr(a, "bar2"))
    # 属性 bar2 不存在，但设置了默认值
    print(getattr(a, "bar3", 3))
