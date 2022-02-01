# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
Python3 函数
    函数调用
        定义一个函数：给了函数一个名称，指定了函数里包含的参数，和代码块结构。
        这个函数的基本结构完成以后，你可以通过另一个函数调用执行，也可以直接从Python命令提示符执行。
"""


# 定义函数
def printme(str_print):
    """打印任何传入的字符串"""
    print(str_print)
    return


if __name__ == "__main__":
    # 调用函数
    printme("我要调用用户自定义函数!")
    printme("再次调用同一函数")
