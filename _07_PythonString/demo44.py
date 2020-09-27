# -*- coding: UTF-8 -*-
# author: chen_yong_jun
"""
Python3 translate()方法
描述：
translate() 方法根据参数table给出的表(包含 256 个字符)转换字符串的字符,要过滤掉的字符放到 deletechars 参数中
语法：
str.translate(table)
bytes.translate(table[, delete])
bytearray.translate(table[, delete]
参数：
table -- 翻译表，翻译表是通过 maketrans() 方法转换而来。
deletechars -- 字符串中要过滤的字符列表。
返回值：返回翻译后的字符串,若给出了 delete 参数，则将原来的bytes中的属于delete的字符删除，剩下的字符要按照table中给出的映射来进行映射
"""
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)  # 制作翻译表

str_a = "this is string example....wow!!!"
print(str_a.translate(trantab))

# 制作翻译表
bytes_tabtrans = bytes.maketrans(b'abcdefghijklmnopqrstuvwxyz', b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# 转换为大写，并删除字母o
print(b'runoob'.translate(bytes_tabtrans, b'o'))
