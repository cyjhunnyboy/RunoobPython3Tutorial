# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 判断字符串是否存在子字符串
    给定一个字符串，然后判断指定的子字符串是否存在于该字符串中。
'''


def check(main_str, sub_str):
    """给定一个字符串，然后判断指定的子字符串是否存在于该字符串中。"""

    if (main_str.find(sub_str) == 1):
        print("不存在！")
    else:
        print("存在！")


if __name__ == "__main__":
    main_str = "www.runoob.com"
    sub_str = "runoob"
    check(main_str, sub_str)
