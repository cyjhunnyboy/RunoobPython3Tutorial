# -*- coding: UTF-8 -*-
# author: chen_yong_jun
"""
Python3 lstrip()方法
lstrip() 方法用于截掉字符串左边的空格或指定字符
语法：str.lstrip([chars])
参数：chars --指定截取的字符
返回值：返回截掉字符串左边的空格或指定字符后生成的新字符串
"""
str1 = "     this is string example....wow!!!     "
print(str1.lstrip())
str2 = "88888888this is string example....wow!!!8888888"
print(str2.lstrip('8'))
