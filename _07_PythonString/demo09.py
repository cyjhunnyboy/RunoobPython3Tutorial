# -*- coding: UTF-8 -*-
# author: chen_yong_jun

"""
Python3 center()方法
center() 方法返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格
语法：str.center(width[, fillchar])
参数：width -- 字符串的总宽度。 fillchar -- 填充字符。
返回值：返回一个指定的宽度 width 居中的字符串，如果 width 小于字符串宽度直接返回字符串，否则使用 fillchar 去填充。
"""
str_a = "[www.runoob.com]"

print("str.center(40, '*') : ", str_a.center(40, '*'))
