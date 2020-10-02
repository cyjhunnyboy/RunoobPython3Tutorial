# -*- coding: UTF-8 -*-
# author: chenyongjun

with open("tmp/foo.txt", "r+") as f:
    s = f.read()
    print(s, end="")
    f.write("My name is Jack!\n")

