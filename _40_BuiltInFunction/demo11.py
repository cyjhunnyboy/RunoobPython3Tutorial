# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 hex() 函数
描述：
    hex() 函数用于将一个指定数字转换为 16 进制数
语法：
    hex(x)
    参数：
        x -- 一个整数
返回值：
    返回一个字符串，以 0x 开头
'''
if __name__ == "__main__":
    print(hex(255))
    print(hex(-42))
    print(hex(12))
    # hex(x)返回值类型是“字符串”
    print(type(hex(12)))
