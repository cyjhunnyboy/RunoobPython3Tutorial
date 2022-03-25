# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 基础语法
        2、字符串(String)
            字符串可以用+运算符连接在一起，用*运算符重复。
            Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
            Python中的字符串不能改变。
            Python没有单独的字符类型，一个字符就是长度为1的字符串。
            字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
"""
if __name__ == "__main__":
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
    # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
    print(str_a[1:5:2])
    # 输出字符串两次
    print(str_a * 2)
    # 连接字符串
    print(str_a + "你好")

