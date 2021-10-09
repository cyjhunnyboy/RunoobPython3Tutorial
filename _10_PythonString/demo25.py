# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python3 isupper()方法
            描述：
                isupper()方法检测字符串中所有的字母是否都为大写
            语法：
                str.isupper()
                参数：
                    无
            返回值：
                如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回True，否则返回False
"""
if __name__ == "__main__":
    str1 = "THIS IS STRING EXAMPLE....WOW!!!"
    print(str1.isupper())

    str2 = "Runoob example....wow!!!"
    print(str2.isupper())
