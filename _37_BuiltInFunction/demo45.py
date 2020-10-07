# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python callable() 函数
描述：
    callable() 函数用于检查一个对象是否是可调用的。如果返回 True，object 仍然可能调用失败；但如果返回 False，调用对象 object 绝对不会成功
    对于函数、方法、lambda 函式、 类以及实现了 __call__ 方法的类实例, 它都返回 True
语法：
    callable(object)
    参数：
        object -- 对象
返回值：
    可调用返回 True，否则返回 False
'''
print(callable(0))
print(callable("runoob"))

def add(c, d):
    return c + d

# 函数返回true
print(callable(add))

class A:

    def method(self):
        return 0


# 类返回true
print(callable(A))
a = A()
# 没有实现 __call__, 返回 False
print(callable(a))

class B:

    def __call__(self, *args, **kwargs):
        return 0


print(callable(B))
b = B()
# 实现 __call__, 返回 True
print(callable(b))
