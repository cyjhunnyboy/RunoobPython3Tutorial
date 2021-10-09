# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python3 rindex()方法
            描述：
                rindex()返回子字符串str在字符串中最后出现的位置，如果没有匹配的字符串会报异常，你可以指定可选参数[beg:end]设置查找的区间
                类似于index()函数，不过是从右边开始查找
            语法：
                str.rindex(str, beg=0 end=len(string))
                参数：
                    str -- 查找的字符串
                    beg -- 开始查找的位置，默认为0
                    end -- 结束查找位置，默认为字符串的长度。
            返回值：
                返回子字符串str在字符串中最后出现的位置，如果没有匹配的字符串会报异常
"""
if __name__ == "__main__":
    str1 = "this is really a string example....wow!!!"
    str2 = "is"

    print(str1.rindex(str2))
    print(str1.rindex(str2, 10))
