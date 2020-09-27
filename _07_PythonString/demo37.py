# -*- coding: UTF-8 -*-
# author: chen_yong_jun
"""
Python3 rstrip()方法
描述：
rstrip() 删除 string 字符串末尾的指定字符（默认为空格）
语法：str.rstrip([chars])
参数：chars -- 指定删除的字符（默认为空格）
返回值：返回删除 string 字符串末尾的指定字符后生成的新字符串
"""
str_a = "     this is string example....wow!!!     "
print(str_a.rstrip())
# print(str_a.lstrip())
# print(str_a.strip())

str_b = "*****this is string example....wow!!!*****"
print(str_b.rstrip("*"))
# print(str_b.lstrip("*"))
# print(str_b.strip("*"))
