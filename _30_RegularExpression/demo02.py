# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 正则表达式
    正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。
    Python自1.5版本起增加了re模块，它提供Perl风格的正则表达式模式。
    re模块使Python语言拥有全部的正则表达式功能。
    compile函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换。
    re模块也提供了与这些方法功能完全一致的函数，这些函数使用一个模式字符串做为它们的第一个参数。

re.match函数
    描述：
        尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
    语法：
        re.match(pattern, string, flags=0)
        参数：
            pattern：匹配的正则表达式
            string: 要匹配的字符串。
            flags: 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等

            正则表达式修饰符 - 可选标志
                正则表达式可以包含一些可选标志修饰符来控制匹配的模式。修饰符被指定为一个可选的标志。
                多个标志可以通过按位OR(|)它们来指定。如：re.I|re.M被设置成I和M标志：
                re.I：使匹配对大小写不敏感
                re.L：做本地化识别（locale-aware）匹配
                re.M：多行匹配，影响^和$
                re.S：使.匹配包括换行在内的所有字符
                re.U：根据Unicode字符集解析字符。这个标志影响\w, \W, \b, \B.
                re.X：该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
    返回值：
        匹配成功re.match方法返回一个匹配的对象，否则返回None。

    可以使用group(num)或groups()匹配对象函数来获取匹配表达式
        group(num=0)：匹配的整个表达式的字符串，group()可以一次输入多个组号，
                      在这种情况下它将返回一个包含那些组所对应值的元组。
        groups()：返回一个包含所有小组字符串的元组，从1到所含的小组号。
'''
import re

if __name__ == "__main__":
    line = "Cats are smarter than dogs"

    # .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
    matchObj = re.match(r"(.*) are (.*?) .*", line, re.M | re.I)

    if matchObj:
        print("matchObj.group()：", matchObj.group())
        print("matchObj.group(1)：", matchObj.group(1))
        print("matchObj.group(2)：", matchObj.group(2))
    else:
        print("No match!!")
