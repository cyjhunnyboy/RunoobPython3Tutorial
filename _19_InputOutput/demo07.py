# -*- coding: UTF-8 -*-
# author: chen_yong_jun
"""
f.readline()
f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行
"""
# 打开一个文件
f = open("tmp/foo.txt", "r")

foo = f.readline()
print(foo)

# 关闭打开的文件
f.close()
