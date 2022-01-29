# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
re.search方法
    描述：
        扫描整个字符串并返回第一个成功的匹配
    语法：
        re.search(pattern, string, flags=0)
    参数：
        pattern：匹配的正则表达式
        string: 要匹配的字符串。
        flags: 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等

    正则表达式修饰符 - 可选标志
        re.I：使匹配对大小写不敏感
        re.L：做本地化识别（locale-aware）匹配
        re.M：多行匹配，影响^和$
        re.S：使.匹配包括换行在内的所有字符
        re.U：根据Unicode字符集解析字符。这个标志影响\w, \W, \b, \B.
        re.X：该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
    返回值：
        匹配成功re.search方法返回一个匹配的对象，否则返回None

    可以使用group(num)或groups()匹配对象函数来获取匹配表达式
        group(num=0)：匹配的整个表达式的字符串，group()可以一次输入多个组号，
                      在这种情况下它将返回一个包含那些组所对应值的元组。
        groups()：返回一个包含所有小组字符串的元组，从1到所含的小组号。
'''
import re

if __name__ == "__main__":
    # 在起始位置匹配
    print(re.search("www", "www.runoob.com").span())
    # 不在起始位置匹配
    print(re.search("com", "www.runoob.com").span())
