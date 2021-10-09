# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python3 split()方法
            描述：
                split()通过指定分隔符对字符串进行切片，如果参数num有指定值，则仅分隔num个子字符串
            语法：
                str.split(str="", num=string.count(str))
                参数：
                    str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
                    num -- 分割次数
            返回值：
                返回分割后的字符串列表
"""
if __name__ == "__main__":
    str_a = "this is string example....wow!!!"
    print(str_a.split())
    print(str_a.split('i', 1))
    print(str_a.split('w'))

    str_b = "path>//input[@id='login']"
    print(str_b.split(">"))
