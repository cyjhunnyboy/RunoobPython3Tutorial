# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 基础语法
        1、空行
            函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
            空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。
            但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
            记住：空行也是程序代码的一部分。

        2、等待用户输入
            "\n\n"在结果输出前会输出两个新的空行。一旦用户按下enter键时，程序将退出
"""
if __name__ == "__main__":
    # 等待用户输入
    # 执行下面的程序在按回车键后就会等待用户输入
    input("\n\n按下Enter键后退出。\n")
