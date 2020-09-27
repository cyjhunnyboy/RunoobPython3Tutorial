# -*- coding: UTF-8 -*-
# author: chen_yong_jun
# 如果要写入一些不是字符串的东西, 那么将需要先进行转换

# 打开一个文件
f = open("tmp/foo.txt", "w")

value = ('www.runoob.com', 14)
s = str(value)
print(s)
f.write(s)

# 关闭打开的文件
f.close()
