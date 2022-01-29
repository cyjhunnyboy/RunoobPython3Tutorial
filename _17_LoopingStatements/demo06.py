# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 循环语句
        Python中的循环语句有for和while

        for语句
            Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
            for循环的一般格式如下：
                for <variable> in <sequence>:
                    <statements>
                else:
                    <statements>
"""
if __name__ == "__main__":
    languages = ["C", "C++", "Perl", "Python"]
    for language in languages:
        print(language)
