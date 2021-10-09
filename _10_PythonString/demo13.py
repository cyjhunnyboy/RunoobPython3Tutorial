# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python3 encode()方法
            描述：
                encode()方法以指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案
            语法：
                str.encode(encoding='UTF-8', errors='strict')
                参数：
                    encoding -- 要使用的编码，如"UTF-8"。
                    errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。
                              其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace'
                              以及通过 codecs.register_error()注册的任何值
            返回值：
                该方法返回编码后的字符串，它是一个bytes对象
"""
if __name__ == "__main__":
    str_r = "菜鸟教程"
    str_utf8 = str_r.encode("UTF-8")
    str_gbk = str_r.encode("GBK")

    print(str_r)

    print("UTF-8 编码：", str_utf8)
    print("GBK 编码：", str_gbk)

    print("UTF-8 解码：", str_utf8.decode("UTF-8", "strict"))
    print("GBK 解码：", str_gbk.decode("GBK", "strict"))
