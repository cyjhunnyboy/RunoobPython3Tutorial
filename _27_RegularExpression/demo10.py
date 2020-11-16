# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
findall 函数
描述：
    在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
    注意：match和search是匹配一次，findall匹配所有。
语法：
    re.findall(pattern, string, flags=0)
    或者
    pattern.findall(string[, pos[, endpos]])
    参数：
        pattern：匹配模式。
        string：待匹配的字符串。
        pos：可选参数，指定字符串的起始位置，默认为0。
        endpos：可选参数，指定字符串的结束位置，默认为字符串的长度。
'''
import re

if __name__ == "__main__":
    result1 = re.findall(r"\d+", "runoob 123 google 456")

    # 查找数字
    pattern = re.compile(r"\d+")
    result2 = pattern.findall("runoob 123 google 456")
    result3 = pattern.findall("run88oob123google456", 0, 10)

    print(result1)
    print(result2)
    print(result3)
