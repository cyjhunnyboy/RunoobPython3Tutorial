# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python3 isalpha()方法
            描述：
                isalpha()方法检测字符串是否只由字母组成
            语法：
                str.isalpha()
                参数：
                    无
            返回值：
                如果字符串至少有一个字符并且所有字符都是字母则返回True，否则返回False
"""
if __name__ == "__main__":
    # 字母
    str_1 = "runoob"
    print(str_1.isalpha())

    # 字母和中文文字
    str_2 = "runoob菜鸟教程"
    print(str_2.isalpha())

    # 字母和特殊字符
    str_3 = "Runoob example....wow!!!"
    print(str_3.isalpha())

    # 中文
    str_4 = "中国人"
    print(str_4.isalpha())
