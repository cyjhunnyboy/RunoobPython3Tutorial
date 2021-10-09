# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python 访问字符串中的值
            Python不支持单字符类型，单字符在Python中也是作为一个字符串使用。
            Python访问子字符串，可以使用方括号来截取字符串，字符串的截取的语法格式如下：
                变量[头下标:尾下标]
            索引值以0为开始值，-1为从末尾的开始位置。

            从后面索引：      -6  -5  -4  -3  -2  -1
            从前面索引：       0   1   2   3   4   5
            字符串：          R   u   n   o   o   b
            从前面截取：      :1   2   3   4   5:
            从后面截取：     :-5  -4  -3  -2  -1:

            str = "RUNOOB"
            字符串：    R   U   N   O   O   B
            索引：     0   1   2   3   4   5
            str[0]="R"          str[:]="RUNOOB"
            str[1]="U"          str[0:]="RUNOOB"
            str[2]="N"          str[:6]="RUNOOB"
            str[3]="O"          str[:3]="RUN"
            str[4]="O"          str[0:2]="RU"
            str[5]="B"          str[1:4]="UNO"
"""
if __name__ == "__main__":
    var1 = "Hello World!"
    var2 = "Runoob"
    print("var1[0]: ", var1[0])
    print("var2[1:5]: ", var2[1:5])
