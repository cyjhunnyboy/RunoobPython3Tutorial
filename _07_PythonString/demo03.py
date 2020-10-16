# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 字符串更新
    你可以截取字符串的一部分并与其他字段拼接

Python 转义字符
    转义字符        描述
    \(在行尾时)     续行符
    \\             反斜杠符号
    \'             单引号
    \"             双引号
    \a             响铃
    \b             退格(Backspace)
    \000           空
    \n             换行
    \v             纵向制表符
    \t             横向制表符
    \r             回车
    \f             换页
    \oyy           八进制数，yy代表的字符，例如：\o12代表换行，其中o是字母，不是数字0
    \xyy           十六进制数，yy代表的字符，例如：\x0a代表换行
    \other         其它的字符以普通格式输出
'''
if __name__ == "__main__":
    var1 = "Hello World!"
    print("已更新字符串：", var1[:6] + "Runoob!")
