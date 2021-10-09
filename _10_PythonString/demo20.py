# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python3 isdigit()方法
            描述：
                isdigit()方法检测字符串是否只由数字组成
            语法：
                str.isdigit()
                参数：
                    无
            返回值：
                如果字符串只包含数字则返回True，否则返回False
"""
if __name__ == "__main__":
    # 数字字符
    str1 = "123456"
    print(str1.isdigit())

    # 字母和特殊字符
    str2 = "Runoob example....wow!!!"
    print(str2.isdigit())
