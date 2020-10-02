# -*- coding: UTF-8 -*-
# author: chenyongjun

# 打开文件
f = open("tmp/temp.txt", "r")
print("文件名为：", f.name)

# readline() 方法用于从文件读取整行，包括 "\n" 字符。如果指定了一个非负数的参数，则返回指定大小的字节数，包括 "\n" 字符。
line = f.readline()
print("读取第一行 %s" % line)

line = f.readline(5)
print("读取的字符串为： %s" % line)

# 关闭文件
f.close()
