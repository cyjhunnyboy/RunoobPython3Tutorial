# -*- coding: UTF-8 -*-
# author: chen_yong_jun

# 打开文件
f = open("tmp/foo.txt", "r")
print("文件名为：", f.name)

# isatty() 方法检测文件是否连接到一个终端设备，如果是返回 True，否则返回 False
res = f.isatty()
print("返回值：", res)

# 关闭文件
f.close()