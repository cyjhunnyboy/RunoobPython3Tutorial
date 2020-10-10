# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python vars() 函数
描述：
    vars() 函数返回对象object的属性和属性值的字典对象
语法：
    vars([object])
    参数：
        object -- 对象
返回值：
    返回对象object的属性和属性值的字典对象，如果没有参数，就打印当前调用位置的属性和属性值 类似 locals()
'''


class Runoob:
    a = 1


if __name__ == "__main__":
    print(vars())
    print(vars(Runoob))
    runoob = Runoob()
    print(vars(runoob))
