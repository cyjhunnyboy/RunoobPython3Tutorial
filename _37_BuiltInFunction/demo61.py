# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python locals() 函数
描述：
    locals() 函数会以字典类型返回当前位置的全部局部变量
    对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True
语法：
    locals()
    参数：
        无
返回值：
    返回字典类型的局部变量
'''


# 两个局部变量：arg、z
def runoob(arg):
    z = 1
    print(locals())


if __name__ == "__main__":
    # 返回一个名字/值对的字典
    runoob(4)
