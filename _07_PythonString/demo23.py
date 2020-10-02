# -*- coding: UTF-8 -*-
# author: chenyongjun
"""
Python3 istitle()方法
istitle() 方法检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写
语法：str.istitle()
参数：无
返回值：如果字符串中所有的单词拼写首字母是否为大写，且其他字母为小写则返回 True，否则返回 False
"""
str1 = "This Is String Example...Wow!!!"
print(str1.istitle())

str2 = "Runoob example....wow!!!"
print(str2.istitle())
