# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 函数
        函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
        函数能提高应用的模块性，和代码的重复利用率。你已经知道Python提供了许多内建函数，比如print()。但你也可以自己创建函数，
        这被叫做用户自定义函数。

        定义一个函数
            你可以定义一个由自己想要功能的函数，以下是简单的规则：
            1、函数代码块以def关键词开头，后接函数标识符名称和圆括号()。
            2、任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
            3、函数的第一行语句可以选择性地使用文档字符串--用于存放函数说明。
            4、函数内容以冒号起始，并且缩进。
            5、return [表达式]结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回None。
        语法：
            Python定义函数使用def关键字，一般格式如下：
                def 函数名（参数列表）:
                    函数体

        默认情况下，参数值和参数名称是按函数声明中定义的顺序匹配起来的
"""


def area(width, height):
    """计算面积"""
    return width * height


def print_welcome(name):
    """控制台输出，Welcome {name}"""
    print("Welcome", name)


if __name__ == "__main__":
    print_welcome("Runoob")
    w = 4
    h = 5
    print("width =", w, " height =", h, " area =", area(w, h))
