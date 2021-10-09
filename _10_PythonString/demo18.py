# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python3 isalnum()方法
            描述：
                isalnum()方法检测字符串是否由字母和数字组成
            语法：
                str.isalnum()
                参数：
                    无
            返回值：
                如果string至少有一个字符并且所有字符都是字母或数字则返回True，否则返回False
"""
if __name__ == "__main__":
    # 字符串没有空格
    str1 = "runoob2016"
    print(str1.isalnum())

    str2 = "www.runoob.com"
    print(str2.isalnum())
