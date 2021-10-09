# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python3 center()方法
            描述：
                center()方法返回一个指定的宽度width居中的字符串，fillchar为填充的字符，默认为空格
            语法：
                str.center(width[, fillchar])
                参数：
                    width -- 字符串的总宽度。
                    fillchar -- 填充字符。
            返回值：
                返回一个指定的宽度width居中的字符串，如果width小于字符串宽度直接返回字符串，否则使用fillchar去填充。
"""
if __name__ == "__main__":
    str_a = "[www.runoob.com]"

    # width大于字符串宽度
    print("str.center(40, '*') : ", str_a.center(40, '*'))

    # width小于字符串宽度
    print("str.center(4, '*') : ", str_a.center(4, '*'))

    # fillchar默认是空格
    print("str.center(40) : ", str_a.center(40))

    # fillchar只能是单个字符
    print("str.center(40, '?!') : ", str_a.center(40, "?!"))
