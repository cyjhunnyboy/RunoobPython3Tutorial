# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python3 count()方法
            描述：
                count()方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置
            语法：
                str.count(sub, start= 0,end=len(string)
                参数：
                    sub -- 搜索的子字符串
                    start -- 字符串开始搜索的位置。默认为第一个字符，第一个字符索引值为0。
                    end -- 字符串中结束搜索的位置。字符中第一个字符的索引为0。默认为字符串的最后一个位置
            返回值：
                该方法返回子字符串在字符串中出现的次数
"""
if __name__ == "__main__":
    str_a = "www.runoob.com"
    sub = 'o'
    print("str.count('o') : ", str_a.count(sub))

    sub = "run"
    print("str.count('run', 0, 10) : ", str_a.count(sub, 0, 10))
