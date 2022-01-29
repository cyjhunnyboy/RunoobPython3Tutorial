# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 字符串大小写转换
    将字符串转换为大写字母，或者将字符串转为小写字母
'''
if __name__ == "__main__":
    str = "www.runoob.com"

    # 把所有字符中的小写字母转换成大写字母
    print(str.upper())
    # 把所有字符中的大写字母转换成小写字母
    print(str.lower())
    # 把第一个字母转化为大写字母，其余小写
    print(str.capitalize())
    # 把每个单词的第一个字母转化为大写，其余小写
    print(str.title())
