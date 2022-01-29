# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 File(文件) 方法
writelines() 方法
描述：
    writelines()方法用于向文件中写入一序列的字符串。
    这一序列字符串可以是由迭代对象产生的，如一个字符串列表。
    换行需要制定换行符\n。
语法：
    fileObject.writelines([str])
    参数：
        str -- 要写入文件的字符串序列。
返回值：
    该方法没有返回值。
'''
if __name__ == "__main__":
    # 打开文件
    fo = open("tmp/test.txt", "w")
    print("文件名为: ", fo.name)

    seq = ["菜鸟教程 1\n", "菜鸟教程 2"]
    fo.writelines(seq)

    # 关闭文件
    fo.close()
