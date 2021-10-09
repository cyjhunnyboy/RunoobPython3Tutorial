# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python3 rjust()方法
            描述：
                rjust()返回一个原字符串右对齐,并使用空格填充至长度width的新字符串。如果指定的长度小于字符串的长度则返回原字符串
            语法：
                str.rjust(width[, fillchar])
                参数：
                    width -- 指定填充指定字符后中字符串的总长度.
                    fillchar -- 填充的字符，默认为空格
            返回值：
                返回一个原字符串右对齐,并使用空格填充至长度width的新字符串。如果指定的长度小于字符串的长度则返回原字符串
"""
if __name__ == "__main__":
    str_a = "this is string example....wow!!!"
    print(str_a.rjust(50, '*'))
