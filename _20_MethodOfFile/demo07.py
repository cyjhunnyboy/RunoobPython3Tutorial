# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 File(文件) 方法
read() 方法
描述：
    read()方法用于从文件读取指定的字节数，如果未给定或为负则读取所有。
语法：
    fileObject.read([size])
    参数：
        size -- 从文件中读取的字节数，默认为-1，表示读取整个文件。
返回值：
    返回从字符串中读取的字节。
'''
if __name__ == "__main__":
    # 打开文件
    f = open("tmp/runoob.txt", "r")
    print("文件名为：", f.name)

    # 从文件读取指定的字节数，如果未给定或为负则读取所有。
    line = f.read(22)
    print("读取的字符串：%s" % line)

    # 关闭文件
    f.close()
