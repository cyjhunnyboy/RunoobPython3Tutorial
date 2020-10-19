# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 字典
    访问字典里的值，把相应的键放入到方括号中
'''
if __name__ == "__main__":
    dict_b = {"Name": "Runoob", "Age": 7, "Class": "First"}
    print("dict['Name']: ", dict_b["Name"])
    print("dict['Age']: ", dict_b["Age"])
    # 如果用字典里没有的键访问数据，会输出错误
    # TypeError: 'type' object is not subscriptable
    print("dict['Alice']: ", dict["Alice"])
