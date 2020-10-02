# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
readlines() 方法用于读取所有行(直到结束符 EOF)并返回列表，该列表可以由 Python 的 for... in ... 结构进行处理。
如果碰到结束符 EOF 则返回空字符串。
如果碰到结束符 EOF 则返回空字符串
"""
# 打开文件
f = open("tmp/temp.txt", "r")
print("文件名为：", f.name)

for line in f.readlines():
    line = line.strip()
    print("读取的数据为：%s" % line)

# 关闭文件
f.close()
