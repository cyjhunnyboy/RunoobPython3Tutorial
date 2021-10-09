# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python字符串运算符
            下表实例变量a值为字符串"Hello"，b变量值为"Python"：
            操作符	  描述	                                                实例
            +	      字符串连接	                                            a+b输出结果：HelloPython
            *	      重复输出字符串	                                        a*2输出结果：HelloHello
            []	      通过索引获取字符串中字符	                                a[1]输出结果：e
            [:]	      截取字符串中的一部分	                                    a[1:4]输出结果：ell
            in	      成员运算符 - 如果字符串中包含给定的字符返回True	            'H' in a输出结果1
            not in	  成员运算符 - 如果字符串中不包含给定的字符返回 True	        'M' not in a输出结果1
            r/R	      原始字符串 - 原始字符串：所有的字符串都是直接按照字面        print( r'\n' )
                      的意思来使用，没有转义特殊或不能打印的字符。原始字符串        print( R'\n' )
                      除在字符串的第一个引号前加上字母 r（可以大小写）以外，
                      与普通字符串有着几乎完全相同的语法。
            %	      格式字符串	                                            请看下一节内容。
"""
if __name__ == "__main__":
    a = "Hello"
    b = "Python"

    print("a+b输出结果：", a + b)
    print("a*2输出结果：", a * 2)
    print("a[1]输出结果：", a[1])
    print("a[1:4]输出结果：", a[1:4])

    if "H" in a:
        print("H在变量a中")
    else:
        print("H不在变量a中")

    if "M" not in a:
        print("M不在变量a中")
    else:
        print("M在变量a中")

    print(r'\n')
    print(R'\n')
