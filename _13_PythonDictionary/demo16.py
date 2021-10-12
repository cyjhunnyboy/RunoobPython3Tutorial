# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字典
        字典内置方法
            Python3 字典get()方法
                描述：
                    Python 字典get()函数返回指定键的值
                语法：
                    dict.get(key, default=None)
                参数：
                    key -- 字典中要查找的键。
                    default -- 如果指定键的值不存在时，返回该默认值。
                返回值：
                    返回指定键的值，如果键不在字典中返回默认值None或者指定的默认值
"""
if __name__ == "__main__":
    dict_a = {"Name": "Runoob", "Age": 27}

    print("Age值为：%s" % dict_a.get("Age"))
    print("Sex值为：%s" % dict_a.get("Sex", "NA"))
