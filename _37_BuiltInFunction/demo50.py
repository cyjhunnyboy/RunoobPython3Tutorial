# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python property() 函数
描述：
    property() 函数的作用是在新式类中返回属性值
语法：
    class property([fget[, fset[, fdel[, doc]]]])
    参数：
        fget -- 获取属性值的函数
        fset -- 设置属性值的函数
        fdel -- 删除属性值函数
        doc -- 属性描述信息
返回值：
    返回新式类属性
'''


class Parrot(object):

    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage


# 上面的代码将 voltage() 方法转化成同名只读属性的 getter 方法
if __name__ == "__main__":
    parrot = Parrot()
    print(parrot.voltage)
