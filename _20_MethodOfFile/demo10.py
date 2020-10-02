# -*- coding: UTF-8 -*-
# author: chenyongjun
"""
tell() 方法返回文件的当前位置，即文件指针当前位置
tell() 方法语法如下：
fileObject.tell()
"""
# 打开文件
f = open("tmp/temp.txt", "r+")
print("文件名为：", f.name)

line = f.readline()
print("读取的数据为：%s" % line)

# 获取当前文件位置
position = f.tell()
print("当前位置：%d" % position)

# 关闭文件
f.close()
