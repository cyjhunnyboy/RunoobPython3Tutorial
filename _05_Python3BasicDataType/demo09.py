# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
    Python3 基本数据类型
        1、String（字符串）
            Python中的字符串用单引号'或双引号"括起来，同时使用反斜杠\转义特殊字符。
            字符串的截取的语法格式：
                变量[头下标:尾下标]
                索引值以0为开始值，-1为从末尾的开始位置。

            从后面索引：     -6 -5 -4 -3 -2 -1
            从前面索引：      0  1  2  3  4  5
                            R  u  n  o  o  b
            从前面截取：    ：1  2  3  4  5  ：
            从后面截取：    ：-5 -4 -3 -2 -1 ：
'''
if __name__ == "__main__":
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