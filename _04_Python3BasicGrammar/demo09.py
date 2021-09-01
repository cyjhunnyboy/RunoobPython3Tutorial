# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 基础语法
        2、字符串(String)
            转义符 '\'
            反斜杠可以用来转义，使用r可以让反斜杠不发生转义。 如 r"this is a line with\n" 则\n会显示，并不是换行。
            按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
"""
if __name__ == "__main__":
    # 转义符"\"，反斜杠可以用来转义，"\n"表示换行
    str_1 = "this is a line with \n"
    print(str_1)

    # 使用r可以让反斜杠不发生转义，"\n"并不换行，直接输出"\n"
    str_2 = r"this is a line with \n"
    print(str_2)
