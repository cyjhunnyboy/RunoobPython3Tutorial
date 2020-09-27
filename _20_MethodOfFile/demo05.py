# -*- coding: UTF-8 -*-
# author: chen_yong_jun

# 打开文件
f = open("tmp/runoob.txt", "r")
print("文件名为：", f.name)

# read() 方法用于从文件读取指定的字节数，如果未给定或为负则读取所有
line = f.read(22)
print("读取的字符串：%s" % line)

# 关闭文件
f.close()
