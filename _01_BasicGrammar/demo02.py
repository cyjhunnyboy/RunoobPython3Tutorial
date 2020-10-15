# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
    关键字（Python保留字）
    Python的标准库提供了一个keyword模块，可以输出当前版本的所有关键字

        [
            "False", "None", "True", "and", "as", "assert", "async", "await", "break", "class", "continue",
            "def", "del", "elif", "else", "except", "finally", "for", "from", "global", "if", "import", "in",
            "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"
        ]
'''
import keyword

if __name__ == "__main__":
    print(keyword.kwlist)
