# -*- coding: UTF-8 -*-
# author: chenyongjun

if __name__ == "__main__":
    '''
    String（字符串）
    Python中的字符串用单引号'或双引号"括起来，同时使用反斜杠\转义特殊字符。
    字符串的截取的语法格式：
    变量[头下标:尾下标]
    索引值以0为开始值，-1为从末尾的开始位置。
    加号+是字符串的连接符， 星号*表示复制当前字符串，紧跟的数字为复制的次数。
    
     注意：
     1、Python没有单独的字符类型，一个字符就是长度为1的字符串。
     2、与C字符串不同的是，Python字符串不能被改变。向一个索引位置赋值，比如word[0] = "m"会导致错误。
    
    注意：
    1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
    2、字符串可以用+运算符连接在一起，用*运算符重复。
    3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
    4、Python中的字符串不能改变。
    '''
    str_a = 'Runoob'

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
    print(str_a + "TEST")
    # Python使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，
    # 可以在字符串前面添加一个r，表示原始字符串
    print('Ru\noob')
    print(r'Ru\noob')

    word = "Python"
    print(word[0], word[5])
    print(word[-1], word[-6])
    # TypeError: 'str' object does not support item assignment
    word[0] = "J"
