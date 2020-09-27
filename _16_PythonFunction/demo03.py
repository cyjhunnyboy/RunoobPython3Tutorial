# -*- coding: UTF-8 -*-
# author: chen_yong_jun

"""
函数调用
定义一个函数：给了函数一个名称，指定了函数里包含的参数，和代码块结构。

这个函数的基本结构完成以后，你可以通过另一个函数调用执行，也可以直接从 Python 命令提示符执行。

如下实例调用了 printme() 函数：
"""


# 定义函数
def print_me(str_print):
    """打印任何传入的字符串"""
    print(str_print)
    return


# 调用函数
print_me("我要调用用户自定义函数!")
print_me("再次调用同一函数")
