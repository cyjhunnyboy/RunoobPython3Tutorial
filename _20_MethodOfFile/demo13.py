# -*- coding: UTF-8 -*-
# author: chen_yong_jun
"""
write() 方法用于向文件中写入指定字符串。

在文件关闭前或缓冲区刷新前，字符串内容存储在缓冲区中，这时你在文件中是看不到写入的内容的。

如果文件打开模式带 b，那写入文件内容时，str (参数)要用 encode 方法转为 bytes 形式，
否则报错：TypeError: a bytes-like object is required, not 'str
语法：fileObject.write( [ str ])
str -- 要写入文件的字符串。
"""
# 打开文件
fo = open("tmp/temp.txt", "r+")
print("文件名: ", fo.name)

s = "6:www.runoob.com"
# 在文件末尾写入一行
fo.seek(0, 2)
line = fo.write(s)

# 读取文件所有内容
fo.seek(0, 0)
for index in range(6):
    line = next(fo)
    print("文件行号 %d - %s" % (index, line))

# 关闭文件
fo.close()

