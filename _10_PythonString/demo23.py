# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python3 isspace()方法
            描述：
                isspace()方法检测字符串是否只由空白字符组成
            语法：
                str.isspace()
                参数：
                    无
            返回值：
                如果字符串中只包含空格，则返回True，否则返回False
"""
if __name__ == "__main__":
    str1 = "   "
    print(str1.isspace())

    str2 = "Runoob example....wow!!!"
    print(str2.isspace())
