# -*- coding: UTF-8 -*-
# author: chen_yong_jun


# 加了两个星号 ** 的参数会以字典的形式导入
# 可写函数说明
def print_info(arg1, **vardict):
    """打印任何传入的参数"""
    print("输出: ")
    print(arg1)
    print(vardict)
    for key, value in vardict.items():
        print(key, value)
    print(len(vardict))


# 调用print_info函数
print_info(1, a=2, b=3)
