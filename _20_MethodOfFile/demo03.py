# -*- coding: UTF-8 -*-
# author: chenyongjun

# 打开文件
f = open("tmp/foo.txt", "r")
print("文件名为：", f.name)

# fileno() 方法返回一个整型的文件描述符(file descriptor FD 整型)，可用于底层操作系统的 I/O 操作
f_id = f.fileno()
print("文件描述符为：", f_id)

# 关闭文件
f.close()
