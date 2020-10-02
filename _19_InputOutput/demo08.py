# -*- coding: UTF-8 -*-
# author: chenyongjun
"""
f.readlines()
f.readlines() 将返回该文件中包含的所有行。

如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割
"""
# 打开一个文件
f = open("tmp/foo.txt", "r")

foos = f.readlines()
print(foos)
for foo in foos:
    print(foo)

# 关闭打开的文件
f.close()
