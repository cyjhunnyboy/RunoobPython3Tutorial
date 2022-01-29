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

在上面，当匹配成功时返回一个Match对象，其中：
    group([group1, …])：方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用group()或group(0)；
    start([group])：方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为0；
    end([group])：方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为0；
    span([group])：方法返回(start(group), end(group))。
'''
import re

if __name__ == "__main__":
    # re.I 表示忽略大小写
    pattern = re.compile(r"([a-z]+) ([a-z]+)", re.I)
    m = pattern.match("Hello World Wide Web")
    # 匹配成功，返回一个Match对象
    print(m)

    # 返回匹配成功的整个子串
    print(m.group(0))

    # 返回匹配成功的整个子串的索引
    print(m.span(0))

    # 返回第一个分组匹配成功的子串
    print(m.group(1))

    # 返回第一个分组匹配成功的子串的索引
    print(m.span(1))

    # 返回第二个分组匹配成功的子串
    print(m.group(2))

    # 返回第二个分组匹配成功的子串的索引
    print(m.span(2))

    # 等价于(m.group(1), m.group(2), ...)
    print(m.groups())

    # 不存在第三个分组
    print(m.group(3))
