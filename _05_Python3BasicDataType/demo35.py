# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python数据类型转换
        Python ord()函数
            描述：
                ord()函数是chr( 函数（对于8位的ASCII字符串）或unichr()函数（对于Unicode对象）
                的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，
                或者Unicode数值，如果所给的Unicode字符超出了你的Python定义范围，则会引发一个TypeError的异常
            语法：
                ord(c)
                参数：
                    c -- 字符
            返回值：
                返回值是对应的十进制整数
"""
if __name__ == "__main__":
    print(ord("a"))
    print(ord("b"))
    print(ord("c"))
