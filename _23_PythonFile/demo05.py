# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 File(文件) 方法
isatty() 方法
描述：
    isatty()方法检测文件是否连接到一个终端设备，如果是返回True，否则返回False。
语法：
    fileObject.isatty()
    参数：
        无
返回值：
    如果连接到一个终端设备返回True，否则返回False。
'''
if __name__ == "__main__":
    # 打开文件
    f = open("tmp/foo.txt", "r")
    print("文件名为：", f.name)

    # 检测文件是否连接到一个终端设备
    res = f.isatty()
    print("返回值：", res)

    # 关闭文件
    f.close()
