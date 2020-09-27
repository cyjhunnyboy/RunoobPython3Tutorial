# -*- coding: UTF-8 -*-
# author: chen_yong_jun
"""
检索和替换
Python 的re模块提供了re.sub用于替换字符串中的匹配项
语法：re.sub(pattern, repl, string, count=0)
参数：
pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
"""
# repl 参数是一个函数
# 以下实例中将字符串中的匹配的数字乘于 2
import re


# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))
