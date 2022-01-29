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

    还有一种就是参数带两个星号**基本语法如下：
        def functionname([formal_args,] **var_args_dict ):
            "函数_文档字符串"
            function_suite
            return [expression]
    加了两个星号**的参数会以字典的形式导入
'''


# 可写函数说明
def printinfo(arg, **vardict):
    """打印任何传入的字符串"""
    print("输出：")
    print(arg)
    print(vardict)


if __name__ == "__main__":
    # 调用printinfo函数
    printinfo(1, a=2, b=3)
