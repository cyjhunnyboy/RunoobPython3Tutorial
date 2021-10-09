# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python3 islower()方法
            描述：
                islower()方法检测字符串是否由小写字母组成
            语法：
                str.islower()
                参数：
                    无
            返回值：
                如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回True，否则返回False
"""
if __name__ == "__main__":
    str1 = "RUNOOB example....wow!!!"
    print(str1.islower())

    str2 = "runoob  example....wow!!!"
    print(str2.islower())
