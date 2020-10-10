# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python repr() 函数
描述：
    repr() 函数将对象转化为供解释器读取的形式
语法：
    repr(object)
    参数：
        object -- 对象
返回值：
    返回一个对象的 string 格式
'''
if __name__ == "__main__":
    str_1 = "RUNOOB"
    print(repr(str_1))
    list_1 = {"runoob", "runoob.com", "google", "google.com"}
    print(list_1)
