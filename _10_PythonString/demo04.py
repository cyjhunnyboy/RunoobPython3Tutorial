# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python 转义字符
            在需要在字符串中使用特殊字符时，python用反斜杠'\'转义字符，如下表：
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
            \oyy           八进制数，yy代表的字符，例如：'\o12'代表换行，其中o是字母，不是数字0
            \other         其它的字符以普通格式输出
"""
if __name__ == "__main__":
    # \(在行尾时)，续行符
    print("line1 \
    ... line2 \
    ... line3")


    # \\反斜杠符号
    print("\\")

    # \'单引号
    print("\'")

    # \"双引号
    print("\"")

    # \a响铃，执行后电脑有响声。
    # print("\a")

    # \b退格（backspace)
    print("Hello \b World!")

    # \000空
    print("\000")

    # \n换行
    print("\n")

    # \v纵向制表符
    print("Hello \v World!")

    # \t横向制表符
    print("Hello \t World!")

    # \r回车，将\r后面的内容移到字符串开头，并逐一替换开头部分的字符，
    # 直至将\r后面的内容完全替换完成
    print("Hello\rWorld!")
    print("google runoob taobao\r123456")

    # \f换页
    print("Hello \f World!")

    # \yyy八进制数，y代表0~7的字符，例如：\012代表换行
    print("\110\145\154\154\157\40\127\157\162\154\144\41")

    # \xyy十六进制数，以\x开头，y代表的字符，例如：\x0a代表换行
    print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")
