# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python3 rstrip()方法
            描述：
                rstrip()删除string字符串末尾的指定字符（默认为空格）
            语法：
                str.rstrip([chars])
                参数：
                    chars -- 指定删除的字符（默认为空格）
            返回值：
                返回删除string字符串末尾的指定字符后生成的新字符串
"""
if __name__ == "__main__":
    str_a = "     this is string example....wow!!!     "

    # 右对齐，字符串左边填充空格
    print(str_a.rstrip())
    # 左对齐，字符串右边填充空格
    print(str_a.lstrip())
    # 去掉字符串左右两边的空格
    print(str_a.strip())

    print("===============================")

    str_b = "*****this is string example....wow!!!*****"
    # 右对齐，字符串左边填充“*”
    print(str_b.rstrip("*"))
    # 左对齐，字符串右边填充“*”
    print(str_b.lstrip("*"))
    # 去掉字符串左右两边的空格
    print(str_b.strip("*"))
