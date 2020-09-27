# -*- coding: UTF-8 -*-
# author: chen_yong_jun
"""
writelines() 方法用于向文件中写入一序列的字符串。

这一序列字符串可以是由迭代对象产生的，如一个字符串列表。

换行需要制定换行符 \n。
writelines() 方法语法如下：
fileObject.writelines( [ str ])
str -- 要写入文件的字符串序列。
"""
# 打开文件
fo = open("tmp/test.txt", "w")
print("文件名为: ", fo.name)

seq = ["菜鸟教程 1\n", "菜鸟教程 2"]
fo.writelines(seq)

# 关闭文件
fo.close()
