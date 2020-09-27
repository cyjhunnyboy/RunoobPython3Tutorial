# -*- coding: UTF-8 -*-
# author: chen_yong_jun

# 打开文件
fo = open("tmp/temp.txt", "r+")
print("文件名为: ", fo.name)

# 截取10个字节
fo.truncate(10)

foo = fo.read()
print("读取数据: %s" % foo)

# 关闭文件
fo.close()
