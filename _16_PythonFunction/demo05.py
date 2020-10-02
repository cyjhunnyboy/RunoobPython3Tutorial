# -*- coding: UTF-8 -*-
# author: chenyongjun


# 可写函数说明
# 你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
def print_info(arg1, *vartuple):
    """打印任何传入的参数"""
    print("输出: ")
    print(arg1)
    print(vartuple)


# 调用print_info函数
print_info(70, 60, 50)
