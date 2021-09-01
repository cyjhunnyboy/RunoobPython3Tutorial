# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python数据类型转换
        Python hex()函数
            描述：
                hex()函数用于将10进制整数转换成16进制，以字符串形式表示
            语法：
                hex(x)
                参数：
                    x -- 10进制整数
            返回值：
                返回16进制数，以字符串形式表示
"""
if __name__ == "__main__":
    print(hex(255))
    print(hex(-42))
    print(hex(1))
    print(hex(12))
    print(type(hex(12)))
