# -*- coding: UTF-8 -*-
# author: chen_yong_jun

# 打开文件
f = open("tmp/foo.txt", "w+")
print("文件名为：", f.name)
f.writelines("Welcome to Python!")

"""
flush() 方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要是被动的等待输出缓冲区写入。
一般情况下，文件关闭后会自动刷新缓冲区，但有时你需要在关闭前刷新它，这时就可以使用 flush() 方法。
"""
# 刷新缓存区
f.flush()

f.close()
