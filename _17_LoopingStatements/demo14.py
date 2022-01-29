# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 循环语句
        pass语句
            Python pass是空语句，是为了保持程序结构的完整性
            pass不做任何事情，一般用做占位语句
"""
if __name__ == "__main__":
    for letter in "Runoob":
        if letter == 'o':
            # 字母为o时执行pass语句块
            pass
            print("执行pass块")
        print("当前字母：", letter)

    print("Good bye!")
