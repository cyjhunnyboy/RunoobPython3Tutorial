# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 函数
        参数
            以下是调用函数时可使用的正式参数类型：
            1、必需参数
            2、关键字参数
            3、默认参数
            4、不定长参数
        关键字参数
            关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
            使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为Python解释器能够用参数名匹配参数值。
"""


# 可写函数说明
def printme(printstr):
    """打印任何传入的字符串"""
    print(printstr)
    return


if __name__ == "__main__":
    # 调用printme函数，不加参数会报错
    printme(printstr="菜鸟教程")
