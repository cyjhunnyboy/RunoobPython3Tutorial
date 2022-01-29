# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 移除字典点键值(key/value)对
    给定一个字典，然后计算它们所有数字值的和。
'''
if __name__ == "__main__":
    # 使用items()移除
    test_dict = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}

    # 输出原始的字典
    print("字典移除前：" + str(test_dict))

    # 使用pop移除Zhihu
    new_dict = {key: val for key, val in test_dict.items() if key != "Zhihu"}

    # 输出移除后的字典
    print("字典移除后：" + str(new_dict))
