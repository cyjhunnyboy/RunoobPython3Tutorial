# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python hasattr() 函数
描述：
    hasattr() 函数用于判断对象是否包含对应的属性
语法：
    hasattr(object, name)
    参数：
        object -- 对象
        name -- 字符串，属性名
返回值：
    如果对象有该属性返回 True，否则返回 False
'''


class Coordinate:
    """Coordinate类"""

    x = 10
    y = -5
    z = 0


if __name__ == "__main__":
    point1 = Coordinate()
    print(hasattr(point1, 'x'))
    print(hasattr(point1, 'y'))
    print(hasattr(point1, 'z'))
    # 没有该属性
    print(hasattr(point1, 'no'))
