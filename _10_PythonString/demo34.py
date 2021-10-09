# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字符串
        Python3 replace()方法
            描述：
                replace()方法返回替换后的新字符串
            语法：
                str.replace(old, new[, max])
                参数：
                    old -- 将被替换的子字符串。
                    new -- 新字符串，用于替换old子字符串。
                    max -- 可选字符串, 替换不超过 max 次
            返回值：
                返回字符串中的 old（旧字符串）替换成new(新字符串)后生成的新字符串，如果指定第三个参数max，则替换不超过max次
"""
if __name__ == "__main__":
    str_a = "www.w3cschool.com"
    print("菜鸟教程旧地址：", str_a)
    print("菜鸟教程新地址：", str_a.replace("w3cschool.com", "runoob.com"))

    str_b = "this is string example....wow!!!"
    print(str_b.replace("is", "was", 3))
