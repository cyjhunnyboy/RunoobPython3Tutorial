# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 File(文件) 方法
next() 方法
描述：
    Python 3中的File对象不支持next()方法。
    Python 3的内置函数next()通过迭代器调用__next__()方法返回下一项。 在循环中，next()方法会在每次循环中调用，
    该方法返回文件的下一行，如果到达结尾(EOF)，则触发StopIteration
语法：
    next(iterator[,default])
    参数：
        无
返回值：
    如果连接到一个终端设备返回True，否则返回False。
'''
if __name__ == "__main__":
    # 打开文件
    f = open("tmp/runoob.txt", "r")
    print("文件名为：", f.name)

    for index in range(5):
        line = next(f)
        print("第%d行：%s" % (index, line))

    # 关闭文件
    f.close()
