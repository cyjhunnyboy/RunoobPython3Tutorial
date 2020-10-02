# -*- coding: UTF-8 -*-
# author: chenyongjun
# 另一种方式是迭代一个文件对象然后读取每行

# 打开一个文件
f = open("tmp/foo.txt", "r")

for line in f:
    print(line, end="")

# 关闭打开的文件
f.close()
