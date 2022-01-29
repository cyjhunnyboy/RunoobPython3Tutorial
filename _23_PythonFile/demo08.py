# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 File(文件) 方法
readline() 方法
描述：
    用于从文件读取整行，包括"\n"字符。如果指定了一个非负数的参数，则返回指定大小的字节数，包括"\n"字符。
语法：
    fileObject.readline()
    参数：
        size -- 从文件中读取的字节数，
返回值：
    返回从字符串中读取的字节。
'''
if __name__ == "__main__":
    # 打开文件
    f = open("tmp/temp.txt", "r")
    print("文件名为：", f.name)

    line = f.readline()
    print("读取第一行 %s" % line)

    line = f.readline(5)
    print("读取的字符串为： %s" % line)

    # 关闭文件
    f.close()
