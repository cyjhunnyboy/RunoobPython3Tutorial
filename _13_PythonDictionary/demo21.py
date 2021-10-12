# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字典
        字典内置方法
            Python3 字典setdefault()方法
                描述：
                    Python字典setdefault()方法和get()方法类似, 如果键不已经存在于字典中，将会添加键并将值设为默认值。
                语法：
                    dict.setdefault(key, default=None)
                    参数
                        key -- 查找的键值。
                        default -- 键不存在时，设置的默认键值。
                返回值
                    如果key在字典中，返回对应的值。如果不在字典中，
                    则插入key及设置的默认值default，并返回default，default默认值为None
"""
if __name__ == "__main__":
    dict_a = {"Name": "Runoob", "Age": 7}
    print("Age键的值为：%s" % dict_a.setdefault("Age", None))
    print("Sex键的值为：%s" % dict_a.setdefault("Sex", None))
    print("新字典为：", dict_a)
