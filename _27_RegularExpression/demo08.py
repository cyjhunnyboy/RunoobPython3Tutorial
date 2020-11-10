# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
compile 函数
描述：
    compile函数用于编译正则表达式，生成一个正则表达式（Pattern）对象，供match()和search()这两个函数使用。
语法：
    re.compile(pattern[,flags])
    参数：
        pattern：一个字符串形式的正则表达式
        flags：可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
            re.I：忽略大小写
            re.L：表示特殊字符集\w, \W, \b, \B, \s, \S依赖于当前环境
            re.M：多行模式
            re.S：即为'.'并且包括换行符在内的任意字符（'.'不包括换行符）
            re.U：表示特殊字符集\w, \W, \b, \B, \d, \D, \s, \S依赖于Unicode字符属性数据库
            re.X：为了增加可读性，忽略空格和'#'后面的注释
'''
import re

if __name__ == "__main__":
    # 用于匹配至少一个数字
    pattern = re.compile(r"\d+")
    # 查找头部，没有匹配
    m = pattern.match("one12twothree34four")
    print(m)

    # # 从'e'的位置开始匹配，没有匹配
    m = pattern.match("one12twothree34four", 2, 10)
    print(m)

    # 从'1'的位置开始匹配，正好匹配
    m = pattern.match("one12twothree34four", 3, 10)
    print(m)

    # 可省略 0
    print(m.group(0))
    print(m.start(0))
    print(m.end(0))
    print(m.span(0))
