# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
检索和替换
    Python的re模块提供了re.sub用于替换字符串中的匹配项
语法：
    re.sub(pattern, repl, string, count=0, flags=0)
    参数：
        pattern：正则中的模式字符串。
        repl：替换的字符串，也可为一个函数。
        string：要被查找替换的原始字符串。
        count：模式匹配后替换的最大次数，默认0表示替换所有的匹配。
        flags：编译时用的匹配模式，数字形式。

        repl参数是一个函数
'''
import re


def double(matched):
    """将匹配的数字乘于2"""

    value = int(matched.group("value"))
    return str(value * 2)


if __name__ == "__main__":
    s = "A23G4HFD567"
    print(re.sub("(?P<value>\d+)", double, s))
