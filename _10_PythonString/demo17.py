# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python3 index()方法
            描述：
                index()方法检测字符串中是否包含子字符串str ，如果指定beg（开始）和end（结束）范围，则检查是否包含在指定范围内，
                该方法与Python find()方法一样，只不过如果str不在string中会报一个异常
            语法：
                str.index(str, beg=0, end=len(string))
                参数：
                    str -- 指定检索的字符串
                    beg -- 开始索引，默认为0。
                    end -- 结束索引，默认为字符串的长度
            返回值：
                如果包含子字符串返回开始的索引值，否则抛出异常
"""
if __name__ == "__main__":
    str1 = "Runoob example....wow!!!"
    str2 = "exam"

    print(str1.index(str2))
    print(str1.index(str2, 5))
    # 找不到子字符串，抛出异常
    # ValueError: substring not found
    print(str1.index(str2, 10))
