# -*- coding: UTF-8 -*-
# author: chen_yong_jun
"""
当处理一个文件对象时, 使用 with 关键字是非常好的方式。在结束后, 它会帮你正确的关闭文件。 而且写起来也比 try - finally 语句块要简短
"""
with open("tmp/foo.txt", "a+") as f:
    f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")

print(f.closed)
