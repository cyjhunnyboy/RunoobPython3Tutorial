# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python setattr() 函数
描述：
    setattr() 函数对应函数 getattr()，用于设置属性值，该属性不一定是存在的。
语法：
    setattr(object, name, value)
    参数：
        object -- 对象。
        name -- 字符串，对象属性。
        value -- 属性值。
返回值：
    无
'''


class A(object):
    bar = 1


if __name__ == "__main__":
    a = A()
    # 获取属性 bar 值
    getattr(a, "bar")
    print(a.bar)
    # 设置属性 bar 值
    setattr(a, 'bar', 5)
    print(a.bar)
