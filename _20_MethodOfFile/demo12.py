# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 File(文件) 方法
truncate() 方法
描述：
    truncate()方法从文件的首行首字符开始截断，截断文件为size个字符，无size表示从当前位置截断；
    截断之后后面的所有字符被删除，其中Widnows系统下的换行代表2个字符大小
语法：
    fileObject.truncate([size])
    参数：
        size -- 可选，如果存在则文件截断为size字节。
返回值：
    该方法没有返回值。
'''
if __name__ == "__main__":
    # 打开文件
    f = open("tmp/temp.txt", "r+")
    print("文件名为：", f.name)

    line = f.readline()
    print("读取行：%s" % line)

    f.truncate()
    line = f.readlines()
    print("读取行: %s" % line)

    # 关闭文件
    f.close()
