# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python3 ljust()方法
            描述：
                ljust()方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串
            语法：
                str.ljust(width[, fillchar)
                参数：
                    width -- 指定字符串长度。
                    fillchar -- 填充字符，默认为空格
            返回值：
                返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串
"""
if __name__ == "__main__":
    s1 = "Runoob example....wow!!!"
    print(s1.ljust(50, "*"))
