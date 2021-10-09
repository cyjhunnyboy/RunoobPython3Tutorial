# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python3 rfind()方法
            描述：
                rfind()返回字符串最后一次出现的位置，如果没有匹配项则返回-1，类似于find()函数，不过是从右边开始查找
            语法：
                str.rfind(str, beg=0 end=len(string))
                参数：
                    str -- 查找的字符串
                    beg -- 开始查找的位置，默认为0
                    end -- 结束查找位置，默认为字符串的长度。
            返回值：
                返回字符串最后一次出现的位置，如果没有匹配项则返回-1
"""
if __name__ == "__main__":
    str1 = "this is really a string example....wow!!!"
    str2 = "is"

    print(str1.rfind(str2))

    print(str1.rfind(str2, 0, 10))
    print(str1.rfind(str2, 10, 0))

    print(str1.find(str2))
    print(str1.find(str2, 0, 10))
    print(str1.find(str2, 10, 0))
