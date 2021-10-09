# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python3 isdecimal()方法
            描述：
                isdecimal()方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象
                注意:定义一个十进制字符串，只需要在字符串前添加'u'前缀即可
            语法：
                str.isdecimal()
                参数：
                    无
            返回值：
                如果字符串是否只包含十进制字符返回True，否则返回False
"""
if __name__ == "__main__":
    str1 = "runoob2016"
    print(str1.isdecimal())

    str2 = "23443434"
    print(str2.isdecimal())
