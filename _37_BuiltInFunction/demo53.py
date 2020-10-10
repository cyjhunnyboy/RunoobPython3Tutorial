# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 chr() 函数
描述：
    chr() 用一个整数作参数，返回一个对应的字符
语法：
    chr(i)
    参数：
        i -- 可以是 10 进制也可以是 16 进制的形式的数字，数字范围为 0 到 1,114,111 (16 进制为0x10FFFF)
返回值：
    返回值是当前整数对应的 ASCII 字符
'''
if __name__ == "__main__":
    print(chr(0x30))
    print(chr(97))
    print(chr(8364))
