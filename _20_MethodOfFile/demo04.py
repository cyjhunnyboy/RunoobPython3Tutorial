# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 File(文件) 方法
fileno() 方法
描述：
    返回一个整型的文件描述符(file descriptor FD整型)，可用于底层操作系统的I/O操作
语法：
    fileObject.fileno()
    参数：
        无
返回值：
    返回文件描述符。
'''
if __name__ == "__main__":
    # 打开文件
    f = open("tmp/foo.txt", "r")
    print("文件名为：", f.name)

    # 获取文件描述符
    f_id = f.fileno()
    print("文件描述符为：", f_id)

    # 关闭文件
    f.close()
