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
不定长参数
    一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数
    基本语法格式如下：
        def functionname([formal_args,] *var_args_tuple ):
            "函数_文档字符串"
            function_suite
            return [expression]
    加了星号*的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
'''


# 可写函数说明
def printinfo(arg, *vartuple):
    """打印任何传入的字符串"""
    print("输出：")
    print(arg)
    print(vartuple)


if __name__ == "__main__":
    # 如果在函数调用时没有指定参数，它就是一个空元组。
    # 我们也可以不向函数传递未命名的变量
    printinfo(10)

    print("===========")

    # 调用printinfo函数
    printinfo(70, 60, 50)
