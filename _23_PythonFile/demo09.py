# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 File(文件) 方法
readlines() 方法
描述：
    用于读取所有行(直到结束符EOF)并返回列表，该列表可以由Python的for... in ...结构进行处理。
    如果碰到结束符 EOF 则返回空字符串。
语法：
    fileObject.readlines()
    参数：
        无
返回值：
    返回列表，包含所有的行。
'''
if __name__ == "__main__":
    # 打开文件
    f = open("tmp/temp.txt", "r")
    print("文件名为：", f.name)

    # 依次读取每行
    for line in f.readlines():
        # 去掉每行头尾空白
        line = line.strip()
        print("读取的数据为：%s" % line)

    # 关闭文件
    f.close()
