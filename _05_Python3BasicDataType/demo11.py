# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 基本数据类型
        1、String（字符串）
            注意：
            1、Python没有单独的字符类型，一个字符就是长度为1的字符串。
            2、与C字符串不同的是，Python字符串不能被改变。向一个索引位置赋值，比如word[0] = "m"会导致错误。

            注意：
            1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
            2、字符串可以用+运算符连接在一起，用*运算符重复。
            3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
            4、Python中的字符串不能改变。
"""
if __name__ == "__main__":
    # Python使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，
    # 可以在字符串前面添加一个r，表示原始字符串
    print('Ru\noob')
    print(r'Ru\noob')

    word = "Python"
    print(word[0], word[5])
    print(word[-1], word[-6])
    # TypeError: 'str' object does not support item assignment
    word[0] = "J"
