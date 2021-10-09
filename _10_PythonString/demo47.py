# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python3 zfill()方法
            描述：
                zfill()方法返回指定长度的字符串，原字符串右对齐，前面填充0
            语法：
                str.zfill(width)
                参数：
                    width -- 指定字符串的长度。原字符串右对齐，前面填充0
            返回值：
                返回指定长度的字符串
"""
if __name__ == "__main__":
    str_a = "this is string example from runoob....wow!!!"
    print("str_a.zfill : ", str_a.zfill(40))
    print("str_a.zfill : ", str_a.zfill(50))
