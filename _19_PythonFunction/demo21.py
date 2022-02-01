# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 函数
        全局变量和局部变量
            定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
            局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。
            调用函数时，所有在函数内声明的变量名称都将被加入到作用域中
"""
# 这是一个全局变量
total = 0


# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和"
    # total在这里是局部变量.
    total = arg1 + arg2
    print("函数内是局部变量：", total)
    return total


if __name__ == "__main__":
    # 调用sum函数
    sum(10, 20)
    print("函数外是全局变量：", total)
