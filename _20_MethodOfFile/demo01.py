# -*- coding: UTF-8 -*-
# author: chen_yong_jun

# 打开文件
f = open("tmp/foo.txt", "wb")
print("文件名为: ", f.name)

"""
close() 方法用于关闭一个已打开的文件。关闭后的文件不能再进行读写操作， 否则会触发 ValueError 错误。 close() 方法允许调用多次。
当 file 对象，被引用到操作另外一个文件时，Python 会自动关闭之前的 file 对象。 使用 close() 方法关闭文件是一个好的习惯。
"""
# 关闭文件
f.close()
