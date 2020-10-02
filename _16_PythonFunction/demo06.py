# -*- coding: UTF-8 -*-
# author: chenyongjun


# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
# 可写函数说明
def print_info(arg1, *vartuple):
    """打印任何传入的参数"""
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# 调用print_info函数
# 如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量
print_info(10)
print_info(70, 60, 50)
