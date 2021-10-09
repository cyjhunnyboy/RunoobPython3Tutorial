# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python3 endswith()方法
            描述：
                endswith()方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。
                可选参数"start"与"end"为检索字符串的开始与结束位置
            语法：
                str.endswith(suffix[, start[, end]])
            参数：
                suffix -- 该参数可以是一个字符串或者是一个元素。
                start -- 字符串中的开始位置。
                end -- 字符中结束位置
            返回值：
                如果字符串含有指定的后缀返回True，否则返回False
"""
if __name__ == "__main__":
    str_a = "Runoob example....wow!!!"
    suffix = "!!"
    print(str_a.endswith(suffix))
    print(str_a.endswith(suffix, 20))
    suffix = "run"
    print(str_a.endswith(suffix))
    print(str_a.endswith(suffix, 0, 19))
