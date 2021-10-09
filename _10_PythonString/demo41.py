# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python3 startswith()方法
            描述：
                startswith()方法用于检查字符串是否是以指定子字符串开头，如果是则返回True，否则返回False。
                如果参数beg和end指定值，则在指定范围内检查
            语法：
                str.startswith(str, beg=0,end=len(string))
            参数：
                str -- 检测的字符串。
                strbeg -- 可选参数用于设置字符串检测的起始位置。
                strend -- 可选参数用于设置字符串检测的结束位置
            返回值：
                如果检测到字符串则返回True，否则返回False
"""
if __name__ == "__main__":
    str_a = "this is string example....wow!!!"
    print(str_a.startswith('this'))
    print(str_a.startswith('string', 8))
    print(str_a.startswith('this', 2, 4))
