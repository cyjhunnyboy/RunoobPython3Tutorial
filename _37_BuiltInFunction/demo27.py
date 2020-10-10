# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python str() 函数
描述：
    str() 函数将对象转化为适于人阅读的形式
语法：
    class str(object='')
    参数：
        object -- 对象
返回值：
    返回一个对象的string格式
'''
if __name__ == "__main__":
    s = "RUNOOB"
    print(str(s))
    dict1 = {'runoob': 'runoob.com', 'google': 'google.com'}
    print(str(dict1))
