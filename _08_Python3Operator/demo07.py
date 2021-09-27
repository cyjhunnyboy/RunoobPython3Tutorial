# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 运算符
        Python身份运算符
            身份运算符用于比较两个对象的存储单元
            is：判断两个标识符是不是引用自一个对象。实例：(x is y)，类似id(x)==id(y)，
                如果引用的是同一个对象则返回True，否则返回False
            is not：是判断两个标识符是不是引用自不同对象。实例：(x is not y)，类似id(a)!= id(b)，
                    如果引用的不是同一个对象则返回结果True，否则返回 False。
            注：id()函数用于获取对象内存地址。
"""
if __name__ == "__main__":
    a = 20
    b = 20

    if a is b:
        print("1-a和b有相同的标识")
    else:
        print("1-a和b没有相同的标识")

    if id(a) == id(b):
        print("2-a和b有相同的标识")
    else:
        print("2-a和b没有相同的标识")

    # 修改变量b的值
    b = 30
    if a is b:
        print("3-a和b有相同的标识")
    else:
        print("3-a和b没有相同的标识")

    if a is not b:
        print("4-a和b没有相同的标识")
    else:
        print("4-a和b有相同的标识")
