# -*- coding: UTF-8 -*-
# author: chenyongjun
"""
文件对象的方法
本节中剩下的例子假设已经创建了一个称为 f 的文件对象。

f.read()
为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。

size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。

以下实例假定文件 foo.txt 已存在（上面实例中已创建）
"""
# 打开一个文件
f = open("tmp/foo.txt", "r")

foo = f.read()
print(foo)

# 关闭打开的文件
f.close()
