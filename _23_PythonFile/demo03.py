# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 File(文件) 方法
flush() 方法
描述：
    是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要是被动的等待输出缓冲区写入。
    一般情况下，文件关闭后会自动刷新缓冲区，但有时你需要在关闭前刷新它，这时就可以使用flush()方法。
语法：
    fileObject.flush()
    参数：
        无。
返回值：
    该方法没有返回值。
'''
if __name__ == "__main__":
    # 打开文件
    f = open("tmp/foo.txt", "w+")
    print("文件名为：", f.name)

    f.writelines("Welcome to Python!")
    # 刷新缓存区
    f.flush()

    # 关闭打开的文件
    f.close()
