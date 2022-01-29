# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python getattr() 函数
描述：
    getattr() 函数对应函数 setattr()，用于获取属性值，该属性不一定是存在的。
语法：
    getattr(object, name)
    参数：
        object -- 对象。
        name -- 字符串，对象属性。
返回值：
    对象属性的值
'''


class A(object):
    bar = 1


if __name__ == "__main__":
    a = A()
    # 获取属性 bar 值
    bar_1 = getattr(a, "bar")
    print(bar_1)
    # 设置属性 bar 值
    setattr(a, 'bar', 5)
    print(a.bar)
