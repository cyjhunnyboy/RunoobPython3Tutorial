# -*- coding: UTF-8 -*-
# author: chenyongjun
"""
Python3 isnumeric()方法
isnumeric() 方法检测字符串是否只由数字组成。这种方法是只针对unicode对象
注：定义一个字符串为Unicode，只需要在字符串前添加 'u' 前缀即可
语法：str.isnumeric()
参数：无
返回值：如果字符串中只包含数字字符，则返回 True，否则返回 False
"""
str1 = u"runoob2016"
print(str1.isnumeric())

str2 = "23443434"
print(str2.isnumeric())
