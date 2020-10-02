# -*- coding: UTF-8 -*-
# author: chenyongjun
"""
truncate() 从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后后面的所有字符被删除，
其中 Widnows 系统下的换行代表2个字符大小
truncate() 方法语法如下：
fileObject.truncate( [ size ])
size -- 可选，如果存在则文件截断为 size 字节。
"""
# 打开文件
f = open("tmp/temp.txt", "r+")
print("文件名为：", f.name)

line = f.readline()
print("读取行：%s" % line)

f.truncate()
line = f.readlines()
print("读取行: %s" % line)

# 关闭文件
f.close()
