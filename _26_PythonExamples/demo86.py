# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 使用正则表达式提取字符串中的 URL
    给定一个字符串，里面包含URL地址，需要我们使用正则表达式来获取字符串的URL。
    ?:说明：
        (?:x)：匹配x但是不记住匹配项。这种括号叫作非捕获括号，使得你能够定义与正则表达式运算符一起使用的子表达式。
        看看这个例子/(?:foo){1,2}/。如果表达式是/foo{1,2}/，{1,2}将只应用于'foo'的最后一个字符'o'。如果使用非捕获括号，则{1,2}会应用于整个'foo'单词。
        执行以上代码输出结果为：
        Urls: ['https://www.runoob.com', 'https://www.google.com']
'''
import re


def find(str):
    # findall()查找匹配正则表达式的字符串
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', str)
    return url


if __name__ == "__main__":
    str = "Runoob 的网页地址为：https://www.runoob.com，Google 的网页地址为：https://www.google.com"
    print("urls：", find(str))
