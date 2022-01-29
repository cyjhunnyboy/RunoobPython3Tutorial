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


class C(object):

    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")


# 如果 c 是 C 的实例化, c.x 将触发 getter,c.x = value 将触发 setter ， del c.x 触发 deleter。
# 如果给定 doc 参数，其将成为这个属性值的 docstring，否则 property 函数就会复制 fget 函数的 docstring（如果有的话）
if __name__ == "__main__":
    c = C()
    c.x = "Python"
    print(c.x)
