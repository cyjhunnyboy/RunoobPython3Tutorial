# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python3 maketrans()方法
            描述：
                maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，
                第二个参数也是字符串表示转换的目标。两个字符串的长度必须相同，为一一对应的关系。
                注：Python3.4已经没有string.maketrans()了，取而代之的是内建函数: bytearray.maketrans()、bytes.maketrans()、str.maketrans()
            语法：
                str.maketrans(intab, outtab)
                参数：
                    intab -- 字符串中要替代的字符组成的字符串。
                    outtab -- 相应的映射字符的字符串
            返回值：
                返回字符串转换后生成的新字符串
"""
if __name__ == "__main__":
    intab = "aeiou"
    outtab = "12345"
    trantab = str.maketrans(intab, outtab)

    str_a = "this is string example....wow!!!"
    print(str_a.translate(trantab))
