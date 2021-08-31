# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
    Python3 基础语法
        1、行与缩进
            Python最具特色的就是使用缩进来表示代码块，不需要使用大括号{}。
            缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数
            缩进不一致，会导致运行错误
'''
if __name__ == "__main__":
    num = 1
    if num != 1:
        print("True")
    else:
        print("False")

    print("Hello, Jack!")
