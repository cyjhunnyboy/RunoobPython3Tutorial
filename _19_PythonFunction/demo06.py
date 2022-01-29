# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 函数
参数
    以下是调用函数时可使用的正式参数类型：
    1、必需参数
    2、关键字参数
    3、默认参数
    4、不定长参数
必需参数
    必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样
'''


# 可写函数说明
def printme(printstr):
    """打印任何传入的字符串"""
    print(printstr)
    return


if __name__ == "__main__":
    # 调用printme函数，不加参数会报错
    # TypeError: printme() missing 1 required
    # positional argument: 'printstr'
    printme()
