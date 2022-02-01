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
        默认参数
            调用函数时，如果没有传递参数，则会使用默认参数。
"""


# 可写函数说明
def printinfo(name, age=35):
    """打印任何传入的字符串"""
    print("名字：", name)
    print("年龄：", age)
    return


if __name__ == "__main__":
    # 调用printinfo函数
    printinfo(age=50, name="runoob")
    # 调用函数时，如果没有传递参数，则会使用默认参数。
    # 以下实例中如果没有传入age参数，则使用默认值
    print("------------------------")
    printinfo(name="runoob")
