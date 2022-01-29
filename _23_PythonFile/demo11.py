# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 File(文件) 方法
tell() 方法
描述：
    tell()方法返回文件的当前位置，即文件指针当前位置。
语法：
    fileObject.tell()
    参数：
        无
返回值：
    返回文件的当前位置。
'''
if __name__ == "__main__":
    # 打开文件
    f = open("tmp/temp.txt", "r+")
    print("文件名为：", f.name)

    line = f.readline()
    print("读取的数据为：%s" % line)

    # 获取当前文件位置
    position = f.tell()
    print("当前位置：%d" % position)

    # 关闭文件
    f.close()
