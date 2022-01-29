# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 File(文件) 方法
close() 方法
描述：
    close()方法用于关闭一个已打开的文件。关闭后的文件不能再进行读写操作， 否则会触发ValueError错误。 close()方法允许调用多次。
    当file对象，被引用到操作另外一个文件时，Python会自动关闭之前的file对象。 使用close()方法关闭文件是一个好的习惯。
语法：
    fileObject.close()
    参数：
        无
返回值：
    该方法没有返回值。
'''
if __name__ == "__main__":
    # 打开文件
    f = open("tmp/runoob.txt", "r")
    print("文件名为: ", f.name)

    # 读取文件
    foo = f.read()
    print(foo)

    # 关闭打开的文件
    f.close()
