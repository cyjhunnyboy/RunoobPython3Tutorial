# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python3 title()方法
            描述：
                title()方法返回"标题化"的字符串，就是说所有单词的首个字母转化为大写，其余字母均为小写(见istitle())
            语法：
                str.title()
                参数：
                    NA
            返回值：
                返回"标题化"的字符串，就是说所有单词的首字母都转化为大写
"""
if __name__ == "__main__":
    str1 = "this is string example from runoob....wow!!!"
    print(str1.title())

    str2 = "This Is String Example....WOW!!!"
    print(str2.title())

    txt = "hello b2b2b2 and 3g3g3g"
    x = txt.title()
    print(x)
