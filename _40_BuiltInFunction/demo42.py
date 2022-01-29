# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python print() 函数
描述：
    print() 方法用于打印输出，最常见的一个函数
    在 Python3.3 版增加了 flush 关键字参数
    print 在 Python3.x 是一个函数，但在 Python2.x 版本不是一个函数，只是一个关键字
语法：
    print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
    参数：
        objects -- 复数，表示可以一次输出多个对象。输出多个对象时，需要用 , 分隔
        sep -- 用来间隔多个对象，默认值是一个空格
        end -- 用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符串
        file -- 要写入的文件对象
        flush -- 输出是否被缓存通常决定于 file，但如果 flush 关键字参数为 True，流会被强制刷新
返回值：
    无
'''
if __name__ == "__main__":
    print(1)
    print("Hello World")

    a = 1
    b = "runoob"
    print(a, b)

    print("aaa""bbb")
    print("aaa", "bbb")

    # 设置间隔符
    print("www", "runoob", "com", sep=".")
