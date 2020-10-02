# -*- coding: UTF-8 -*-
# author: chenyongjun
"""
Python3 expandtabs()方法
expandtabs() 方法把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8
语法：str.expandtabs(tabsize=8)
参数：tabsize -- 指定转换字符串中的 tab 符号('\t')转为空格的字符数
返回值：该方法返回字符串中的 tab 符号('\t')转为空格后生成的新字符串
"""
str_a = "this is\tstring example....wow!!!"

print("原始字符串: " + str_a)
print("替换 \\t 符号: " + str_a.expandtabs())
print("使用16个空格替换 \\t 符号: " + str_a.expandtabs(16))

