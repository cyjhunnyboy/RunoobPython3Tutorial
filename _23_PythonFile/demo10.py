# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 File(文件) 方法
seek() 方法
描述：
    seek()方法用于移动文件读取指针到指定位置。
语法：
    fileObject.seek(offset[, whence])
    参数：
        offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
        whence：可选，默认值为0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，
                1代表从当前位置开始算起，2代表从文件末尾算起。
返回值：
    如果操作成功，则返回新的文件位置，如果操作失败，则函数返回-1。
'''
if __name__ == "__main__":
    # 打开文件
    f = open("tmp/temp.txt", "r+")
    print("文件名为：", f.name)

    line = f.readline()
    print("读取的数据为：%s" % line)

    # 重新设置文件读取指针到开头
    f.seek(0, 0)
    line = f.readline()
    print("读取的数据为：%s" % line)

    # 关闭文件
    f.close()
