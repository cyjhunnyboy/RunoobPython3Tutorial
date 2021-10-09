# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python3 isnumeric()方法
            描述：
                isnumeric()方法检测字符串是否只由数字组成。数字可以是： Unicode 数字，全角数字（双字节），罗马数字，汉字数字
                指数类似²与分数类似½也属于数字
                注：定义一个字符串为Unicode，只需要在字符串前添加'u'前缀即可
            语法：
                str.isnumeric()
                参数：
                    无
            返回值：
                如果字符串中只包含数字字符，则返回True，否则返回False
"""
if __name__ == "__main__":
    str1 = u"runoob2016"
    print(str1.isnumeric())

    str2 = "23443434"
    print(str2.isnumeric())

    # s = "²3455"
    s = "\u00B23455"
    print(s.isnumeric())

    # s = "½"
    s = "\u00BD"
    print(s.isnumeric())

    # unicode for 0
    a = "\u0030"
    print(a.isnumeric())

    # unicode for ²
    b = "\u00B2"
    print(b.isnumeric())

    c = "10km2"
    print(c.isnumeric())
