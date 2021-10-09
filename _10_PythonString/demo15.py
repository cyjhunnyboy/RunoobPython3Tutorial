# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python3 expandtabs()方法
            描述：
                expandtabs()方法把字符串中的 ab符号('\t')转为空格，tab符号('\t')默认的空格数是8
            语法：
                str.expandtabs(tabsize=8)
                参数：
                    tabsize -- 指定转换字符串中的 tb符号('\t')转为空格的字符数
            返回值：
                该方法返回字符串中的tab符号('\t')转为空格后生成的新字符串
"""
if __name__ == "__main__":
    str_a = "runoob\t12345\tabc"
    print("原始字符串：" + str_a)

    # 默认8个空格
    # runnob有6个字符，后面的\t填充2个空格
    # 12345有5个字符，后面的\ 填充3个空格
    print("替换\\t符号：" + str_a.expandtabs())

    # 2个空格
    # runnob有6个字符，刚好是2的3倍，后面的\t填充2个空格
    # 12345有5个字符，不是2的倍数，后面的\t填充1个空格
    print("使用2个空格替换\\t符号:", str.expandtabs(2))

    # 3个空格
    print("使用3个空格:", str.expandtabs(3))

    # 4个空格
    print("使用4个空格:", str.expandtabs(4))

    # 5个空格
    print("使用5个空格:", str.expandtabs(5))

    # 6个空格
    print("使用6个空格:", str.expandtabs(6))
