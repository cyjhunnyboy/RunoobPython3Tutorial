# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字典
        字典内置方法
            Python3 字典in操作符
                描述：
                    Python字典in操作符用于判断键是否存在于字典中，如果键在字典dict里返回true，否则返回false。
                    而not in操作符刚好相反，如果键在字典dict里返回false，否则返回true。
                语法：
                    key in dict
                    参数：
                        key -- 要在字典中查找的键
                返回值：
                    如果键在字典里返回true，否则返回false
"""
if __name__ == "__main__":
    dict_a = {"Name": "Runoob", "Age": 7}

    # 检测键Age是否存在
    if "Age" in dict_a:
        print("键Age存在")
    else:
        print("键Age不存在")

    # 检测键Sex是否存在
    if "Sex" in dict_a:
        print("键Sex存在")
    else:
        print("键Sex不存在")

    # not in
    # 检测键Age是否存在
    if "Age" not in dict:
        print("键Age不存在")
    else:
        print("键Age存在")
