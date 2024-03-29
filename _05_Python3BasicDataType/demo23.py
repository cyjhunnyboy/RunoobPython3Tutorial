# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python数据类型转换
        有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。

        以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值
            int(x [,base]) 将x转换为一个整数
            float(x) 将x转换到一个浮点数
            complex(real [,imag]) 创建一个复数
            str(x) 将对象 x 转换为字符串
            repr(x) 将对象 x 转换为表达式字符串
            eval(str) 用来计算在字符串中的有效Python表达式,并返回一个对象
            tuple(s) 将序列 s 转换为一个元组
            list(s) 将序列 s 转换为一个列表
            set(s) 转换为可变集合
            dict(d) 创建一个字典。d 必须是一个序列 (key,value)元组。
            frozenset(s) 转换为不可变集合
            chr(x) 将一个整数转换为一个字符
            ord(x) 将一个字符转换为它的整数值
            hex(x) 将一个整数转换为一个十六进制字符串
            oct(x) 将一个整数转换为一个八进制字符串

    Python int()函数
        描述：
            int()函数用于将一个字符串或数字转换为整型。
        语法：
            class int(x, base=10)
            参数：
                x -- 字符串或数字。
                base -- 进制数，默认十进制。
        返回值：
            返回整型数据。
"""
if __name__ == "__main__":
    print(int())
    print(int(3))
    print(int(3.6))
    # 如果是带参数base的话，12要以字符串的形式进行输入，12为16进制
    print(int('12', 16))
    print(int('0xa', 16))
    print(int('10', 8))
