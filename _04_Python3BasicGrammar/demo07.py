# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
    Python3 基础语法
        1、数字(Number)类型
            Python中数字有四种类型：整数、布尔型、浮点数和复数。
            int(整数), 如1, 只有一种整数类型int，表示为长整型，没有Python2中的Long。
            bool(布尔), 如 True。
            float(浮点数), 如 1.23、3E-2
            complex(复数), 如 1 + 2j、 1.1 + 2.2j

        2、字符串(String)
            Python中单引号和双引号使用完全相同。
            使用三引号(单三引号或双三引号)可以指定一个多行字符串。
            转义符 '\'
            反斜杠可以用来转义，使用r可以让反斜杠不发生转义。 如 r"this is a line with\n" 则\n会显示，并不是换行。
            按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
            字符串可以用+运算符连接在一起，用*运算符重复。
            Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
            Python中的字符串不能改变。
            Python没有单独的字符类型，一个字符就是长度为1的字符串。
            字符串的截取的语法格式如下：变量[头下标:尾下标]
'''
if __name__ == "__main__":
    print(r"this is a line with \n")

    word = "字符串"
    sentence = "这是一个句子。"
    paragraph = """这是一个段落，可以由多行组成"""
    print(word)
    print(sentence)
    print(paragraph)
    print('---------------')

    str_a = "Runoob"
    # 输出字符串
    print(str_a)
    # 输出第一个到倒数第二个的所有字符
    print(str_a[0:-1])
    # 输出字符串第一个字符
    print(str_a[0])
    # 输出从第三个开始到第五个的字符
    print(str_a[2:5])
    # 输出从第三个开始的后的所有字符
    print(str_a[2:])
    # 输出字符串两次
    print(str_a * 2)
    # 连接字符串
    print(str_a + "你好")
    print('---------------')

    # 使用反斜杠(\)+n转义特殊字符
    print("hello\nrunoob")
    # 在字符串前面添加一个r，表示原始字符串，不会发生转义
    print(r"hello\nrunoob")
