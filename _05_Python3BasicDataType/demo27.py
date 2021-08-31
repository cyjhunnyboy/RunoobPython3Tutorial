# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
    Python数据类型转换
        Python repr()函数
            描述：
                repr()函数将对象转化为供解释器读取的形式
            语法：
                repr(object)
                参数：
                    object -- 对象
            返回值：
                返回一个对象的string格式
'''
if __name__ == "__main__":
    s = "RUNOOB"
    print(repr(s))
    dict_a = {"runoob": "runoob.com", "google": "google.com"}
    print(repr(dict_a))
