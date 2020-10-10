# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python issubclass() 函数
描述：
    issubclass() 方法用于判断参数 class 是否是类型参数 classinfo 的子类
语法：
    issubclass(class, classinfo)
    参数：
        class -- 类
        classinfo -- 类
返回值：
    如果 class 是 classinfo 的子类返回 True，否则返回 False
'''


class A:
    pass


class B(A):
    pass


if __name__ == "__main__":
    # 返回 True
    print(issubclass(B, A))
